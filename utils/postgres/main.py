import os
from generate import FakerEvents
from dotenv import load_dotenv


load_dotenv()

if __name__ == "__main__":
    db_uri = os.getenv("DB_URI")
    fake_events = FakerEvents(db_uri)

    fake_events.create_stations(100)
    fake_events.create_status(100)
    fake_events.create_trips(100)
