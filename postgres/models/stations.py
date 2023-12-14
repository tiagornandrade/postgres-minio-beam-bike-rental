import os
from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))


Base = declarative_base()


class Stations(Base):
    __tablename__ = 'stations'

    station_id = Column(Integer, primary_key=True)
    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    dockcount = Column(Integer)
    landmark = Column(String)
    installation_date = Column(TIMESTAMP)


def create_engine_and_session(db_uri):
    engine = create_engine(db_uri)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    return engine, Session
