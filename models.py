from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///emeraldblog.db')
base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


class Post(base):

    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    subtitle = Column(String(50))
    author = Column(String(50))
    date = Column(DateTime, default=func.now())
    content = Column(Text(10000))
