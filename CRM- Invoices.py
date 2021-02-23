from tkinter import *
from tkinter import ttk 
import sqlite3

###Tkinter configuration
root = Tk()
root.configure(background ='#DADADE')
root.title("CRM")
root.geometry("500x500")

#Password
set_password = "pass123"

###Table
conection = sqlite3.connect("Customer's_data.db")
cursor = conection.cursor()

'''
cursor.execute("""CREATE TABLE customer(
                customer_name text,
                street text,
                city text,
                ZIP text,
                state text,
                contract text,
                invoice_number text,
                invoice_amount text,
                invoice_date text,
                added_by text
                )""")
'''

cursor.execute("SELECT *, oid FROM customer")
records = cursor.fetchall()
print_records = []

# List of customers for Combobox
for record in records:
    print_records += (str(record[0])).lower() + (" : ") + (str(record[10])),
print_records = sorted(print_records)

#Global variables
cust_id = None
contract_t = None
inv_num_t = None
inv_amt_t = None
inv_date_t = None
cust_n = None
submitted_passw = None
pass_con = None
password = None
passwordII = None
pass_con_II = None
cust_n_l = None
c_strt = None
cus_c = None
zp = None
cust_s = None

###Functions
#Upload only int from list
def get_numbers(list):
    our_number = ""
    numbers = str([0,1,2,3,4,5,6,7,8,9])
 
    for i in list:
        if i in numbers:
            our_number +=i
      
    return our_number
    print(our_number)

#Submit button
def submit():
   
    connection = sqlite3.connect("Customer's_data.db")
    cursor = connection.cursor()
  
    cursor.execute ("Insert into customer VALUES(:customer_name, :street, :city, :ZIP, :state, :contract, :invoice_number, :invoice_amount, :invoice_date, :added_by )",
                    {
                     "customer_name": customer_name.get(),
                     "street": street.get(),
                     "city": city.get(),
                     "ZIP": zip_code.get(),
                     "state": state.get(),
                     
                     "contract": contract.get(),
                     "invoice_number": inv_num.get(),
                     "invoice_amount": inv_amt.get(),
                     "invoice_date": inv_date.get(),
                     "added_by": added_by.get(),                 
                    })

    connection.commit()
    connection.close()
    
    customer_name.delete(0,END)
    street.delete(0,END)
    city.delete(0,END)
    zip_code.delete(0,END)
    state.delete(0,END)
    contract.delete(0,END)
    inv_num.delete(0,END)
    inv_date.delete(0,END)

