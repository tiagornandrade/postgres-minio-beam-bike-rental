{{
    config(
        materialized='view'
    )
}}

select
  id as user_id,
  age,
  creation_date,
  round(timestamp_diff(current_timestamp(), creation_date, day)/31) as user_tenure
from
  {{ source('staging','users') }}
where
  -- limit to recent data for the purposes of this demo project
  creation_date >= timestamp( "{{ var('data_inicial') }}" ) AND creation_date < timestamp( "{{ var('data_final') }}" )