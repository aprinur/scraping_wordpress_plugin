from sqlalchemy import Column, String, Integer, Float
from source import Base, engine, TABLE


class Format_SQL(Base):
    __tablename__ = TABLE

    id = Column(Integer, primary_key=True)
    Name = Column(String, unique=True)
    Release_Date = Column(String, nullable=False)
    Last_Update = Column(String, nullable=False)
    Number_of_Rating = Column(Integer, nullable=False)
    Rating = Column(Float, nullable=False)
    Plugin_Link = Column(String, nullable=False)


Base.metadata.create_all(engine)