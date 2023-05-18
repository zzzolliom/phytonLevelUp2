from CREATE_BD  import Event_type
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///my.db_2')

Session = sessionmaker(bind=engine)
session = Session()

import requests

response = requests.get('https://kudago.com/public-api/v1.4/event-categories')
data = response.json()

event_types_lst = []
print(data )

for event_type in data:
    slug = event_type["slug"]
    name = event_type["name"]
    event_types_lst.append(Event_type(slug=slug,name=name))
print(event_types_lst)

for c in event_types_lst:
    session.add(c)
session.commit()
