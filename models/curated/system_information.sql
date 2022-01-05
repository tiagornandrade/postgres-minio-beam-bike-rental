{{
  config(
    materialized = 'incremental',
    schema = 'curated',
    uniqueKey = ['last_updated','start_date','timezone','operator','license_url','purchase_url','language','name','system_id','short_name','phone_number','email','url'],
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
    {{ fieldsSystemInformation() }}
  FROM
    {{ source('raw','system_information') }}
)

SELECT * FROM base
{% if is_incremental() %}
WHERE DATE(last_updated) > (SELECT max(DATE(last_updated)) FROM {{ this }})
{% endif %}