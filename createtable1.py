import sqlite3 as lite
cars=(
    (1,'audi',52642),
    (2,'mercedes',57127),
    (3,'skoda',9000),
    (4,'volvo',29000),
    (5,'beatley',350000),
    (6,'hummer',41400),
    (7,'volkswagen',21600),
)
con=lite.connect('test.db')
with con:
    cur=con.cursor()
    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute("CREATE TABLE Cars(Id INT,Name TEXT,Price INT)")
    cur.executemany("INSERT INTO Cars VALUES(?,?,?)",cars)
