{{
  config(
    materialized = 'incremental',
    schema = 'curated',
    uniqueKey = ['last_updated'],
    merge_update_columns = ['last_updated'],
    timestamp_field = 'last_updated',
    partition_by = {
      'field': 'last_updated',
      'data_type': 'timestamp',
      'granularity': 'day'
    }
  )
}}

SELECT
  {{ fieldsFreeBikes() }}
FROM
  {{ source('raw','free_bike_status') }}
{% if is_incremental() %}
WHERE last_updated >= (SELECT max(last_updated) FROM {{ this }})
{% endif %}