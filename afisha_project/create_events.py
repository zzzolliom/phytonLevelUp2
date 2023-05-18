from CREATE_BD  import Events

from CREATE_BD  import cities
from CREATE_BD  import Event_type
from CREATE_BD  import platforms


import requests
from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///my.db_2')

Session = sessionmaker(bind=engine)
session = Session()


response = requests.get('https://kudago.com/public-api/v1.4/places') #надо собрать со всех страниц - пока 20 по умолчанию взято
data = response.json()
print(data)
events_lst = []

for event in data['results']:
    title = event["title"]
    # description = events["description"]
    event_link = event["site_url"]
    city_slug = event['location']
    city = session.query(cities).filter_by(slug=city_slug).first()
    city_id = city.id if city else None

    platform_slug = event['slug']
    platform = session.query(platforms).filter_by(slug=platform_slug).first()
    platform_id = platform.id if platform else None
    create_at = datetime.now()
    events_lst.append(Events(title=title,  event_link=event_link, city_slug=city_slug,  city_id=city_id, platform_slug=platform_slug, platform_id=platform_id, create_at=create_at))


for p in events_lst:
    session.add(p)
session.commit()
