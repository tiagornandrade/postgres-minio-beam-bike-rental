{{ config(
    materialized="table",
    schema="curated"
) }}

SELECT
    bike_id
    , duration
    , end_date
    , rental_id
    , start_date
    , end_station_id
    , end_station_name
    , start_station_id
    , start_station_name
    , end_station_priority_id
    , end_station_logical_terminal
    , start_station_logical_terminal
    , _airbyte_ab_id as airbyte_id
    , _airbyte_emitted_at as airbyte_created
FROM {{ source('raw','cycle_hire') }}