#Prin all customers
def printing_customers():

    customer_data = Tk()
    customer_data.configure(background ='#DADADE')
    customer_data.title("List of customers")
    customer_data.geometry("900x680")
    
    connection = sqlite3.connect("Customer's_data.db")
    cursor = connection.cursor()
    cursor.execute("SELECT *, oid FROM customer")

    records = cursor.fetchall()
    cus_id = ""
    cust_nm = ""
    strt = "" 
    ct = ""
    zp = ""
    st = ""
    addb = ""
   
    for record in records:
        cus_id +=  str(record[10])+"\n" 
        cust_nm += str(record[0])+"\n" 
        strt += str(record[1])+"\n"  
        ct += str(record[2])+"\n" 
        zp += str(record[3])+"\n" 
        st += str(record[4])+"\n" 
        addb += str(record[9])+"\n"

    #Header
    cus_id_tab_label = Label(customer_data, fg = "white", bg = "#144072", width = 12, text = "Customer ID")
    cus_id_tab_label.grid(row = 0, column = 0)

    cust_nm_lab = Label(customer_data, fg = "white", bg = "#144072", width = 22, text = "Customer name")
    cust_nm_lab.grid(row = 0, column = 1)

    strt_lab = Label(customer_data, fg = "white", bg = "#144072", width = 24, text = "Street")
    strt_lab.grid(row = 0, column = 2)

    ct_lab = Label(customer_data, fg = "white", bg = "#144072", width = 17, text = "City")
    ct_lab.grid(row = 0, column = 3)

    zp_lab = Label(customer_data, fg = "white", bg = "#144072", width = 9, text = "ZIP")
    zp_lab.grid(row = 0, column = 4)

    st_lab = Label(customer_data, fg = "white", bg = "#144072", width = 18, text = "State")
    st_lab.grid(row = 0, column = 5)

    processor_lab = Label(customer_data, fg = "white", bg = "#144072", width = 18, text = "Added by")
    processor_lab.grid(row = 0, column = 6)
   
    #scrollbar
    scrollbar_inv = Scrollbar(customer_data)
    scrollbar_inv.grid(row = 0, column = 7, ipady = 309, rowspan = 2)

    #Table
    #ID
    id_tab = Text(customer_data, bg = "#DADADE", width = 10, height = 40, yscrollcommand = scrollbar_inv.set)
    id_tab.grid(row = 1, column = 0)
    id_tab.insert(END, cus_id)
    id_tab.configure(state='disabled', wrap='none')

    #Cust name
    cust_nm_tab = Text(customer_data, bg = "#DADADE", width = 19, height = 40, yscrollcommand = scrollbar_inv.set )
    cust_nm_tab.grid(row = 1, column = 1)
    cust_nm_tab.insert(END, cust_nm)
    cust_nm_tab.configure(state='disabled', wrap='none')

    #Street      
    strt_tab = Text(customer_data, bg = "#DADADE", width = 21, height = 40, yscrollcommand = scrollbar_inv.set)
    strt_tab.grid(row = 1, column = 2)
    strt_tab.insert(END, strt)
    strt_tab.configure(state='disabled', wrap='none')

    #City
    ct_tab = Text(customer_data, bg = "#DADADE", width = 15, height = 40, yscrollcommand = scrollbar_inv.set)
    ct_tab.grid(row = 1, column = 3)
    ct_tab.insert(END, ct)
    ct_tab.configure(state='disabled', wrap='none')

    #Zip
    zp_tab = Text(customer_data, bg = "#DADADE", width = 8, height = 40, yscrollcommand = scrollbar_inv.set)
    zp_tab.grid(row = 1, column = 4)
    zp_tab.insert(END, zp)
    zp_tab.configure(state='disabled', wrap='none')
   
    #state
    st_tab = Text(customer_data, bg = "#DADADE", width = 16, height = 40, yscrollcommand = scrollbar_inv.set)
    st_tab.grid(row = 1, column = 5)
    st_tab.insert(END, st)
    st_tab.configure(state='disabled', wrap='none')

    #added by
    processor = Text(customer_data, bg = "#DADADE", width = 16, height = 40, yscrollcommand = scrollbar_inv.set)
    processor.grid(row = 1, column = 6)
    processor.insert(END, addb)
    processor.configure(state='disabled', wrap='none')

    #Function to scroll all rows
    def yview(*args):
        cus_id.yview(*args)
        cust_nm.yview(*args)
        strt.yview(*args)
        ct.yview(*args)
        zp.yview(*args)
        st.yview(*args)
        processor.yview(*args)

    scrollbar_inv.config( command = yview )

# Print all customer's Invoices
def  print_invoices():

    #New window for Invoice data 
    invoices = Tk()
    invoices.configure(background ='#DADADE' )
    width= invoices.winfo_screenwidth()  
    height= invoices.winfo_screenheight()
    invoices.geometry("475x700")
    spec_cust = customers.get()
    invoices.title("Invoices: "+ spec_cust ) 

    #Getting Invoice data from the database
    connection = sqlite3.connect("Customer's_data.db")
    cursor = connection.cursor()
      
    cursor.execute("SELECT *, oid FROM customer WHERE oid = " + cust_id)
    records = cursor.fetchall()
    contr = ""
    inv_n = ""
    inv_a = "" 
    inv_d = ""
   
    for record in records:
        contr += str(record[5]) 
        inv_n += str(record[6]) 
        inv_a += str(record[7]) 
        inv_d += str(record[8]) 
    
    #Header
    contr_tab_label = Label(invoices, fg = "white", bg = "#144072", width = 16, text = "Contract #")
    contr_tab_label.grid(row = 0, column = 0)

    inv_n_tab_lab = Label(invoices, fg = "white", bg = "#144072", width = 16, text = "Invoice #")
    inv_n_tab_lab.grid(row = 0, column = 1)

    inv_a_tab_lab = Label(invoices, fg = "white", bg = "#144072", width = 16, text = "Invoice amount")
    inv_a_tab_lab.grid(row = 0, column = 2)

    inv_d_tab_lab = Label(invoices, fg = "white", bg = "#144072", width = 14, text = "Invoice date")
    inv_d_tab_lab.grid(row = 0, column = 3)

    #scrollbar
    scrollbar_inv = Scrollbar(invoices)
    scrollbar_inv.grid(row = 0, column = 4, ipady = 309, rowspan = 2)

    #Table
    #Contract
    contr_tab = Text(invoices, bg = "#DADADE", width = 14, height = 40, yscrollcommand = scrollbar_inv.set)
    contr_tab.grid(row = 1, column = 0)
    contr_tab.insert(END, contr)
    contr_tab.configure(state='disabled', wrap='none')

    #Inv number
    inv_n_tab = Text(invoices, bg = "#DADADE", width = 14, height = 40, yscrollcommand = scrollbar_inv.set )
    inv_n_tab.grid(row = 1, column = 1)
    inv_n_tab.insert(END, inv_n)
    inv_n_tab.configure(state='disabled', wrap='none')

    #Invoice amount        
    inv_a_tab = Text(invoices, bg = "#DADADE", width = 14, height = 40, yscrollcommand = scrollbar_inv.set)
    inv_a_tab.grid(row = 1, column = 2)
    inv_a_tab.insert(END, inv_a)
    inv_a_tab.configure(state='disabled', wrap='none')

    #Inv date
    inv_d_tab = Text(invoices, bg = "#DADADE", width = 12, height = 40, yscrollcommand = scrollbar_inv.set)
    inv_d_tab.grid(row = 1, column = 3)
    inv_d_tab.insert(END, inv_d)
    inv_d_tab.configure(state='disabled', wrap='none')

    #Function to scroll all rows
    def yview(*args):
        contr_tab.yview(*args)
        inv_n_tab.yview(*args)
        inv_a_tab.yview(*args)
        inv_d_tab.yview(*args)

    scrollbar_inv.config( command = yview )

