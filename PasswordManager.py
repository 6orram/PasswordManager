# Starting--------------------------------------------------------------------------------------------------------------------------------

print(""" 
  --------------------------------------------------------------------
    ______                                                       
   /      \                                                      
  |  $$$$$$\  ______    ______    ______   ______   ______ ____  
  | $$___\$$ /      \  /      \  /      \ |      \ |      \    \ 
  | $$    \ |  $$$$$$\|  $$$$$$\|  $$$$$$\ \$$$$$$\| $$$$$$\$$$$\ 
  | $$$$$$$\| $$  | $$| $$   \$$| $$   \$$/      $$| $$ | $$ | $$
  | $$__/ $$| $$__/ $$| $$      | $$     |  $$$$$$$| $$ | $$ | $$
   \$$    $$ \$$    $$| $$      | $$      \$$    $$| $$ | $$ | $$
    \$$$$$$   \$$$$$$  \$$       \$$       \$$$$$$$ \$$  \$$  \$$

  ------------------------ Sweet Manager -----------------------------                                                                                                                                                                                        
""")
print("Don't forget to check My GitHub")
print("https://github.com/6orram")


# Importing Mosules and Librarys :  -------------------------------------------------------------------------------------------------------
from tkinter import messagebox
import mysql.connector
import customtkinter as ctk
from tkinter import *
from tkcalendar import Calendar
from datetime import date
from connectionObjects import *



connection = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    database=DATABASE
)
cmd = connection.cursor()

# Function : ------------------------------------------------------------------------------------------------------------------

def CtkMessageBox(message):
    # Create a new window for the message box
    messagebox_window = ctk.CTk()

    # Set the window title and size
    messagebox_window.title("Message")
    messagebox_window.geometry("300x150")

    # Create a label to display the message
    label = ctk.CTkLabel(messagebox_window, text=message)
    label.pack(pady=20)

    # Create an "OK" button to close the message box
    ok_button = ctk.CTkButton(messagebox_window, text="OK", command=messagebox_window.destroy)
    ok_button.pack()

    # Run the message box window
    messagebox_window.mainloop()
    
def Select():
    today = date.today()
    window.textbox4.delete(0, END)
    window.textbox4.insert(0, today)

def Save():
    try:
        username = window.textbox1.get()
        pwd = window.textbox2.get()
        website = window.textbox3.get()
        time = window.textbox4.get()

        # Insert the values into the materiel table
        requete = "insert into password(username,pwd,website,time) values (%s, %s, %s, %s);"
        values = (username, pwd, website, time)
        cmd.execute(requete, values)
        connection.commit()
        CtkMessageBox("Password Saved")
    except:
        CtkMessageBox("Error !")

def Delete():
    try:
        username = window.textbox1.get() 

        # Insert the values into the materiel table
        requete = "Delete from password where username = %s;"
        values = (username,)
        cmd.execute(requete, values)
        connection.commit()
        CtkMessageBox("Password Deleted")
    except:
        CtkMessageBox("Error !")

def Search():
    selected_value = window.optionmenu_1.get()
    if selected_value == "Tous":
        try:
            # Clear the existing text in the textbox_1
            window.text_1.delete("1.0", ctk.END)

            # Retrieve the values from the "materiel" table
            cmd.execute("SELECT username,pwd,website,time FROM password")
            result = cmd.fetchall()

            # Format and display the values in the textbox_1
            for row in result:
                username, password, website, time = row
                entry_text = f"{username}\t|\t{password}\t|\t{website}\n\n"
                window.text_1.insert(ctk.END, entry_text)

        except Exception as e:
            CtkMessageBox("Problem: " + str(e))
    elif selected_value == "Username":
        username = window.textbox5.get()
        try:
            # Clear the existing text in the textbox_1
            window.text_1.delete("1.0", ctk.END)

            # Retrieve the values from the "materiel" table
            values = (username,)
            cmd.execute("SELECT username,pwd,website,time FROM password where username = %s", values)

            result = cmd.fetchall()

            for row in result:
                username, password, website, time = row
                entry_text = f"{username}\t|\t{password}\t|\t{website}\n"
                window.text_1.insert(ctk.END, entry_text)

        except Exception as e:
            CtkMessageBox("Problem: " + str(e))
    elif selected_value == "Password":
        password = window.textbox5.get()
        try:
            # Clear the existing text in the textbox_1
            window.text_1.delete("1.0", ctk.END)

            # Retrieve the values from the "materiel" table
            values = (password,)
            cmd.execute("SELECT username,pwd,website,time FROM password where username = %s", values)

            result = cmd.fetchall()

            for row in result:
                username, password, website, time = row
                entry_text = f"{username}\t|\t{password}\t|\t{website}\t|\t{time}\n"
                window.text_1.insert(ctk.END, entry_text)

        except Exception as e:
            CtkMessageBox("Problem: " + str(e))
    elif selected_value == "Website":
        website = window.textbox5.get()
        try:
            # Clear the existing text in the textbox_1
            window.text_1.delete("1.0", ctk.END)

            # Retrieve the values from the "materiel" table
            values = (website,)
            cmd.execute("SELECT username,pwd,website,time FROM password where website = %s", values)

            result = cmd.fetchall()

            for row in result:
                username, password, website, time = row
                entry_text = f"{username}\t|\t{password}\t|\t{website}\n"
                window.text_1.insert(ctk.END, entry_text)

        except Exception as e:
            CtkMessageBox("Problem: " + str(e))



