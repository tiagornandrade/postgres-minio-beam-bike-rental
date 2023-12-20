import os
import pandas as pd
from minio import Minio
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()

minio_endpoint = os.getenv("MINIO_ENDPOINT")
minio_access_key = os.getenv("MINIO_ACCESS_KEY")
minio_secret_key = os.getenv("MINIO_SECRET_KEY")
raw_bucket = "raw"
trusted_bucket = "trusted"

def promotion_to_trusted():
    tables = ["stations", "status", "trips"]

    print(f"Access Key: {minio_access_key}")
    minio_client = Minio(minio_endpoint, access_key=minio_access_key, secret_key=minio_secret_key, secure=False)

    for table in tables:
        df = pd.DataFrame({"column_name": ["example_value"]})

        csv_buffer = BytesIO()
        df.to_csv(csv_buffer, index=False)
        csv_buffer.seek(0)

        minio_client.put_object(trusted_bucket, f"{table}.csv", csv_buffer, len(csv_buffer.getvalue()), 'text/csv')

    print("Done!")

if __name__ == '__main__':
    promotion_to_trusted()
