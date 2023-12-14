import psycopg2
import pandas as pd
from minio import Minio
from minio.error import S3Error
import pyarrow as pa
import pyarrow.parquet as pq
from io import BytesIO
from sqlalchemy import create_engine

pg_host = "localhost"
pg_user = "postgres"
pg_password = "postgres"
pg_db = "postgres"

minio_endpoint = "localhost:9000"
minio_access_key = "HC9UoYAg9etUDaq7xYuZ"
minio_secret_key = "3vzwJcATu9zLKcqVnGHUcphqlCJJMK8n6x6Wi3YZ"
minio_bucket = "raw"

tables = ["stations", "status", "trips"]

minio_client = Minio(minio_endpoint, access_key=minio_access_key, secret_key=minio_secret_key, secure=False)
connection = psycopg2.connect(host=pg_host, user=pg_user, password=pg_password, dbname=pg_db)
engine = create_engine(f"postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}/{pg_db}")

for table in tables:
    sql_query = f"SELECT * FROM {table}"
    df = pd.read_sql_query(sql_query, engine)
    parquet_buffer = BytesIO()
    pq.write_table(pa.Table.from_pandas(df), parquet_buffer)
    parquet_buffer.seek(0)
    minio_client.put_object(minio_bucket, f"{table}.parquet", parquet_buffer, parquet_buffer.getbuffer().nbytes,
                            'application/octet-stream')

connection.close()
print("Done!")
