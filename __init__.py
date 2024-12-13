from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

URl = 'https://public-api.wordpress.com/rest/v1.3/marketplace/search?'

DB_URL = f'sqlite:///D:/Github/aprinur/Scraping_Wordpress_plugin/wordpress_plugin.db'
engine = create_engine(DB_URL, echo=False)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()