# GUI : ------------------------------------------------------------------------------------------------------------------


window = ctk.CTk()
window.title('Password Manager')
window.geometry('1000x900')
window.resizable(False, False)

frame1 = ctk.CTkFrame(master=window)
frame1.grid(row=0, column=0, sticky="nsew")
frame1.pack(pady=(20, 10), padx=20, fill="both")

window.label0 = ctk.CTkLabel(frame1, text="Enter Your Information", font=ctk.CTkFont(size=20, weight="bold"))
window.label0.grid(row=0, column=0, padx=10, pady=5)

window.label1 = ctk.CTkLabel(frame1, text="Username ")
window.label1.grid(row=1, column=0, padx=15, pady=5, sticky="w")
window.textbox1 = ctk.CTkEntry(frame1, placeholder_text="Enter your username", width=250)
window.textbox1.grid(row=1, column=1,sticky="w",padx=10, pady=(10, 10))

window.label2 = ctk.CTkLabel(frame1, text="Password ")
window.label2.grid(row=2, column=0, padx=15, pady=5, sticky="w")
window.textbox2 = ctk.CTkEntry(frame1, placeholder_text="Enter your Password", width=250)
window.textbox2.grid(row=2, column=1,sticky="w",padx=10, pady=(10, 10))

window.label3 = ctk.CTkLabel(frame1, text="Website ")
window.label3.grid(row=3, column=0, padx=15, pady=5, sticky="w")
window.textbox3 = ctk.CTkEntry(frame1, placeholder_text="Enter The Website", width=250)
window.textbox3.grid(row=3, column=1,sticky="w",padx=10, pady=(10, 10))

window.label4 = ctk.CTkLabel(frame1, text="Date")
window.label4.grid(row=4, column=0, padx=15, pady=5, sticky="w")
window.textbox4 = ctk.CTkEntry(frame1, placeholder_text="yy-mm-dd", width=150)
window.textbox4.grid(row=4, column=1, sticky="w", padx=10, pady=(10, 10))
select_button1 = ctk.CTkButton(frame1, text="Select", width=80, command=Select)
select_button1.grid(row=4, column=1, padx=80, pady=(10, 10), sticky="e")


select_button1 = ctk.CTkButton(frame1, text="Save", width=100, command=Save)
select_button1.grid(row=5, column=1, padx=10, pady=(20, 30), sticky="w")

select_button2 = ctk.CTkButton(frame1, text="Delete", width=100, command=Delete)
select_button2.grid(row=5, column=1, padx=120, pady=(20, 30), sticky="w")

frame2 = ctk.CTkFrame(master=window)
frame2.pack(pady=(20, 40), padx=20, fill="both", expand=True)


window.optionmenu_1 = ctk.CTkOptionMenu(frame2 ,values=["Username","Password","Website","Date","Tous"], width=100)
window.optionmenu_1.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="w")
window.optionmenu_1.set("Filtre")


window.textbox5 = ctk.CTkEntry(frame2, placeholder_text="Enter what you search", width=250)
window.textbox5.grid(row=0, column=0, padx=200, pady=(10, 10), sticky="w")


select_button4 = ctk.CTkButton(frame2, text="Search", width=100, command=Search)
select_button4.grid(row=0, column=0, padx=460, pady=(10, 10), sticky="w")


window.text_1 = ctk.CTkTextbox(frame2, width=910, height=400, font=("Arial", 25))
window.text_1.grid(row=1,column=0, padx=20,pady=20,sticky="w")






window.mainloop()
