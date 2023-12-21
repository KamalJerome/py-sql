import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os


mydb = mysql.connector.connect(host="localhost",port="3306",user="root", passwd="omega11@kj",database="studentdb")
cursor = mydb.cursor()

def update(rows):
    trv.delete(*trv.get_children())
    for row in rows:
        trv.insert('', 'end', values=row)

#============================ 

def search():
    q2 = searchvar.get()

    if searchcol.get() == "Admn. No.":
        q3 = "admno"
    elif searchcol.get() == "Name":
        q3 = "name"
    elif searchcol.get() == "Class Sec.":
        q3 = "classec"
    elif searchcol.get() == "Mode Of Transport":
        q3 = "trpmode"
    elif searchcol.get() == "Email ID":
        q3 = "emailid"
    elif searchcol.get() == "Contact No.":
        q3 = "contactno"
    elif searchcol.get() == "Address":
        q3 = "address"

    query = "SELECT admno, name, classec, trpmode, emailid, contactno, address from studentdbms WHERE "+q3+" like '%"+q2+"%'"
    cursor.execute(query)
    rows= cursor.fetchall()
    update(rows)

#============================ 
    
def clear():
    query = "SELECT admno, name, classec, trpmode, emailid, contactno, address from studentdbms"
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)

#============================ 

def getrow(event):
    ent0.delete(0,END)
    ent1.delete(0,END)
    ent2.delete(0,END)
    ent3.delete(0,END)
    ent4.delete(0,END)
    ent5.delete(0,END)
    ent6.delete(0,END)
    ent7.delete(0,END)
    rowid = trv.identify_row(event.y)
    selected = trv.focus()
    values = trv.item(selected,'values')
    ent0.insert(0,values[0])
    ent1.insert(0,values[1])
    ent2.insert(0,values[2])
    ent3.insert(0,values[3])
    ent4.insert(0,values[4])
    ent5.insert(0,values[5])
    ent6.insert(0,values[6])
    ent7.insert(0,values[4])

#============================ 

def clear_sel():
    ent0.delete(0,END)
    ent1.delete(0,END)
    ent2.delete(0,END)
    ent3.delete(0,END)
    ent4.delete(0,END)
    ent5.delete(0,END)
    ent6.delete(0,END)
    ent7.delete(0,END)

#============================ 

def update_student():
    name = ent1.get()
    cls = ent2.get()
    mod = ent3.get()
    email = ent4.get()
    cont = ent5.get()
    addr = ent6.get()
    admn = ent0.get()

    mydb = mysql.connector.connect(host="localhost",port="3306",user="root", passwd="omega11@kj",database="studentdb")
    cursor = mydb.cursor()
    
    if messagebox.askyesno("Confirm Update","Are you sure you want to update this record?"):
        query = "UPDATE studentdbms SET name=%s, classec=%s, trpmode=%s, emailid=%s, contactno=%s, address=%s WHERE admno=%s"
        cursor.execute(query,(name,cls,mod,email,cont,addr,admn))
        mydb.commit()
        query2 = "SELECT admno, name, classec, trpmode, emailid, contactno, address from studentdbms"
        cursor.execute(query2)
        rows = cursor.fetchall()
        trv.delete(*trv.get_children())
        for row in rows:
            trv.insert('', 'end', values=row)
        ent0.delete(0,END)
        ent1.delete(0,END)
        ent2.delete(0,END)
        ent3.delete(0,END)
        ent4.delete(0,END)
        ent5.delete(0,END)
        ent6.delete(0,END)
        
    else:
        return True

#============================ 

