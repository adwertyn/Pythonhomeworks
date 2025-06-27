# 7. Advanced Query
with sqlite3.connect("library.db") as con:
    cursor = con.cursor()
    cursor.execute("Select * From Library order by Year_Published asc")
    