# 5. Delete data
with sqlite3.connect("library.db") as con:
    cursor = con.cursor()
    cursor.execute("DELETE FROM Library WHERE Year_Published < 1950")