# Submit Invoice data
def submit_inv():
    connection = sqlite3.connect("Customer's_data.db")
    cursor = connection.cursor()

    cursor.execute("SELECT *, oid FROM customer WHERE oid = " + cust_id)
    records_i = cursor.fetchall()
    cust_cont = ""
    cust_inv_n = ""
    cust_inv_a = ""
    cust_inv_d = ""

    for record in records_i:
        cust_cont += str(record[5])
        cust_inv_n += str(record[6])
        cust_inv_a += str(record[7]) 
        cust_inv_d += str(record[8])

    connection = sqlite3.connect("Customer's_data.db")
    cursor = connection.cursor()
    contract = contract_t.get()
    invoice_number = inv_num_t.get()
    invoice_amount = inv_amt_t.get()
    invoice_date = inv_date_t.get()
     
    cursor.execute ("""UPDATE customer SET
                     contract = :contract,
                     invoice_number = :invoice_number,
                     invoice_amount = :invoice_amount,
                     invoice_date = :invoice_date   
                     WHERE oid = """ + cust_id,
                     {"contract" : cust_cont + "\n" + contract, 
                      "invoice_number" : cust_inv_n + "\n" + invoice_number,
                      "invoice_amount" : cust_inv_a + "\n" + invoice_amount,
                      "invoice_date" : cust_inv_d + "\n" + invoice_date,
                      "oid" : cust_id}
                     )

    connection.commit()
    connection.close()

    contract_t.delete(0,END)
    inv_num_t.delete(0,END)
    inv_amt_t.delete(0,END)
    inv_date_t.delete(0,END)

# Update cust. data
def sub_pa_chngs():
    submitted_passw_II = pass_con_II.get()

    connection = sqlite3.connect("Customer's_data.db")
    cursor = connection.cursor()

    cursor.execute("SELECT *, oid FROM customer WHERE oid = " + cust_id)

    connection = sqlite3.connect("Customer's_data.db")
    cursor = connection.cursor()

    customer_name = cust_n_l.get()
    street = c_strt.get()
    city = cus_c.get()
    ZIP = zp.get()
    state = cust_s.get()

    if submitted_passw_II == set_password:
            cursor.execute ("""UPDATE customer SET
                        customer_name = :customer_name,
                        street = :street,
                        city = :city,
                        ZIP = :ZIP,
                        state = :state                        
                        WHERE oid = """ + cust_id,
                        {"customer_name" : customer_name,
                        "street" : street,
                        "city" : city,
                        "ZIP" : ZIP,
                        "state" : state,
                        "oid" : cust_id}
                        )
            passwordII.destroy()
    else:
        pass_con_l = Label(passwordII, bg = "#DADADE", text = "Incorect password!!!")
        pass_con_l.grid(row = 1, column = 0, columnspan = 2, padx = 3)
        
    connection.commit()
    connection.close()

