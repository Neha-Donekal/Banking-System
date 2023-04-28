import tkinter as tk
import pymysql

root = tk.Tk()
con = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    password='Neha_41s',
    db='Bank Details',
    charset='utf8')

cur = con.cursor()

name_var=tk.StringVar()
username_var=tk.StringVar()
passw_var=tk.StringVar()
initialamt_var=tk.StringVar()
what_var = tk.StringVar()
to_what_var=tk.StringVar()
sure_var=tk.StringVar()
choice_var=tk.StringVar()

root.title("Banking System")
root.geometry("600x400")

def submit():
    choice = choice_var.get()
    print("The choice is : " + choice)
    choice_var.set("")

    if choice == "1":
        clear_frame()
        enter_info_for_create() 
        
        
    elif choice == "2": 
        clear_frame()      
        enter_info_for_login()     

    elif choice == "3":
        clear_frame()
        enter_info_for_close()
        

    elif choice == "4":
        clear_frame()
        enter_info_for_modify()
        

    elif choice == "5":
        clear_frame()
        exit()
        exit

def menu():
    menu1= tk.Label(root, text = "Your options are:")
    menu2= tk.Label(root, text = "1) Create a new account")
    menu3= tk.Label(root, text = "2) Login to account")
    menu4= tk.Label(root, text = "3) Close account")
    menu5= tk.Label(root, text = "4) Modify existing account")
    menu6= tk.Label(root, text = "5) Exit")
    choice_label = tk.Label(root, text = 'Enter your choice(in number):', font=('calibre',10, 'normal'))
    choice_entry = tk.Entry(root, textvariable = choice_var, font=('calibre',10,'normal'))
    sub_btn=tk.Button(root,text = 'Submit', command = submit)

    menu1.grid(sticky='w')
    menu2.grid(sticky='w')
    menu3.grid(sticky='w')
    menu4.grid(sticky='w')
    menu5.grid(sticky='w')
    menu6.grid(sticky='w')
    choice_label.grid()
    choice_entry.grid()
    sub_btn.grid()
    



def create_account():
 
    name=name_var.get()
    username = username_var.get()
    password=passw_var.get()
    balance = initialamt_var.get()
    print("The name is : " + name)
    print("The username is:" + username)
    print("The password is : " + password)
    print("The initial amount is: $" + balance)
     
    name_var.set("")
    username_var.set("")
    passw_var.set("")
    initialamt_var.set("")

    sql4 = "INSERT INTO Customer_Details (Name, Username, Password, Balance) VALUES(%s,%s,%s,%s)"
    val = (name, username, password, balance)
    cur.execute(sql4, val)
    con.commit()
    ret = tk.Label(root, text= "Account was successfully created!")
    ret.grid()
    clear_frame()
    menu()

def enter_info_for_create():
    label= tk.Label(root, text = "Creating a New Account- No Special characters")
    name_label = tk.Label(root, text = 'Name', font=('calibre',10, 'normal'))
    name_entry = tk.Entry(root, textvariable = name_var, font=('calibre',10,'normal'))
    username_label = tk.Label(root, text = 'Username', font=('calibre',10, 'normal'))
    username_entry=tk.Entry(root, textvariable = username_var, font = ('calibre',10,'normal'))
    passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'normal'))
    passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
    initialamt_label = tk.Label(root, text= 'Enter inital amount',font=('calibre',10, 'normal'))
    initialamt_entry=tk.Entry(root, textvariable = initialamt_var, font = ('calibre',10,'normal'))
    sub_btn=tk.Button(root,text = 'Submit', command = create_account)

    label.grid()
    name_label.grid()
    name_entry.grid()
    username_label.grid()
    username_entry.grid()
    passw_label.grid()
    passw_entry.grid()
    initialamt_label.grid()
    initialamt_entry.grid()

    sub_btn.grid()

def login():
    username = username_var.get()
    password=passw_var.get()
    print("The username is:" + username)
    print("The password is : " + password)
    username_var.set("")
    passw_var.set("")
    sql1 = 'SELECT * FROM Customer_Details'
    cur.execute(sql1)
    rows = cur.fetchall()
    result = any(username in tu for tu in rows)
    result1 = any(password in tu for tu in rows)
    con.commit()
    if result == True and result1 == True:
       ret= tk.Label(root, text='Login Successful!')
       ret.grid()
       clear_frame()
       menu()
    else:
        ret=tk.Label(root, text="Your username or password is wrong. Please try again!")
        ret.grid()
        clear_frame()
        menu()


def enter_info_for_login():
    label = tk.Label(root, text= "Logining In-")
    username_label = tk.Label(root, text = 'Username', font=('calibre',10, 'normal'))
    username_entry=tk.Entry(root, textvariable = username_var, font = ('calibre',10,'normal'))
    passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'normal'))
    passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')

    sub_btn=tk.Button(root,text = 'Submit', command = login)

    label.grid()
    username_label.grid()
    username_entry.grid()
    passw_label.grid()
    passw_entry.grid()
    sub_btn.grid()

