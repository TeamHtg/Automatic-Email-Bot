import smtplib                               #smtp:- Simple Mail Transfer Protocol
from email.message import EmailMessage
from tkinter import*
#-----------------------------------------------------Backend-----------------------------------------------------

def send_email(to,subject,body,attachment,extension,fr,password):
    server= smtplib.SMTP('smtp.gmail.com',587)   #587 :- Port Number
    server.starttls()                            #tls:- Transfer Layer Security:- It tells tha person you are not fraud
    server.login(fr,password)
    email=EmailMessage()
    email['From']=fr
    email['To']=to
    email['Subject']=subject
    email.set_content(body)
    with open(attachment,"rb") as f:
        file_data=f.read()
        file_name=f.name
        email.add_attachment(file_data,maintype="application",subtype=extension,filename=file_name)
    server.send_message(email)
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------Frontend-----------------------------------------------------
root = Tk()
root.geometry('500x600')
root.title("My Mail-EmailBot")
def getint():
    to=entry_2.get()
    subject=entry_3.get()
    body=entry_4.get()
    attachment=entry_5.get()
    extension=entry_6.get()
    fr=entry_1.get()
    password=entry_7.get()
    send_email(to,subject,body,attachment,extension,fr,password)
    

label_0 = Label(root, text="My Mail",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="From",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_7 = Label(root, text="Password",width=20,font=("bold", 10))
label_7.place(x=80,y=180)

entry_7 = Entry(root,show="*")
entry_7.place(x=240,y=180)

label_2 = Label(root, text="To",width=20,font=("bold", 10))
label_2.place(x=80,y=230)

entry_2 = Entry(root)
entry_2.place(x=240,y=230)

label_3 = Label(root, text="Subject",width=20,font=("bold", 10))
label_3.place(x=68,y=280)

entry_3 = Entry(root)
entry_3.place(x=240,y=280)

label_4 = Label(root, text="Body",width=20,font=("bold", 10))
label_4.place(x=68,y=330)

entry_4 = Entry(root)
entry_4.place(x=240,y=330)

label_5 = Label(root, text="Attachment",width=20,font=("bold", 10))
label_5.place(x=68,y=380)

entry_5 = Entry(root)
entry_5.place(x=240,y=380)

label_6 = Label(root, text="Extension",width=20,font=("bold", 10))
label_6.place(x=68,y=430)

entry_6 = Entry(root)
entry_6.place(x=240,y=430)


Button(root, text='Submit',width=20,bg='brown',fg='white',command=getint).place(x=180,y=500)
# it is use for display the registration form on the window
root.mainloop()



#-----------------------------------------------------------------------------------------------------------------