def submit_data():
    global passwordII
    global pass_con_II

    passwordII = Tk()
    passwordII.configure(background ='#DADADE')
    passwordII.geometry("300x100")
    passwordII.title("Enter Password:")

    pass_con_l = Label(passwordII, bg = "#DADADE", text = "Enter password:")
    pass_con_l.grid(row = 0, column = 0, padx = 3)

    pass_con_II = Entry(passwordII, show="*")
    pass_con_II.grid(row = 0, column = 1)
    
    sub_button = Button(passwordII, fg = "white", bg = "#144072", text = " Submit", command = sub_pa_chngs)
    sub_button.grid(row = 0, column = 3, )

#Customer's Invoice tool
def  invoice_tool():
    
    #Global variables
    global cust_id
    global contract_t
    global inv_num_t
    global inv_amt_t
    global inv_date_t
    global cust_n_l
    global c_strt
    global cus_c
    global zp
    global cust_s

    #New window for invoice tool
    inv_tool = Tk()
    inv_tool.configure(background ='#DADADE')
    inv_tool.geometry("500x580")
    spec_cust = customers.get()
    inv_tool.title(spec_cust)

    #Getting customer's data from the database
    connection = sqlite3.connect("Customer's_data.db")
    cursor = connection.cursor()
        
    cust_id = get_numbers(spec_cust)
      
    cursor.execute("SELECT *, oid FROM customer WHERE oid = " + cust_id)
    records = cursor.fetchall()
    cust_name = ""
    strt = ""
    cust_city = ""
    c_zip = ""
    stat = ""
    add_b = ""
    cus_id = ""

    for record in records:
        cust_name += str(record[0])
        strt += str(record[1])
        cust_city += str(record[2])   
        c_zip += str(record[3])
        stat += str(record[4]) 
        add_b += str(record[9])
        cus_id += str(record[10])
    
    #wdigets in customer's Invoice tool
    #Header- Invoice data
    header_tool_label = Label(inv_tool, fg = "white", bg = "#144072", text = cust_name)
    header_tool_label.grid(row = 0, column = 0, columnspan = 2, pady = 10, ipadx = 180, ipady = 8)

    #Contract number
    contract_t_label = Label(inv_tool, bg = "#DADADE", text = "Contract#")
    contract_t_label.grid(row = 1, column = 0, padx = 2, pady = 5)

    contract_t = Entry(inv_tool)
    contract_t.grid(row = 1, column = 1, padx = 2, pady = 5)

    #Inv number
    inv_num_t_label = Label(inv_tool, bg = "#DADADE", text = "Invoice number")
    inv_num_t_label.grid(row = 2, column = 0, padx = 2, pady = 5)

    inv_num_t = Entry(inv_tool)
    inv_num_t.grid(row = 2, column = 1, padx = 2, pady = 5)

    #Inv amount
    inv_amt_t_label  = Label(inv_tool, bg = "#DADADE", text = "Invoice amount")
    inv_amt_t_label .grid(row = 3, column = 0, padx = 2, pady = 5)

    inv_amt_t = Entry(inv_tool)
    inv_amt_t.grid(row = 3, column = 1, padx = 1, pady = 5)

    #Inv date
    inv_date_label_t  = Label(inv_tool, bg = "#DADADE", text = "Invoice date")
    inv_date_label_t.grid(row = 4, column = 0, padx = 2, pady = 5)

    inv_date_t = Entry(inv_tool)
    inv_date_t.grid(row = 4, column = 1, padx = 2, pady = 5)

    #Submit Invoice
    invoice_button = Button(inv_tool, fg = "white", bg = "#144072", text = " Add invoice", command = submit_inv)
    invoice_button.grid(row = 5, column = 1, padx = 2, pady = 5, ipadx = 15)

    #Show all customers Inv
    show_button= Button(inv_tool, fg = "white", bg = "#556577", text = " Show all customer's invoices", command = print_invoices)
    show_button.grid(row = 6, column = 0, padx = 5, pady = 9)

    #Header- Customer data
    header_cust_label = Label(inv_tool, fg = "white", bg = "#144072", text = "Customer data")
    header_cust_label.grid(row = 7, column = 0, columnspan = 2, padx = 5, pady = 10, ipadx = 168, ipady = 8)

    #Customer ID
    c_id_l = Label(inv_tool, bg = "#DADADE", anchor = "e", text = "Customer ID :")
    c_id_l.grid(row = 8, column = 0, ipadx = 38, pady = 5)

    c_id = Label(inv_tool, bg = "#DADADE",  text = cus_id)
    c_id.grid(row = 8, column = 1, sticky = W)

    #Customer name
    cust_n = Label(inv_tool, bg = "#DADADE", anchor = "e",  text = "Customer name :")
    cust_n.grid(row = 9, column = 0, ipadx = 30, pady = 5)

    cust_n_l = Entry(inv_tool, bg = "#DADADE", bd = 0 )
    cust_n_l.grid(row = 9, column = 1, sticky = W)
    cust_n_l.insert(0, cust_name)
       
    #Street
    c_strt_l = Label(inv_tool, bg = "#DADADE", anchor = "e", text = "Street :")
    c_strt_l.grid(row = 10, column = 0, ipadx = 59, pady = 5)

    c_strt = Entry(inv_tool, bg = "#DADADE", bd = 0)
    c_strt.grid(row = 10, column = 1, sticky = W)
    c_strt.insert(0, strt)
  
    #City
    cus_c_l = Label(inv_tool, bg = "#DADADE", anchor = "e", text = "City :")
    cus_c_l.grid(row = 11, column = 0, ipadx = 63, pady = 5)

    cus_c = Entry(inv_tool, bg = "#DADADE", bd = 0)
    cus_c.grid(row = 11, column = 1, sticky = W)
    cus_c.insert(0, cust_city)
   
    #ZIP
    zp_l = Label(inv_tool, bg = "#DADADE", anchor = "e", text = "ZIP :")
    zp_l.grid(row = 12, column = 0, ipadx = 66, pady = 5)

    zp = Entry(inv_tool, bg = "#DADADE", text = c_zip, bd = 0)
    zp.grid(row = 12, column = 1, sticky = W)
    zp.insert(0, c_zip)
  
    #State
    cust_s_l = Label(inv_tool, bg = "#DADADE", anchor = "e", text = "State :")
    cust_s_l.grid(row = 13, column = 0, ipadx = 62, pady = 5)

    cust_s = Entry(inv_tool, bg = "#DADADE", bd = 0 )
    cust_s.grid(row = 13, column = 1, sticky = W)
    cust_s.insert(0, stat)
   
    #Added by
    a_b_l = Label(inv_tool, bg = "#DADADE", anchor = "e", text = "Added by :")
    a_b_l.grid(row = 14, column = 0, ipadx = 51, pady = 5)

    a_b = Label(inv_tool, bg = "#DADADE", text = add_b)
    a_b.grid(row = 14, column = 1, sticky = W)
   
   #Submitt changes for customer data
    change_button= Button(inv_tool, fg = "white", bg = "#556577", text = " Submit changes", command = submit_data)
    change_button.grid(row = 15, column = 0, padx = 5, pady = 9) 

    connection.commit()
    connection.close()

