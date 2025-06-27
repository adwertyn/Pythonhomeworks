# 5. Delete data
with sqlite3.connect('roster.db') as con:
    cursor = con.cursor()
    cursor.execute("DELETE FROM Rosters WHERE Age > 100")