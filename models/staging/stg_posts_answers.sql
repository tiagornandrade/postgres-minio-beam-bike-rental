{{
    config(
        materialized='view'
    )
}}

select
  id as post_id,
  creation_date as created_at,
  'answer' as type,
  title,
  body,
  owner_user_id,
  cast(parent_id as string) as parent_id
from
  {{ source('staging','posts_answers') }}
where
  -- limit to recent data for the purposes of this demo project
  creation_date >= timestamp( "{{ var('data_inicial') }}" ) AND creation_date < timestamp( "{{ var('data_final') }}" )