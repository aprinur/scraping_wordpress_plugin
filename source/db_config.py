from sqlalchemy import Column, String, Integer, Float, inspect
from source import Base, engine
from typing import Type


class WP_PLugins(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    Name = Column(String, unique=True)
    Release_Date = Column(String, nullable=False)
    Last_Update = Column(String, nullable=False)
    Number_of_Rating = Column(Integer, nullable=False)
    Rating = Column(Float, nullable=False)
    Plugin_Link = Column(String, nullable=False)


def get_existing_table_class(tablename: str) -> Type[WP_PLugins]:
    """ Get existing table with WP_Plugins class structure

        Args:
            tablename(str): table name from database to add data

        Returns:
            Type[WP_PLugins]: A dynamically created class representing the existing table structure.
            """
    inspector = inspect(engine)

    if not inspector.has_table(tablename):
        raise ValueError(f'Table{tablename} does not exist in the database')

    class ExistingTable(WP_PLugins):
        __tablename__ = tablename
        __table_args__ = {'extend_existing': True}

    return ExistingTable


def create_db_table(tablename: str) -> Type[WP_PLugins]:
    """Create new table based on WP_Plugins class structure

        Args:
            tablename (str): The name of the new table to create.

        Returns:
            Type[WP_PLugins]: A dynamically created class representing the new table structure."""
    class DynamicTable(WP_PLugins):
        __tablename__ = tablename
        __table_args__ = {'extend_existing': True}

    Base.metadata.create_all(engine)
    return DynamicTable