from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import EnvironmentSettings, StreamTableEnvironment

env_settings = EnvironmentSettings.new_instance().in_streaming_mode().build()
env = StreamExecutionEnvironment.get_execution_environment()
table_env = StreamTableEnvironment.create(env, environment_settings=env_settings)

jdbc_url = "jdbc:postgresql://localhost:5432/postgresql"
jdbc_driver = "org.postgresql.Driver"
jdbc_username = "postgresql"
jdbc_password = "postgresql"


table_env.execute_sql("""
    CREATE TABLE stations_landing (
        station_id INT,
        name STRING,
        latitude INT,
        longitude INT,
        dockcount INT,
        landmark STRING,
        installation_date TIMESTAMP
    ) WITH (
        'connector' = 'stations_raw',
        'fields.id.kind' = 'sequence',
        'fields.id.start' = '1',
        'fields.id.end' = '10'
    )
""")

table_env.execute_sql(
    """
    CREATE TABLE stations_raw (
        station_id INT,
        name STRING,
        latitude INT,
        longitude INT,
        dockcount INT,
        landmark STRING,
        installation_date TIMESTAMP
    ) WITH (
        'connector' = 'stations_raw'
    )
    """)

source_table = table_env.from_path("stations_raw")
source_table = table_env.sql_query("SELECT * FROM stations_landing")

result_table = source_table.select("station_id + 1, name, latitude, longitude, dockcount, landmark, installation_date")
result_table.execute_insert("print").wait()
table_env.execute_sql("INSERT INTO stations_raw SELECT * FROM stations_landing").wait()
