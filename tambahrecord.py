from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User

engine = create_engine('sqlite:///latihan.db')
DBSession = sessionmaker()
DBSession.configure(bind=engine)
session = DBSession()

new_user = User(username='coba', password='coba')
session.add(new_user)
session.commit()