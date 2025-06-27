# 3. Update
with sqlite3.connect("library.db") as con:
    cursor = con.cursor()
    cursor.execute("""
        UPDATE Library
        SET Year_Published = 1950
        WHERE Title = 1984
    """)