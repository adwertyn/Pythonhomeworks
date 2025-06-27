# 2_task Insert data
books = (
    ('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
    ('1984','George Orwell', 1949, 'Dystopian'),
    ('The Great Gatsby','F. Scott Fitzgerald', 1925, 'Classic')
)
with sqlite3.connect("library.db") as con:
    cursor = con.cursor()
    place_holder = ", ".join(["?"] * 4)
    cursor.executemany("Insert into Library Values({place_holder})", books)
