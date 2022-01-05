{{
  config(
    materialized = 'incremental',
    schema = 'curated',
    uniqueKey = ['last_updated','type','lastUpdated','description','summary','url','alert_id','time_end','time_start'],
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
    {{ fieldsSystemAlerts() }}
  FROM
    {{ source('raw','system_alerts') }}  AS t,
    UNNEST(data.alerts) AS alerts,
    UNNEST(alerts.times) AS times
)

SELECT * FROM base
{% if is_incremental() %}
WHERE DATE(last_updated) > (SELECT max(DATE(last_updated)) FROM {{ this }})
{% endif %}