import random
from faker import Faker
from datetime import datetime


class FakeDataGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate_fake_station(self):
        return {
            "station_id": random.randint(1, 1000000),
            "name": self.fake.name(),
            "latitude": self.fake.latitude(),
            "longitude": self.fake.longitude(),
            "dockcount": random.randint(1, 1000),
            "landmark": self.fake.city(),
            "installation_date": self.fake.date_time_between(
                start_date="-30y", end_date="now"
            ),
            "created_at": datetime.now(),
        }

    def generate_fake_status(self):
        return {
            "station_id": random.randint(1, 1000000),
            "bikes_available": random.randint(1, 1000),
            "docks_available": random.randint(1, 1000),
            "time": self.fake.date_time_between(start_date="-30y", end_date="now"),
            "created_at": datetime.now(),
        }

    def generate_fake_trip(self):
        return {
            "trip_id": random.randint(1, 1000000),
            "duration_sec": random.randint(1, 1000),
            "start_date": self.fake.date_time_between(
                start_date="-30y", end_date="now"
            ),
            "start_station_name": self.fake.name(),
            "start_station_id": random.randint(1, 1000),
            "end_date": self.fake.date_time_between(start_date="-30y", end_date="now"),
            "end_station_name": self.fake.name(),
            "end_station_id": random.randint(1, 1000),
            "bike_number": random.randint(1, 1000),
            "zip_code": self.fake.zipcode(),
            "subscriber_type": self.fake.name(),
            "created_at": datetime.now(),
        }
