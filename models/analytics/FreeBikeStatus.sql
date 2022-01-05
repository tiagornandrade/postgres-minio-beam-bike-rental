{{
  config(
    materialized = 'incremental',
    schema = 'analytics',
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
  *
FROM
  {{ source('curated','free_bike_status') }}
{% if is_incremental() %}
WHERE DATE(last_updated) > (SELECT max(DATE(last_updated)) FROM {{ this }})
{% endif %}
