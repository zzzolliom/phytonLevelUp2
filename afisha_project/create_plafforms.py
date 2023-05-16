from CREATE_BD  import cities

from CREATE_BD  import platforms


import requests


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///my.db_2')

Session = sessionmaker(bind=engine)
session = Session()


response = requests.get('https://kudago.com/public-api/v1.4/places') #надо собрать со всех страниц - пока 20 по умолчанию взято
data = response.json()
print(data)
places_lst = []

for places in data['results']:
    slug = places["slug"]
    name = places["title"]
    city_slug = places['location']
    address = places['address']
    city = session.query(cities).filter_by(slug=city_slug).first()
    city_id = city.id if city else None
    places_lst.append(platforms(slug=slug, name=name, city_id=city_id))


for p in places_lst:
    session.add(p)
session.commit()
