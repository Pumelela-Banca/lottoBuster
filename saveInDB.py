"""
Saves collected numbers into a database
"""
import sqlalchemy
from sqlalchemy.orm import sessionmaker
import create_db


def save_number(date, numbers):
    """
    Saves numbers into sql db
    """
    engine2 = sqlalchemy.create_engine("sqlite:///database.db")
    session = sessionmaker(bind=engine2)()
    metadata2 = sqlalchemy.MetaData()
    my_table = sqlalchemy.Table("daily_numbers",
                                metadata2,
                                autoload_with=engine2)
    # Inserting into table
    add_in = my_table.insert().values(date=date, numbers=numbers)
    session.execute(add_in)
    session.commit()
    session.close()