def add_new():
    name = ent1.get()
    cls = ent2.get()
    mod = ent3.get()
    email = ent4.get()
    cont = ent5.get()
    addr = ent6.get()

    mydb = mysql.connector.connect(host="localhost",port="3306",user="root", passwd="omega11@kj",database="studentdb")
    cursor = mydb.cursor()
    
    if messagebox.askyesno("Confirm Insert","Are you sure you want to add this new record?"):
        query = "INSERT INTO studentdbms(name, classec, trpmode, emailid, contactno, address) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(query,(name,cls,mod,email,cont,addr))
        mydb.commit()
        query2 = "SELECT admno, name, classec, trpmode, emailid, contactno, address from studentdbms"
        cursor.execute(query2)
        rows = cursor.fetchall()
        trv.delete(*trv.get_children())
        for row in rows:
            trv.insert('', 'end', values=row)
        ent0.delete(0,END)
        ent1.delete(0,END)
        ent2.delete(0,END)
        ent3.delete(0,END)
        ent4.delete(0,END)
        ent5.delete(0,END)
        ent6.delete(0,END)
    else:
        return True   

#============================ 

def delete_student():
    adm = ent0.get()
    
    mydb = mysql.connector.connect(host="localhost",port="3306",user="root", passwd="omega11@kj",database="studentdb")
    cursor = mydb.cursor()

    if messagebox.askyesno("Confirm Delete","Are you sure you want to delete this record?"):
        query = "DELETE FROM studentdbms WHERE admno ="+adm
        cursor.execute(query)
        mydb.commit()
        query2 = "SELECT admno, name, classec, trpmode, emailid, contactno, address from studentdbms"
        cursor.execute(query2)
        rows = cursor.fetchall()
        trv.delete(*trv.get_children())
        for row in rows:
            trv.insert('', 'end', values=row)
        ent0.delete(0,END)
        ent1.delete(0,END)
        ent2.delete(0,END)
        ent3.delete(0,END)
        ent4.delete(0,END)
        ent5.delete(0,END)
        ent6.delete(0,END)
    else:
        return True

#============================ 

