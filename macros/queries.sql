{% macro fieldsFreeBikes() %}
  TIMESTAMP_SECONDS(last_updated) AS last_updated
  , data.bikes
{% endmacro %}

{% macro fieldsStationInformation() %}
  ttl
  , last_updated
  , stations.capacity
  , stations.station_id
  , stations.eightd_has_key_dispenser
  , stations.external_id
  , stations.rental_methods
  , stations.rental_uris.android
  , stations.rental_uris.ios
  , stations.region_id
  , stations.name
  , stations.lon
  , stations.legacy_id
  , stations.station_type
  , stations.electric_bike_surcharge_waiver
  , stations.short_name
  , stations.lat
  , stations.has_kiosk
{% endmacro %}

{% macro loadInitialTable() %}
  load_table AS (
    SELECT 
      *
    FROM table_struct,
    UNNEST(rental_methods) as rental_methods
  ),
{% endmacro %}

{% macro loadFinalTable() %}
  final_table AS (
    SELECT
      * except (rental_methods)
    FROM load_table
  ),
{% endmacro %}

{% macro loadBaseTable() %}
  SELECT
    TIMESTAMP_SECONDS(last_updated) AS last_updated
    , capacity
    , station_id
    , eightd_has_key_dispenser
    , external_id
    , 'KEY' AS rental_methods
    , android
    , ios
    , region_id
    , name
    , lon
    , legacy_id
    , station_type
    , electric_bike_surcharge_waiver
    , short_name
    , lat
    , has_kiosk	
  FROM final_table
  GROUP BY 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17
{% endmacro %}

{% macro fieldsStationStatus() %}
  TIMESTAMP_SECONDS(last_updated) AS last_updated 
  , stations.legacy_id
  , stations.num_docks_available
  , stations.is_renting
  , stations.is_installed
  , TIMESTAMP_SECONDS(stations.last_reported) AS last_reported
  , stations.station_id
  , stations.eightd_has_available_keys
  , stations.num_ebikes_available
  , stations.num_docks_disabled
  , stations.is_returning
  , stations.station_status
  , stations.num_bikes_disabled
  , stations.num_bikes_available
{% endmacro %}

{% macro fieldsSystemAlerts() %}
  TIMESTAMP_SECONDS(t.last_updated) AS last_updated
  , alerts.type
  , TIMESTAMP_SECONDS(alerts.last_updated) AS lastUpdated
  , alerts.description
  , alerts.summary
  , alerts.url
  , alerts.alert_id
  , TIMESTAMP_SECONDS(times.end) AS time_end
  , TIMESTAMP_SECONDS(times.start) AS time_start
{% endmacro %}

{% macro fieldsSystemCalendar() %}
  TIMESTAMP_SECONDS(last_updated) AS last_updated
  , calendars.end_month
  , calendars.end_day
  , calendars.start_month
  , calendars.start_day
{% endmacro %}

{% macro fieldsSystemHours() %}
  TIMESTAMP_SECONDS(last_updated) AS last_updated
  , data.rental_hours
{% endmacro %}

{% macro fieldsSystemInformation() %}
  TIMESTAMP_SECONDS(last_updated) AS last_updated
  , data.start_date
  , data.timezone
  , data.operator
  , data.license_url
  , data.purchase_url
  , data.language
  , data.name
  , data.system_id
  , data.short_name
  , data.phone_number
  , data.email
  , data.url
{% endmacro %}

{% macro fieldsSystemRegions() %}
  TIMESTAMP_SECONDS(last_updated) AS last_updated
  , regions.region_id
  , regions.name
{% endmacro %}