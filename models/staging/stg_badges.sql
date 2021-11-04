{{
    config(
        materialized='view'
    )
}}

select
  id as badge_id,
  name as badge_name,
  date as award_timestamp,
  user_id
from
  {{ source('staging','badges') }}
where 
  date >= timestamp( "{{ var('data_inicial') }}" ) AND date < timestamp( "{{ var('data_final') }}" )