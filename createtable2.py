import sqlite3 as lite
con=lite.connect('test.db')
def input_fun():
    a=int(input("enter id:"))
    b=input("enter name:")
    b=" ' "+b+" ' "
    c=int(input("enter price:"))
    str1="INSERT INTO Cars VALUES({},{},{})".format(a,b,c)
    return str1
with con:
    cur=con.cursor()
    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute("CREATE TABLE Cars(Id INT,Name TEXT,Price INT)")
    print("table created")
    cur.execute(input_fun())
    print("values in the table car inserted.")
