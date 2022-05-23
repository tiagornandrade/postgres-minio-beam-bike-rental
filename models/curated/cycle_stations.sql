{{ config(
    materialized="table",
    schema="curated"
) }}

SELECT
    id
    , name
    , locked
    , latitude
    , installed
    , longitude
    , temporary
    , bikes_count
    , docks_count
    , install_date
    , nbEmptyDocks
    , removal_date
    , terminal_name
    , _airbyte_ab_id as airbyte_id
    , _airbyte_emitted_at as airbyte_created
FROM {{ source('raw','cycle_stations') }}