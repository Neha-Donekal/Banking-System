print("Hello, thank you for choosing our bank.")


menu = int(input("""Your options are:
    1) Create a new account
    2) Login to account 
    3) Close account
    4) Modify existing account
    Enter your choice:  """)) 

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