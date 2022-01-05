{{
  config(
    materialized = 'incremental',
    schema = 'curated',
    uniqueKey = ['last_updated','legacy_id','num_docks_available','is_renting','is_installed','last_reported','station_id','eightd_has_available_keys','num_ebikes_available','num_docks_disabled','is_returning','station_status','num_bikes_disabled','num_bikes_available'],
    merge_update_columns = ['last_updated', 'station_id'],
    timestamp_field = 'last_updated',
    partition_by = {
      'field': 'last_updated',
      'data_type': 'timestamp',
      'granularity': 'day'
    }
  )
}} 

WITH base AS (
  SELECT
    {{ fieldsStationStatus() }}
  FROM
    {{ source('raw','station_status') }},
    UNNEST(data.stations) AS stations
)

SELECT * FROM base
{% if is_incremental() %}
WHERE DATE(last_updated) > (SELECT max(DATE(last_updated)) FROM {{ this }})
{% endif %}