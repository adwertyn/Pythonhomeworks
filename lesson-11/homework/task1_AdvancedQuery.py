# 7. Advanced Query
with sqlite3.connect("roster.db") as con:
    cursor = con.cursor()
    cursor.execute("Select * From Rosters order by Age desc")