#Submit the password
def sub_pass():

    submitted_passw = pass_con.get()
    
    connection = sqlite3.connect("Customer's_data.db")
    cursor = connection.cursor()
    spec_cust = customers.get()
    cust_id = get_numbers(spec_cust)

    if submitted_passw == set_password:
        cursor.execute("DELETE from customer WHERE oid = " +  cust_id)
        password.destroy()
    else:
        pass_con_l = Label(password, bg = "#DADADE", text = "Incorect password!!!")
        pass_con_l.grid(row = 1, column = 0, columnspan = 2, padx = 3)

    connection.commit()
    connection.close()

#Delete function
def delete():
    global pass_con
    global password
   
    password = Tk()
    password.configure(background ='#DADADE')
    password.geometry("300x100")
    password.title("Enter Password:")

    pass_con_l = Label(password, bg = "#DADADE", text = "Enter password:")
    pass_con_l.grid(row = 0, column = 0, padx = 3)

    pass_con = Entry(password, show="*")
    pass_con.grid(row = 0, column = 1)
    
    sub_button = Button(password, fg = "white", bg = "#144072", text = " Submit", command = sub_pass)
    sub_button.grid(row = 0, column = 3, )
      

### Main screen widgets 

#Header new customer
header1_label = Label(root, fg = "white", bg = "#144072", text = "New customer")
header1_label.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 10, ipadx = 190, ipady = 8)

