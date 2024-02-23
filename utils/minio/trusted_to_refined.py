import os
import pandas as pd
from minio import Minio
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()

minio_endpoint = os.getenv("MINIO_ENDPOINT")
minio_access_key = os.getenv("MINIO_ACCESS_KEY")
minio_secret_key = os.getenv("MINIO_SECRET_KEY")
trusted_bucket = "trusted"
refined_bucket = "refined"


def download_data_from_minio(table):
    minio_client = Minio(
        minio_endpoint,
        access_key=minio_access_key,
        secret_key=minio_secret_key,
        secure=False,
    )

    object_data = minio_client.get_object(trusted_bucket, f"{table}.csv")
    df = pd.read_csv(BytesIO(object_data.read()))

    return df


def promotion_to_refined():
    tables = ["stations", "status", "trips"]

    minio_client = Minio(
        minio_endpoint,
        access_key=minio_access_key,
        secret_key=minio_secret_key,
        secure=False,
    )

    for table in tables:
        df = download_data_from_minio(table)

        csv_buffer = BytesIO()
        df.to_csv(csv_buffer, index=False)
        csv_buffer.seek(0)

        minio_client.put_object(
            refined_bucket,
            f"{table}.csv",
            csv_buffer,
            len(csv_buffer.getvalue()),
            "text/csv",
        )
        print(f"Promoting trusted.{table} to from refined.{table}")

    print("Done!")


if __name__ == "__main__":
    promotion_to_refined()
