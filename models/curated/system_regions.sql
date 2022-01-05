{{
  config(
    materialized = 'incremental',
    schema = 'curated',
    uniqueKey = ['last_updated','region_id','name'],
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
    {{ fieldsSystemRegions() }}
  FROM
    {{ source('raw','system_regions') }},
    UNNEST(data.regions) AS regions
)

SELECT * FROM base
{% if is_incremental() %}
WHERE DATE(last_updated) > (SELECT max(DATE(last_updated)) FROM {{ this }})
{% endif %}