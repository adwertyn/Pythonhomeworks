# 4. Query Data
with sqlite3.connect("library.db") as con:
    cursor = con.cursor()
    data = cursor.execute("SELECT Title, Author  FROM Library WHERE Genre = 'Dystopian'")
    data.fetchall()
print(data)