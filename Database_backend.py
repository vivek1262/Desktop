import sqlite3

class Database:
    def __init__(self,db):
        self.conn =sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("create table if not exists book (id ENTER PRIMARY KEY,title text,author text,year integer,isbn integer)")
        self.conn.commit()



    def insert(self,title,author,year,isbn):
        conn =sqlite3.connect("books.db")
        cur = conn.cursor()
        self.cur.execute("insert into book values (NULL,?,?,?,?)",(self,title,author,year,isbn))
        conn.commit()
        conn.close()

    def view(self):
        self.cur.execute("select * from book")
        rows = self.cur.fetchall()
        conn.close()
        return rows

    def search(self,title='',author='',year='',isbn=''):
        self.cur.execute("select * from book where title=? or author=? or year=? or isbn=?",(title,author,year,isbn))
        rows = self.cur.fetchall()
        self.conn.close()
        return rows

    def delete(self,id):
        self.cur.execute("delete from book where id=?",(id,))
        self.conn.commit()


    def update(self,id,title,author,year,isbn):
        self.cur.execute("update book SET title=?,author=?,year=?,isbn=? where id=? ",(id,title,author,year,isbn))
        self.conn.commit()
        self.conn.close()

#
# insert("The Mind","Siva",2020,10061991)
# print(view())
# print(delete(1))
# print(update(4,"vivek","earth",1929,165892))
# print(search(author='vivek'))