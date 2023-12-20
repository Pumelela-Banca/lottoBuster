"""
creates sql table to store daily numbers
"""

import sqlalchemy
import sqlite3


def create_table():
    """
    creates a table to store numbers and dates
    """
    connection = sqlite3.connect("database.db")
    connection.close()
    engine = sqlalchemy.create_engine("sqlite:///database.db")
    metadata = sqlalchemy.MetaData()
    draw = sqlalchemy.Table("daily_numbers", metadata,
                            sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                            sqlalchemy.Column("date", sqlalchemy.String),
                            sqlalchemy.Column("numbers", sqlalchemy.String))
    metadata.create_all(engine)
