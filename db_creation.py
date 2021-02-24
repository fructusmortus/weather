from sqlalchemy import create_engine, func, Column, Integer, String, ForeignKey, DateTime, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
engine = create_engine("postgresql://postgres:123QWEasd@localhost:5432/api_data_test_2")


class Country(Base):
    __tablename__ = "country"

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    name = Column('name', String, unique=True)
    news = relationship("News", back_populates="country")


class News(Base):
    __tablename__ = "news"

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    country_id = Column(Integer, ForeignKey('country.id'))
    country = relationship("Country", back_populates="news")
    title = Column('title', String)
    body = Column('body', String)
    date = Column('dateadded', DateTime, default=func.now())


class City(Base):
    __tablename__ = "city"

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    name = Column('name', String, unique=True)
    weather = relationship("Weather", back_populates="city")


class Weather(Base):
    __tablename__ = "weather"

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    city_id = Column(Integer, ForeignKey('city.id'))
    city = relationship("City", back_populates="weather")
    weather_info = Column('weather_info', String)
    temp_in_c = Column('temp_in_c', Integer)
    wind_speed_kmph = Column('wind_speed_kmph', Integer)
    date = Column('dateadded', DateTime, default=func.now())


Base.metadata.create_all(bind=engine)
