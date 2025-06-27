#  1. Data creation
import sqlite3

with sqlite3.connect('roster.db') as con:
    cursor = con.cursor()
    query = """
        Drop table if exists Rosters;
        Create table Rosters(
            Name text,
            Species text,
            Age int
        )
    """ 
    cursor.executescript(query)
