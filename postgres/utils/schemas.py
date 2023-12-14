import random
from faker import Faker

fake = Faker()


def stations_schema(*args):
    return {
        "station_id": lambda: random.randint(1, 1000),
        "name": lambda: fake.name(),
        "latitude": lambda: fake.latitude(),
        "longitude": lambda: fake.longitude(),
        "dockcount": lambda: random.randint(1, 1000),
        "landmark": lambda: fake.city(),
        "installation_date": lambda: fake.date_time_between(start_date="-30y", end_date="now"),
    }


def status_schema(*args):
    return {
        "station_id": lambda: random.randint(1, 1000),
        "bikes_available": lambda: random.randint(1, 1000),
        "docks_available": lambda: random.randint(1, 1000),
        "time": lambda: fake.date_time_between(start_date="-30y", end_date="now"),
    }


def trips_schema(*args):
    return {
        "trip_id": lambda: random.randint(1, 1000),
        "duration_sec": lambda: random.randint(1, 1000),
        "start_date": lambda: fake.date_time_between(start_date="-30y", end_date="now"),
        "start_station_name": lambda: fake.name(),
        "start_station_id": lambda: random.randint(1, 1000),
        "end_date": lambda: fake.date_time_between(start_date="-30y", end_date="now"),
        "end_station_name": lambda: fake.name(),
        "end_station_id": lambda: random.randint(1, 1000),
        "bike_number": lambda: random.randint(1, 1000),
        "zip_code": lambda: fake.zipcode(),
        "subscriber_type": lambda: fake.name(),
    }
