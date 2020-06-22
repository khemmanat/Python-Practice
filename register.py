from tkinter import * 
import sqlite3

root = Tk()
root.title("Registration")
root.iconbitmap("C:/Python/My Project/images/icon/web.ico")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

def center(win):
    """
    centers a tkinter window
    :param win: the root or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


#Databases

# Create a database or connect to one
conn = sqlite3.connect('registration.db')

#Create cursor
c = conn.cursor()

#Create table (database)
'''
c.execute("""CREATE TABLE info (
    first_name text, 
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer ,
    telephone_no text,
    age integer,
    date_of_birth date,
    job text
    )""")
    '''

#Create Function to Delete A Record
def delete():
    # Create a database or connect to one
    conn = sqlite3.connect('registration.db')

    #Create cursor
    c = conn.cursor()

    #Delete
    c.execute("DELETE FROM info WHERE oid= "+ delete_box.get())

    delete_box.delete(0,END)
    #Commit Changes
    conn.commit()

    #Class connection
    conn.close()

#Create Submit Function For Database
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('registration.db')

    #Create cursor
    c = conn.cursor()

    #Insert Into Table
    c.execute("INSERT INTO info VALUES (:f_name, :l_name, :address, :city, :state, :zipcode, :tel_no, :age, :dob, :job)",
        {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'address': address.get(),
            'city': city.get(),
            'state': state.get(),
            'zipcode': zipcode.get(),
            'tel_no': tel_no.get(),
            'age' : age.get(),
            'dob': dob.get(),
            'job': job.get()
        })
    
    #Commit Changes
    conn.commit()

    #Class connection
    conn.close()

    #Clear The Text Boxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)
    tel_no.delete(0,END)
    age.delete(0,END)
    dob.delete(0,END)
    job.delete(0,END)


#Create Query function
def query():
    # Create a database or connect to one
    conn = sqlite3.connect('registration.db')

    #Create cursor
    c = conn.cursor()

    # Query the database
    c.execute("SELECT *, oid FROM info")
    records = c.fetchall()
    print(records)
    #Loop through results
    print_records = ''
    for record in records:
        print_records += "Name: "+ str(record[0]) + " "+ str(record[1])+ "  Address: " +"\t" + str(record[2])+" "+ str(record[3])+" "+ str(record[4])+" "+ str(record[5])+"  Telephone No.: "+ str(record[6])+"  Age: "+ str(record[7])+"  Date of Birth: "+ str(record[8])+"  Job: "+ str(record[9])+"\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=14,column=0, columnspan=2)

    #Commit Changes
    conn.commit()

    #Class connection
    conn.close()


#Create Text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0 ,column=1, padx =20, pady=(10,0))

l_name = Entry(root, width=30)
l_name.grid(row=1 ,column=1 )

address = Entry(root, width=30)
address.grid(row=2 ,column=1)

city = Entry(root, width=30)
city.grid(row=3 ,column=1)

state = Entry(root, width=30)
state.grid(row=4 ,column=1 )

zipcode = Entry(root, width=30)
zipcode.grid(row=5 ,column=1 )

tel_no = Entry(root, width=30)
tel_no.grid(row=6 ,column=1 )

age = Entry(root, width=30)
age.grid(row=7 ,column=1 )

dob = Entry(root, width=30)
dob.grid(row=8 ,column=1 )

job = Entry(root, width=30)
job.grid(row=9 ,column=1 )

delete_box = Entry(root, width=30)
delete_box.grid(row=12, column=1, pady=5)



#Create text box labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10,0))

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

tel_no_label = Label(root, text="Telephone No")
tel_no_label.grid(row=6, column=0)

age_label = Label(root, text="Age")
age_label.grid(row=7, column=0)

dob_label = Label(root, text="Date of Birth")
dob_label.grid(row=8, column=0)

job_label = Label(root, text="Job")
job_label.grid(row=9, column=0)

delete_box_label = Label(root, text="Delete ID")
delete_box_label.grid(row=12, column=0, pady=5)


#Create Submit Button
submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=10,column=0, columnspan=2, pady=10, padx= 10, ipadx=100)

#Create a Query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=11,column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#Create a delete button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=13,column=0, columnspan=2, pady=10, padx=10, ipadx=136)


#Commit Changes
conn.commit()

#Class connection
conn.close()

center(root)



root.mainloop()