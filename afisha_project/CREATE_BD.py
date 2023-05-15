#
# import sqlite3
#
# # Создание базы данных
# connection = sqlite3.connect('my.db')
#
# # Создание таблицы
# connection.execute('''CREATE TABLE IF NOT EXISTS users
#                       (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')






from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///my.db')
Base = declarative_base()
class Events(Base):
    __tablename__ = 'events'
    id = Column(Integer,primary_key = True)
    title = Column(String)
    description = Column(String)
    price_from = Column(Integer)
    price_to = Column(Integer)
    ivent_link = Column(String)
    city_id = Column(Integer, ForeignKey('cities.id'))
    platform_id = Column(Integer, ForeignKey('platforms.id'))
    not_intresting = Column(Boolean)
    create_at = Column(DateTime)
    is_new = Column(Boolean)

class Event_type(Base):
    __tablename__ = 'event_type'
    id = Column(Integer,primary_key = True)
    title = Column(String)
    description = Column(String)


class Event_genre(Base):
    __tablename__ = 'event_genre'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)

class Type_to_genre_relation(Base):
    __tablename__ = 'type_to_genre_relation'
    id = Column(Integer, primary_key=True)
    event_type_id = Column(Integer,  ForeignKey('event_type.id'))
    event_genre = Column(Integer,  ForeignKey('event_type.id'))
    event_id = Column(Integer, ForeignKey('events.id'))

class platforms(Base):
    __tablename__ = 'platforms'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    city_id = Column(Integer, ForeignKey('cities.id'))
class cities(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    slug = Column(String)



Base.metadata.create_all(engine)



