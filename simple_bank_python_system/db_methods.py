import sqlite3
from tkinter import E

def establish_a_connection():
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    return cur,con


def initializing_the_db():
    cur,con = establish_a_connection()
    cur.execute("""CREATE TABLE IF NOT EXISTS person(
        card_number INT PRIMARY KEY,
        id_number TEXT,
        date TEXT,
        age INT,
        date_of_birth TEXT,
        time_of_creation TEXT,
        initial_money INT);""")
    con.commit()
    con.close()
    cur.close()



def register_an_account(card_number,id_number,name,age,date_of_birth,time_of_creation,initial_money):
    
    initializing_the_db()
    cur,con = establish_a_connection()
    person = (card_number,id_number,name,age,date_of_birth,time_of_creation,initial_money)
    cur.execute("INSERT INTO person VALUES(?,?,?,?,?,?,?);",person)
    con.commit()
    con.close()
    cur.close()

    print("Created Successfully ")
    
def transfer_money(amount,sender,receiver):
  try:
    cur,con = establish_a_connection()
    cur.execute("SELECT * FROM person WHERE card_number=?", (sender,))
    row = cur.fetchone()
    sender_money = float(row[6])
    cur.execute("SELECT * FROM person WHERE card_number=?", (receiver,))
    row = cur.fetchone()
    receiver_money = float(row[6])

    if float(sender_money) >= amount:
       new_sender_money = sender_money - float(amount)
       new_receiver_money = receiver_money + float(amount)
       changes_for_sender = (new_sender_money,sender)  
       changes_for_receiver = (new_receiver_money,receiver)
       cur.execute("""Update person set initial_money = ? where card_number = ?""",changes_for_sender)
       con.commit()
       cur.execute("""Update person set initial_money = ? where card_number = ?""",changes_for_receiver)
       con.commit()

       print("Transferred Successfully ")
       
       con.close()
       cur.close()

    else:
        print("Insufficient Balance")
        
        con.close()
        cur.close()
  except:
      print("One Of The Numbers Is Incorrent") 
      con.close()
      cur.close()

def check_the_balance(card_number):
    cur,con = establish_a_connection()
    cur.execute("SELECT * FROM person WHERE card_number=?", (card_number,))
    row = cur.fetchone()
    balance = float(row[6])
    print(f"The Balance For {card_number} Is: {balance}")
    con.close()
    cur.close()


def delete_this_card_number(card_number):
    try:
      cur,con = establish_a_connection()
      cur.execute("DELETE FROM person WHERE card_number=?",(card_number))
      con.commit()
      print("Done!")
      cur.close()
      con.close()
    except:
        print("An Error Occured.There's A Chance That is Card Number Is Wrong")