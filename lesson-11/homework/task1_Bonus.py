# 6. Bonus Task
with sqlite3.connect("roster.db") as con:
    cursor = con.cursor()
    cursor.execute("ALTER TABLE Rosters ADD COLUMN Rank text")

rank = [
    ('Captain', 'Benjamin Sisko'),
    ('Lieutenant', 'Ezri Dax'),
    ('Major', 'Kira Nerys')
]

with sqlite3.connect("roster.db") as con:
    cursor = con.cursor()
    cursor.executemany("UPDATE Rosters SET Rank = ? WHERE Name = ?", rank)