def openport():
    window = Toplevel(root)
    window.grab_set()
    window.geometry("800x500")
    portphoto = PhotoImage(file = 'portphoto.png')
    window.iconphoto(False, portphoto)
    window.title("AMPS Email Port")

    email_user = "etesting865@gmail.com"  
    email_password =  "865testing"

    id = Label(window, text="Email ID", font=("bold", 10))
    id.place(x=20, y=30)
    password = Label(window,text="Password",font=("bold", 10))
    password.place(x=20,y=60)
    emailsend = Label(window,text="Receiver Email ID",font=("bold", 10))
    emailsend.place(x=20,y=90)
    cc = Label(window,text="CC",font=("bold", 10))
    cc.place(x=20,y=120)
    subject = Label(window,text="Subject",font=("bold", 10))
    subject.place(x=20,y=150)
    body = Label(window,text="Body",font=("bold", 10))
    body.place(x=20,y=180)
    attachment = Label(window,text="Attachment",font=("bold", 10))
    attachment.place(x=20,y=420)
    emailinfo = Label(window,text="",font=("bold", 10), fg = "green")
    emailinfo.place(x=300,y=450)

    e_id = Text(window,height = 1, width = 50)
    e_id.insert('end-1c', email_user)
    e_id.place(x=150, y=30)
    e_password = Text(window,height = 1, width = 50)
    e_password.insert('end-1c', email_password)
    e_password.place(x=150, y=60)
    e_emailsend = Text(window,height = 1, width = 50)
    e_emailsend.insert('end-1c', ent7.get())
    e_emailsend.place(x=150, y=90)
    e_cc = Text(window,height = 1, width = 50)
    e_cc.place(x=150, y=120)
    e_subject = Text(window,height = 1, width = 50)
    e_subject.place(x=150, y=150)
    e_body = Text(window,height = 14)
    e_body.place(x=150, y=180)
    e_attachment= Text(window,height = 1, width = 50)
    e_attachment.place(x=150, y=420)


    def send():
        try:  
            email_send = e_emailsend.get("1.0",'end-1c')
            subject = e_subject.get("1.0",'end-1c')
            cc = e_cc.get("1.0",'end-1c')

            rcpt = cc.split(",")+[email_send]
            msg = MIMEMultipart()
            msg['From'] = email_user
            msg['To'] = email_send
            msg['Subject'] = subject
            msg['Cc'] = cc

            body = e_body.get("1.0",'end-1c')
            msg.attach(MIMEText(body,'plain'))

            fileName= e_attachment.get("1.0",'end-1c')

            if fileName != "":
                attachment = open(fileName,'rb')
                part = MIMEBase('application','octet-stream')
                part.set_payload((attachment).read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition',"attachment; filename= "+fileName)
                msg.attach(part)
                text = msg.as_string()
            else:
                text = msg.as_string()

            server = smtplib.SMTP('smtp.gmail.com',587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(email_user,email_password) 

            try:
                server.sendmail(email_user,rcpt,text)
            finally:
                emailinfo.config(text="Email sent Successfully", fg = "green")
                server.quit()

        except smtplib.SMTPException :
            emailinfo.config(text="Email failed", fg = "red")
            
    #============================ 

    def reset_port():
        e_id.delete('1.0',END)
        e_password.delete('1.0',END)
        e_emailsend.delete('1.0',END)
        e_subject.delete('1.0',END)
        e_body.delete('1.0',END)
        e_attachment.delete('1.0',END)
        e_cc.delete('1.0',END)
        emailinfo.config(text="")

    #============================

    def browsefile():
        directory = filedialog.askopenfilename(initialdir = "\\", title = "Select a File", filetypes = (("Text files","*.txt*"),("All files","*.*")))

        filenametext = directory

        e_attachment.insert('end-1c', filenametext)


    browse = Button(window, text="Browse", font=("italic", 10), bg="white", command=browsefile)
    browse.place(x=600, y=420)    
    send = Button(window, text="Send", font=("italic", 10), bg="white", command=send)
    send.place(x=20, y=450)
    reset = Button(window, text="Reset", font=("italic", 10), bg="white", command=reset_port)
    reset.place(x=100, y=450)

    
#==========================================================================

root = Tk()

#Variables----------------------------
t0 = StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()
t6 = StringVar()
mailid = StringVar()
searchvar = StringVar()
searchcol = StringVar()

#Wrappers and Treeview----------------
wrapper1 = LabelFrame(root, text="Student Details")
wrapper2 = LabelFrame(root, text="Search for Data")
wrapper3 = LabelFrame(root, text="Student Data")
wrapper4 = LabelFrame(root, text="Email Student")

wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper4.pack(fill="both", expand="yes", padx=20, pady=10) 

trv = ttk.Treeview(wrapper1, columns=(1,2,3,4,5,6,7), show="headings", height="10")
trv.pack()

#Headings-----------------------------
trv.heading(1, text="Admn. No.")
trv.heading(2, text="Name")
trv.heading(3, text="Class Sec.")
trv.heading(4, text="Mode of Transport")
trv.heading(5, text="Email ID")
trv.heading(6, text="Contact No.")
trv.heading(7, text="Address")

#Binding------------------------------
trv.bind('<Double-1>', getrow)

#Scrollbars---------------------------
hsb = ttk.Scrollbar(orient="horizontal")
hsb.configure(command=trv.xview)
trv.configure(xscrollcommand=hsb.set)
hsb.pack(fill=X,side = BOTTOM)

vsb = ttk.Scrollbar(orient="vertical")
vsb.configure(command=trv.yview)
trv.configure(yscrollcommand=vsb.set)
vsb.pack(fill=Y,side = RIGHT)

#Update-------------------------------
query = "SELECT admno, name, classec, trpmode, emailid, contactno, address from studentdbms"
cursor.execute(query)
rows = cursor.fetchall()
clear()
update(rows)

#Search Section-----------------------
lbll = Label(wrapper2, text="Column")
lbll.pack(side=tk.LEFT, padx=10)
colcb = ttk.Combobox(wrapper2, textvariable=searchcol)
colcb['values']=('Admn. No.', 'Name', 'Class Sec.', 'Mode Of Transport', 'Email ID', 'Contact No.', 'Address')
colcb.pack(side=tk.LEFT, padx=6)
lbl = Label(wrapper2, text="Search")
lbl.pack(side=tk.LEFT, padx=10)
ent = Entry(wrapper2, textvariable=searchvar)
ent.pack(side=tk.LEFT, padx=6)

btn = Button(wrapper2, text="Search", command=search)
btn.pack(side=tk.LEFT, padx=100)
cbtn = Button(wrapper2, text="Show All", command=clear)
cbtn.pack(side=tk.LEFT, padx=2)


#Student Data Section-----------------
lbl0 = Label(wrapper3, text="Admn. No.")
lbl0.grid(row=0, column=1, padx=5, pady=3)
ent0 = Entry(wrapper3, textvariable=t0)
ent0.grid(row=0, column=2, padx=5, pady=3)

lbl1 = Label(wrapper3, text="Name")
lbl1.grid(row=1, column=1, padx=5, pady=3)
ent1 = Entry(wrapper3, textvariable=t1)
ent1.grid(row=1, column=2, padx=5, pady=3)

lbl2 = Label(wrapper3, text="Class Sec.")
lbl2.grid(row=2, column=1, padx=5, pady=3)
ent2 = Entry(wrapper3, textvariable=t2)
ent2.grid(row=2, column=2, padx=5, pady=3)

lbl3 = Label(wrapper3, text="Mode Of Transport")
lbl3.grid(row=3, column=1, padx=5, pady=3)
ent3 = ttk.Combobox(wrapper3, textvariable=t3)
ent3['values']=('Cycle/Alone','Bus','Private Van','Parent Pickup')
ent3.grid(row=3, column=2, padx=5, pady=3)

lbl4 = Label(wrapper3, text="Email ID")
lbl4.grid(row=4, column=1, padx=5, pady=3)
ent4 = Entry(wrapper3, textvariable=t4)
ent4.grid(row=4, column=2, padx=5, pady=3)

lbl5 = Label(wrapper3, text="Contact No.")
lbl5.grid(row=5, column=1, padx=5, pady=3)
ent5 = Entry(wrapper3, textvariable=t5)
ent5.grid(row=5, column=2, padx=5, pady=3)

lbl6 = Label(wrapper3, text="Address")
lbl6.grid(row=6, column=1, padx=5, pady=3)
ent6 = Entry(wrapper3, textvariable=t6)
ent6.grid(row=6, column=2, padx=5, pady=3)

up_btn = Button(wrapper3, text="Update", command=update_student)
add_btn = Button(wrapper3, text="Insert New", command=add_new)
delete_btn = Button(wrapper3, text="Delete", command=delete_student)
selclear_btn = Button(wrapper3, text="Clear Data", command=clear_sel)

add_btn.grid(row=7, column=0, padx=5, pady=3)
up_btn.grid(row=7, column=1, padx=5, pady=3)
delete_btn.grid(row=7, column=2, padx=5, pady=3)
selclear_btn.grid(row=7, column=3, padx=5, pady=3)

#Email Student-----------------------
mlbl1 = Label(wrapper4, text="Student Email ID.")
mlbl1.grid(row=0, column=1, padx=5, pady=3)
ent7 = Entry(wrapper4, textvariable=mailid)
ent7.grid(row=0, column=2, padx=5, pady=3)

mail_btn = Button(wrapper4, text="Open Email Port", command=openport)
mail_btn.grid(row=0, column=6, padx=5, pady=3)

#Root Window-------------------------
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
root.title("Student Database")
root.geometry("%dx%d" % (width, height))
photo = PhotoImage(file = 'dbnobg.png')
root.iconphoto(False, photo)
root.mainloop()