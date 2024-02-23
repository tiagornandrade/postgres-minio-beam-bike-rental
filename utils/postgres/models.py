from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


Base = declarative_base()


class Station(Base):
    __tablename__ = "stations"

    station_id = Column(Integer, primary_key=True)
    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    dockcount = Column(Integer)
    landmark = Column(String)
    installation_date = Column(DateTime)
    created_at = Column(DateTime)


class Status(Base):
    __tablename__ = "status"

    station_id = Column(Integer, primary_key=True)
    bikes_available = Column(Integer)
    docks_available = Column(Integer)
    time = Column(DateTime)
    created_at = Column(DateTime)


class Trips(Base):
    __tablename__ = "trips"

    trip_id = Column(Integer, primary_key=True)
    duration_sec = Column(Integer)
    start_date = Column(DateTime)
    start_station_name = Column(String)
    start_station_id = Column(Integer)
    end_date = Column(DateTime)
    end_station_name = Column(String)
    end_station_id = Column(Integer)
    bike_number = Column(Integer)
    zip_code = Column(String)
    subscriber_type = Column(String)
    created_at = Column(DateTime)