#Name
customer_name_label = Label(root, bg = "#DADADE", text = "Customer name")
customer_name_label.grid(row = 1, column = 0, padx = 2, pady = 5 )

customer_name = Entry(root)
customer_name.grid(row = 1, column = 1, padx = 2, pady = 5)

#Street
street_label = Label(root, bg = "#DADADE", text = "Street")
street_label.grid(row = 2, column = 0, padx = 2, pady = 5)

street = Entry(root)
street.grid(row = 2, column = 1, padx = 2, pady = 5)

#City
city_label = Label(root, bg = "#DADADE", text = "City")
city_label.grid(row = 3, column = 0, padx = 2, pady = 5)

city = Entry(root)
city.grid(row = 3, column = 1)

#Zip code
zip_code_label = Label(root, bg = "#DADADE", text = "Zip code")
zip_code_label .grid(row = 4, column = 0, padx = 2, pady = 5)

zip_code = Entry(root)
zip_code.grid(row = 4, column = 1, padx = 2, pady = 5)

#State
state_label  = Label(root, bg = "#DADADE", text = "State, Country")
state_label.grid(row = 5, column = 0, padx = 2, pady = 5)

state = Entry(root)
state.grid(row = 5, column = 1, padx = 2, pady = 5)

#Added by
added_by_label = Label(root, bg = "#DADADE", text = "added by")
added_by_label.grid(row = 6, column = 0, padx = 2, pady = 5)

employees = ["Peter Parker",
            "John Wayne", 
            "Henry Smith",
            "Peter Black",
            "Bruce Banner",
            "Clark Wayne",
            "Bruce Kent",
            "Tony Stark"]

added_by = ttk.Combobox(root, value= employees, height = 5)
added_by.grid(row = 6, column = 1, padx = 2, pady = 5)
added_by.bind("<<<Combo Selected>>>")
added_by.current(0)
added_by.get()

#Contract
contract_label = Label(root, bg = "#DADADE", text = "Contract#")
contract_label.grid(row = 1, column = 2, padx = 2, pady = 5)

contract = Entry(root)
contract.grid(row = 1, column = 3, padx = 2, pady = 5)

#Inv
inv_num_label = Label(root, bg = "#DADADE", text = "Invoice number")
inv_num_label.grid(row = 2, column = 2, padx = 2, pady = 5)

inv_num = Entry(root)
inv_num.grid(row = 2, column = 3, padx = 2, pady = 5)

#Inv amount
inv_amt_label  = Label(root, bg = "#DADADE", text = "Invoice amount")
inv_amt_label .grid(row = 3, column = 2, padx = 2, pady = 5)

inv_amt = Entry(root)
inv_amt.grid(row = 3, column = 3, padx = 2, pady = 5)

#Inv date
inv_date_label  = Label(root, bg = "#DADADE", text = "Invoice date")
inv_date_label .grid(row = 4, column = 2, padx = 2, pady = 5)

inv_date = Entry(root)
inv_date.grid(row = 4, column = 3, padx = 2, pady = 5)

#Submit button
submit_button = Button(root, fg = "white", bg = "#144072", text = "Submit", command = submit) 
submit_button.grid(row =6, column = 3, ipadx = 32, pady = 15)

#Header Customer detail
header1_label = Label(root, fg = "white", bg = "#144072", text = "Customer detail")
header1_label.grid(row = 7, column = 0, columnspan = 4, pady = 10, ipadx = 185, ipady = 8)

#List of customers
customers_label = Label(root, bg = "#DADADE", text = "Customer")
customers_label.grid(row = 8, column = 0, padx = 2, pady = 5)

customers = ttk.Combobox(root, values = print_records, height = 8)
customers.grid(row = 8, column = 1, columnspan = 2, ipadx = 12, pady = 5)
customers.bind("<<<Combo Selected>>>")

#Invoices button
invoice_button = Button(root, fg = "white", bg = "#144072", text = "Invoice tool", command = invoice_tool)
invoice_button.grid(row = 9, column = 3, padx = 2, pady = 5, ipadx = 15)

#Show all customers
show_button= Button(root, fg = "white", bg = "#556577", text = " Show all customers", command = printing_customers)
show_button.grid(row = 10, column = 1, padx = 2, pady = 9)

#Delete button
delete_button = Button(root, fg = "white", bg = "#556577", text = " Delete record", command = delete)
delete_button.grid(row = 10, column = 0, padx = 2, pady = 9)

conection.commit()
conection.close()

root.mainloop()
