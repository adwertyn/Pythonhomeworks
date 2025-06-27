# 6. Bonus Task
with sqlite3.connect("library.db") as con:
    cursor = con.cursor()
    cursor.execute("ALTER TABLE Library ADD COLUMN Rating Real")
    
ratings = [
    (4.8, 'To Kill a Mockingbird'),
    (4.7, '1984'),
    (4.5, 'The Great Gatsby')
]

with sqlite3.connect("library.db") as con:
    cursor = con.cursor()
    cursor.executemany("UPDATE Library SET Rating = ? WHERE Title = ?", ratings)