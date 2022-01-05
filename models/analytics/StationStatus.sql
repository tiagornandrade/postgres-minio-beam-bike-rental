{{
  config(
    materialized = 'incremental',
    schema = 'analytics',
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

SELECT
  *
FROM
  {{ source('curated','station_status') }}
{% if is_incremental() %}
WHERE DATE(last_updated) > (SELECT max(DATE(last_updated)) FROM {{ this }})
{% endif %}
