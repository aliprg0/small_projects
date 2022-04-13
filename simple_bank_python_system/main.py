# I've just started learning Sqlite and this is simply just a program to test myself

from datetime import datetime
from db_methods import check_the_balance, delete_this_card_number, initializing_the_db,register_an_account, transfer_money
import random

print("Hello. Welcome To The RGBank.")

while True:
    print("--------------------------")
    print("1. Create An Account\n2.Transfer Money\n3.Delete Accoun\n4.Check The Balance")
    task = input( "What Can I Do For You?(Type the Number) : ")
    if task == "1":
     try:
      card_number = random.randint(100000000,999999999)  
      id_number = input("Type Your ID Number: ")
      name = input("Type Your Name: ")
      age = input("Type Your Age: ")
      date_of_birth = input("Type Your Date of Birth: ")
      time_of_creation = datetime.now()
      initial_money = float(input("Enter The Money You Want TO Start The Account With: "))

      register_an_account(card_number,id_number,name,age,date_of_birth,time_of_creation,initial_money)
      print(f"You Card Number Is: {card_number}")
     except ValueError:
        print("Oops!  That was no valid number.  Try again...")
     except:
        print("An Error Occurred.Try Again")


    elif task == "2":
      amount = float(input("Amount You Want TO Transfer: "))
      sender_card_number = int(input("Type Your Card Name: "))
      receiver_card_number = int(input("Type The Receiver Card Number: ")) 
      transfer_money(amount,sender_card_number,receiver_card_number)
    
    elif task == "3":
       delete_this_card_number(int(input("Type Your Card Number: ")))

    elif task == "4":
      card_number = int(input("Type Your Card Name: "))
      check_the_balance(card_number)

    else:
        print("Unknown Command!")

