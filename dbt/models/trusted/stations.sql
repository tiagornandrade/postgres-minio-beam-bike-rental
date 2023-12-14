{{ config(
    materialized="table",
    schema="trusted"
) }}

SELECT
    station_id
    , name
    , latitude
    , longitude
    , dockcount
    , landmark
    , installation_date
FROM {{ source('data_lake_raw','stations') }}