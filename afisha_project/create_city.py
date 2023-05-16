
from CREATE_BD  import cities
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///my.db_2')

Session = sessionmaker(bind=engine)
session = Session()

import requests

response = requests.get('https://kudago.com/public-api/v1.4/locations')
data = response.json()

cities_lst = []

for city in data:
    slug = city["slug"]
    name = city["name"]
    cities_lst.append(cities(slug=slug,name=name))
print(cities_lst)

for c in cities_lst:
    session.add(c)
session.commit()
