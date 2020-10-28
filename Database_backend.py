import sqlite3

def connect():
    conn =sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("create table if not exists book (id ENTER PRIMARY KEY,title text,author text,year integer,isbn integer)")
    conn.commit()
    conn.close()


def insert(title,author,year,isbn):
    conn =sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("insert into book values (NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn =sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("select * from book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title='',author='',year='',isbn=''):
    conn =sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("select * from book where title=? or author=? or year=? or isbn=?",(title,author,year,isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("delete from book where id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("update book SET title=?,author=?,year=?,isbn=? where id=? ",(id,title,author,year,isbn))
    conn.commit()
    conn.close()

connect()
#
# insert("The Mind","Siva",2020,10061991)
# print(view())
# print(delete(1))
# print(update(4,"vivek","earth",1929,165892))
# print(search(author='vivek'))