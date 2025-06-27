# 2_task Insert data
population = (
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys',	'Bajoran',	29)
)
with sqlite3.connect("roster.db") as con:
    cursor = con.cursor()
    place_holder = ", ".join(["?"] * 3)
    cursor.executemany("Insert into Rosters Values({place_holder})", population)