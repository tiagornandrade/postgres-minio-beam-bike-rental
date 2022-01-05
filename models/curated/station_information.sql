{{
  config(
    materialized = 'incremental',
    schema = 'curated',
    uniqueKey = ['station_id'],
    merge_update_columns = ['last_updated', 'station_id'],
    timestamp_field = 'last_updated',
    partition_by = {
      'field': 'last_updated',
      'data_type': 'timestamp',
      'granularity': 'day'
    }
  )
}} 

WITH table_struct AS (
  SELECT
    {{ fieldsStationInformation() }}
  FROM
    {{ source('raw','station_information') }},
    UNNEST(data.stations) as stations
),

{{ loadInitialTable() }}
{{ loadFinalTable() }}

base AS (
  {{ loadBaseTable() }}
)

SELECT * FROM base
{% if is_incremental() %}
WHERE DATE(last_updated) > (SELECT max(DATE(last_updated)) FROM {{ this }})
{% endif %}