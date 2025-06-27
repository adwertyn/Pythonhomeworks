# 4. Query Data
with sqlite3.connect('roster.db') as con:
    cursor = con.cursor()
    data = cursor.execute("SELECT Name, Age FROM Rosters WHERE Species = 'Bajoran'")
    data.fetchall()
print(data)
    