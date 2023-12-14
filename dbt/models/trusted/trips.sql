{{ config(
    materialized="table",
    schema="trusted"
) }}

SELECT
    trip_id
    , duration_sec
    , start_date
    , start_station_name
    , start_station_id
    , end_date
    , end_station_name
    , end_station_id
    , bike_number
    , zip_code
    , subscriber_type
FROM {{ source('data_lake_raw','trips') }}