{{ config(
    materialized="table",
    schema="trusted"
) }}

SELECT
    station_id
    , bikes_available
    , docks_available
    , time
FROM {{ source('data_lake_raw','status') }}