import random
from faker import Faker
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from models import Base, Station, Status, Trips
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from schemas import FakeDataGenerator


class FakerEvents:
    def __init__(self, db_uri):
        self.engine = create_engine(db_uri)
        Base.metadata.create_all(bind=self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.fake_data_generator = FakeDataGenerator()

    def generate_fake_data(self, sample_size, generate_function):
        fake_data = []
        for _ in range(sample_size):
            fake_data.append(generate_function())
        return fake_data

    def create_stations(self, x):
        fake_stations = self.generate_fake_data(
            x, self.fake_data_generator.generate_fake_station
        )
        with self.Session() as session:
            try:
                for __fake_station in fake_stations:
                    print("Inserting status:", __fake_station)
                    existing_stations = session.query(Station).get(
                        __fake_station["station_id"]
                    )
                    if existing_stations:
                        existing_stations.update(__fake_station)
                    else:
                        stations = Station(**__fake_station)
                        session.add(stations)

                session.commit()
                print("Stations inserted successfully.")
            except Exception as e:
                print("Error inserting status:", e)
                session.rollback()

    def create_status(self, x):
        fake_status = self.generate_fake_data(
            x, self.fake_data_generator.generate_fake_status
        )
        with self.Session() as session:
            try:
                for __fake_status in fake_status:
                    print("Inserting status:", __fake_status)
                    existing_status = session.query(Status).get(
                        __fake_status["station_id"]
                    )
                    if existing_status:
                        existing_status.update(__fake_status)
                    else:
                        status = Status(**__fake_status)
                        session.add(status)

                session.commit()
                print("Status inserted successfully.")
            except Exception as e:
                print("Error inserting status:", e)
                session.rollback()

    def create_trips(self, x):
        fake_trips = self.generate_fake_data(
            x, self.fake_data_generator.generate_fake_trip
        )
        with self.Session() as session:
            try:
                for __fake_trip in fake_trips:
                    print("Inserting trip:", __fake_trip)
                    existing_trip = session.query(Trips).get(__fake_trip["trip_id"])
                    if existing_trip:
                        existing_trip.update(__fake_trip)
                    else:
                        trip = Trips(**__fake_trip)
                        session.add(trip)

                session.commit()
                print("Trips inserted successfully.")
            except Exception as e:
                print("Error inserting trips:", e)
                session.rollback()

    def create_engine_and_session(db_uri):
        engine = create_engine(db_uri)
        Base.metadata.create_all(bind=engine)
        Session = sessionmaker(bind=engine)
        return engine, Session
