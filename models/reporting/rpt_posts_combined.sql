{{
    config(
      materialized='incremental',
      uniqueKey='post_id',
      timestamp_field = 'created_at',
      partition_by={
       'field': 'created_at',
       'data_type': 'timestamp',
       'granularity': 'day'
      }
    )
}} 

select
  post_id,
  created_at,
  type,
  title,
  body,
  owner_user_id,
  parent_id
from
  {{ ref('stg_posts_answers') }}
  {% if is_incremental() %}
    WHERE created_at > (SELECT MAX(created_at) FROM {{ this }})
  {% endif %}

union all

select
  post_id,
  created_at,
  type,
  title,
  body,
  owner_user_id,
  parent_id
from
  {{ ref('stg_posts_questions') }}
  {% if is_incremental() %}
    WHERE created_at > (SELECT MAX(created_at) FROM {{ this }})
  {% endif %}