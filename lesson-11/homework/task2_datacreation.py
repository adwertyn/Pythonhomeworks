#  1. Data creation
import sqlite3

with sqlite3.connect('library.db') as con:
    cursor = con.cursor()
    query = """
        Drop table if exists Library;
        Create table Library(
            Title text,
            Author text,
            Year_Published int,
            Genre text
        )
    """ 
    cursor.executescript(query)