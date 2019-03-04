import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    c=conn.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS book (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,title TEXT NOT NULL ,author TEXT NOT NULL,year INTEGER NOT NULL,isbn INTEGER NOT NULL)")
    conn.commit()

    conn.close()

def insert(title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    c=conn.cursor()
    c.execute("INSERT INTO book(title,author,year,isbn) VALUES(?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def views():
    conn=sqlite3.connect("books.db")
    c=conn.cursor()
    c.execute("SELECT * FROM book")
    rows=c.fetchall()
    conn.close()
    return rows

def select(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("books.db")
    c=conn.cursor()
    c.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    rows=c.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    c=conn.cursor()
    c.execute("DELETE FROM  book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title="",author="",year="",isbn=""):
    conn=sqlite3.connect("books.db")
    c=conn.cursor()
    c.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()



connect()

#print (views())
#print(select(title="Pagal Manxey"))
#delete(13)
#update(12,title="pagal maaaanxey")

#print (views())