def modify():
    username = username_var.get()
    password=passw_var.get()
    what = what_var.get().lower()
    to_what = to_what_var.get()
    print("The username is : " + username)
    print("The password is:" + password)
    print("The what is : " + what)
    print("The to what is:" + to_what)

    username_var.set("")
    passw_var.set("")
    what_var.set("")
    to_what_var.set("")

    sql1 = 'SELECT * FROM Customer_Details'
    cur.execute(sql1)
    rows = cur.fetchall()
    result = any(username in tu for tu in rows)
    result1 = any(password in tu for tu in rows)
    print(f"Result is: {result}, Result1 is: {result1}")
    con.commit()
    if result == True and result1 == True:
        new = to_what
        if what == 'name':
            command = 'UPDATE Customer_Details SET Name = %s WHERE Username = %s'
            val = (new, username)
            cur.execute(command, val)
            con.commit()
            ret = tk.Label(root, text="Name was modified")
            ret.grid()
            clear_frame()
            menu()
        if what == 'username':
            command = 'UPDATE Customer_Details SET Username = %s WHERE Username = %s'
            val = (new, username)
            cur.execute(command, val)
            con.commit()
            ret = tk.Label(root, text="Username was modified")
            ret.grid()
            clear_frame()
            menu()
        if what == 'password':
            command = 'UPDATE Customer_Details SET password = %s WHERE Username = %s'
            val = (new, username)
            cur.execute(command, val)
            con.commit()
            ret = tk.Label(root, text="Password was modified")
            ret.grid()
            clear_frame()
            menu()
        else:
            ret= tk.Label(root, text="The choice you entered is not correct!")
            ret.grid()
            clear_frame()
            menu()
    else:
        ret= tk.Label(root, text="Something went wrong! Please make sure you entered your Username and Password correctly.")
        ret.grid()
        clear_frame()
        menu()

def enter_info_for_modify():
    label = tk.Label(root, text= "Modifying Account-")
    username_label = tk.Label(root, text = 'Username', font=('calibre',10, 'normal'))
    username_entry=tk.Entry(root, textvariable = username_var, font = ('calibre',10,'normal'))
    passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'normal'))
    passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
    what_label = tk.Label(root, text = 'What would you like to modify in your account(name, username, or password)?', font=('calibre',10, 'normal'))
    what_entry=tk.Entry(root, textvariable = what_var, font = ('calibre',10,'normal'))
    to_what_label=tk.Label(root, text = 'What do you want to change it to?', font=('calibre',10, 'normal'))
    to_what_entry=tk.Entry(root, textvariable = to_what_var, font = ('calibre',10,'normal'))
    
    sub_btn=tk.Button(root,text = 'Submit', command = modify)
    
    label.grid()
    username_label.grid()
    username_entry.grid()
    passw_label.grid()
    passw_entry.grid()
    what_label.grid()
    what_entry.grid()
    to_what_label.grid()
    to_what_entry.grid()
    sub_btn.grid()


def close():
    sure = sure_var.get().lower()
    username = username_var.get()
    password=passw_var.get()
    print("The sure is : " + sure)
    print("The username is:" + username)
    print("The password is : " + password)
    sure_var.set("")
    username_var.set("")
    passw_var.set("")
    if sure == 'yes':
        sql3 = "delete from Customer_Details where username = %s and password = %s"
        val = (username, password)
        cur.execute(sql3, val)
        con.commit()
        ret = tk.Label(root, text="Account was successfully closed!")
        ret.grid()
        clear_frame()
        menu()
        
    elif sure == 'no':
        ret=tk.Label(root, text="You chose not to close your account!")
        ret.grid()
        clear_frame()
        menu()

def enter_info_for_close():
    label = tk.Label(root, text= "Closing Account-")
    sure_label=tk.Label(root, text="Are you sure you want to close your account?", font=('calibre',10, 'normal'))
    sure_entry=tk.Entry(root, textvariable = sure_var, font = ('calibre',10,'normal'))
    username_label = tk.Label(root, text = 'Username', font=('calibre',10, 'normal'))
    username_entry=tk.Entry(root, textvariable = username_var, font = ('calibre',10,'normal'))
    passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'normal'))
    passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
    
    sub_btn=tk.Button(root,text = 'Submit', command = close)

    label.grid()
    sure_label.grid()
    sure_entry.grid()
    username_label.grid()
    username_entry.grid()
    passw_label.grid()
    passw_entry.grid()
    
    sub_btn.grid()

def exit():
    last = tk.Label(root, text="Thank you for coming!")
    last.grid()
    clear_frame()
    exit

def clear_frame():
   for widgets in root.winfo_children():
      widgets.destroy()
      

print(menu())


root.mainloop()
cur.close()
con.close()