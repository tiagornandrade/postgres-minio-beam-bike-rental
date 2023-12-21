from generate import FakerEvents


if __name__ == "__main__":
    db_uri = "postgresql://postgres:postgres@localhost:5432/postgres"
    fake_events = FakerEvents(db_uri)

    fake_events.create_stations(100)
    fake_events.create_status(100)
    fake_events.create_trips(100)