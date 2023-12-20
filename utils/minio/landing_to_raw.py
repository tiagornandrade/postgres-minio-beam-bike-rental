import os
import psycopg2
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from minio import Minio
from minio.error import S3Error
from io import BytesIO
from sqlalchemy import create_engine
from dotenv import load_dotenv


load_dotenv()


pg_host = os.getenv("PG_HOST")
pg_user = os.getenv("PG_USER")
pg_password = os.getenv("PG_PASSWORD")
pg_db = os.getenv("PG_DB")

minio_endpoint = os.getenv("MINIO_ENDPOINT")
minio_access_key = os.getenv("MINIO_ACCESS_KEY")
minio_secret_key = os.getenv("MINIO_SECRET_KEY")
minio_bucket = "raw"


def process_etl():
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
