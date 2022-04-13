import sqlite3

def make_connection():
      conn = sqlite3.connect("books.db")
      cur = conn.cursor()
      return conn,cur


def get_all_books():
    conn,cur = make_connection()
    cur.execute("""Select * from books""")
    books = cur.fetchall()
    conn.commit()
    return books

def search_in_db(id):

    conn,cur = make_connection()
    cur.execute("""Select * from books where book_id=?""",id)
    book = cur.fetchall()
    conn.commit()
    conn.close()
    return book

def add_in_db(id,name):
  try:  
    conn,cur = make_connection()
    cur.execute("""Insert into books(book_id,book_name) Values(?,?)""",(id,name))
    conn.commit()
    conn.close()
    return "Done!"
  except:
    return "Error!"


