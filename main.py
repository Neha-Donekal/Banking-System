import tkinter as tk
import pymysql


con = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    password='Neha_41s',
    db='Bank Details',
    charset='utf8'
)

cur = con.cursor()

"""
If 1; then ask for bank:  photo ID, birthdate, SSN, an inital deposit amount, 
phone number
If 2; ask for username and password,then ask if check balance, deposit, 
withdraw, then ask for amount
If 3; sign an account closing form,
If 4; provide them all their information and ask which part needs to be 
modified(edit name, PIN, or any other personal identification required to 
open an account)
"""
print("\n\n Hello! Thank you for choosing our bank!")
def menu():
    return """
    Your options are:
    1) Create a new account
    2) Login to account 
    3) Close account
    4) Modify existing account
    5) Exit
     """


def create_account():
    name = input("Enter your name: ")
    username = input("Enter a username(no special characters): ")
    password = input("Enter a password(no special characters): ")
    balance = int(input("Enter an amount for inital deposit: $ "))
    sql4 = "INSERT INTO Customer_Details (Name, Username, Password, Balance) VALUES(%s,%s,%s,%s)"
    val = (name, username, password, balance)
    cur.execute(sql4, val)
    con.commit()
    return "A new account was created for you!"    



def login():
    user = input("Please enter your username: ")
    password1 = input("Please enter your password: ")
    sql1 = 'SELECT * FROM Customer_Details'
    cur.execute(sql1)
    rows = cur.fetchall()
    result = any(user in tu for tu in rows)
    result1 = any(password1 in tu for tu in rows)
    con.commit()
    if result == True and result1 == True:
        print('Login Successful!')
    else:
        print("Your username or password is wrong. Please try again!")


def close():
    sure = input("Are you sure you want to close your account? ").lower()
    if sure == 'yes':
        username1 = input("Please enter your username: ")
        password2 = input("Please enter your password: ")
        sql3 = "delete from Customer_Details where username = %s and password = %s"
        val = (username1, password2)
        cur.execute(sql3, val)
        con.commit()
        
    elif sure == 'no':
        return "You chose not to close your account!"
    

def modify():
    what = input("What would you like to modify in your account(name, username, or password)? ").lower()
    user = input("Please enter your username: ")
    password1 = input("Please enter your password: ")
    sql1 = 'SELECT * FROM Customer_Details'
    cur.execute(sql1)
    rows = cur.fetchall()
    result = any(user in tu for tu in rows)
    result1 = any(password1 in tu for tu in rows)
    con.commit()
    if result == True and result1 == True:
        if what == 'name':
            new = input("What would you like to change the name to? ")
            command = 'UPDATE Customer_Details SET Name = %s WHERE Username = %s'
            val = (new, user)
            cur.execute(command, val)
            con.commit()
        if what == 'username':
            new1 = input("What would you like to change the username to? ")
            command = 'UPDATE Customer_Details SET Username = %s WHERE Username = %s'
            val = (new1, user)
            cur.execute(command, val)
            con.commit()
        if what == 'password':
            new = input("What would you like to change the password to? ")
            command = 'UPDATE Customer_Details SET password = %s WHERE Username = %s'
            val = (new, user)
            cur.execute(command, val)
            con.commit()
        else:
            print("The choice you entered is not correct!")
    else:
        print("Something went wrong! Please make sure you entered your Username and Password correctly.")



play = True

while play == True:
    print(menu())
    choice = int(input("Enter your choice: "))
    if choice == 1:
        create_account() 
        print(menu)
    elif choice == 2:
        login()
        print(menu)
    elif choice == 3:
        close()
        print(menu)
    elif choice == 4:
        modify()
        print(menu)
    elif choice == 5:
        print("Thank you for visiting!")
        play = False
        exit

cur.close()
con.close()