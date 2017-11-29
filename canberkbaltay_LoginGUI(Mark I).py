from tkinter import *
import os

creds = 'tempfile.temp'

def Signup():
    global pwordE
    global nameE
    global roots

    roots = Tk()
    roots.geometry("600x200")
    roots.configure(background="black")
    #logo = PhotoImage(file = "logo.gif")
    #Label (roots, image = logo, bg ="black").grid(row= 3, column = 4, sticky = E)
    roots.title('Signup')
    
    intruction = Label(roots, text='Please Enter Info\n', bg="black", fg="white", font="none 12 bold")
    intruction.grid(row = 0, column = 0, sticky = E)
    
    nameL = Label(roots, text = 'New Username: ', bg="black", fg="white", font="none 12 bold")
    pwordL = Label(roots, text = 'New Password: ', bg="black", fg="white", font="none 12 bold")
    nameL.grid(row = 1, column = 0, sticky = W)
    pwordL.grid(row = 2, column = 0, sticky = W)
    
    nameE = Entry(roots)
    pwordE = Entry(roots, show='*')
    
    nameE.grid(row = 1, column = 1)
    pwordE.grid(row = 2, column = 1)
    
    signupButton = Button(roots, text = 'Signup', command = FSSignup)
    signupButton.grid(columnspan = 2, sticky = W)
    roots.mainloop()

def FSSignup():
    with open(creds, 'w') as f:
        f.write(nameE.get())
        f.write('\n')
        f.write(pwordE.get())
        f.close()

    roots.destroy()
    Login()

def Login():
    global nameEL
    global pwordEL
    global rootA
    
    rootA = Tk()
    rootA.geometry("600x200")
    rootA.title('Login')
    rootA.configure(background="red")

    intruction = Label(rootA, text = 'Please Login\n',  bg="red", fg="white", font="none 12 bold")
    intruction.grid(sticky=E)

    nameL = Label(rootA, text = 'Username: ', bg="red", fg="white", font="none 12 bold")
    pwordL = Label(rootA, text = 'Password: ',  bg="red", fg="white", font="none 12 bold")
    nameL.grid(row = 1, sticky = W)
    pwordL.grid(row = 2, sticky = W)

    nameEL = Entry(rootA)
    pwordEL = Entry(rootA, show = '*')
    nameEL.grid(row = 1, column = 1 )
    pwordEL.grid(row = 2, column = 1)

    loginB = Button(rootA, text = 'Login', command = CheckLogin)
    loginB.grid(columnspan = 2, sticky = W)

    rmuser = Button(rootA, text = 'Delete User ', fg='red', command = DelUser)
    rmuser.grid(columnspan =2, sticky = W)
    rootA.mainloop()

def CheckLogin():
    with open(creds) as f:
        data = f.readlines()
        uname = data[0].rstrip()
        pword = data[1].rstrip()

    if nameEL.get() == uname and pwordEL.get() == pword:
        r = Tk()
        r.title('Success')
        r.geometry('450 x 150')
        rlbl = Label(r, text = '\n[+] Loggedin')
        rlbl.grid(row = 1, column = 1, sticky = W)
        rlbl.pack()
        r.mainloop()
    else:    
        r = Tk()
        r.title('Fail')
        r.geometry('450 x 150')
        rlbl = Label(r, text = '\n[!] Invalid Login')
        rlbl.grid(row = 1, column = 1, sticky = W)
        rlbl.pack()
        r.mainloop()
def DelUser():
    
        os.remove(creds)
        rootA.destroy()
        Signup()

if os.path.isfile(creds):
    Login()
else:
    Signup()
        

    
