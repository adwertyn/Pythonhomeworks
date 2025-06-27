# 3. Update
with sqlite3.connect('roster.db') as con:
    cursor = con.cursor()
    cursor.execute("""
        UPDATE Rosters
        SET Name = Ezri Dax
        WHERE Name = Jadzia Dax
    """)
