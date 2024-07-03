from tkinter import *
import socket
from tkinter import filedialog
import os

root = Tk()
root.title("ShaFileMagic")
root.geometry("450x560")

# icon for our app
icon = PhotoImage(file='SFM icon.png')
root.iconphoto(True, icon)
root.configure(background='#3386FF')
root.resizable(True, True)

def Send():
    window = Toplevel(root)
    window.title("Send")
    window.geometry('450x560+500+200')
    window.configure(bg="#f4fdfe")
    window.resizable(True, True)

    def select_file():
        global filename
        filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                              title='Select File',
                                              filetypes=(('All Files', '*.*'),))

    def sender():
        s = socket.socket()
        host = socket.gethostname()
        port = 8080
        s.bind((host, port))
        s.listen(1)
        print(host)
        print('Waiting for any incoming connections.....')
        conn, addr = s.accept()
        with open(filename, 'rb') as file:
            chunk = file.read(1024)
            while chunk:
                conn.send(chunk)
                chunk = file.read(1024)
        conn.close()
        print('Data transmission successful!')

    image_icon1 = PhotoImage(file='send.png')
    window.iconphoto(True, image_icon1)

    SBackground = PhotoImage(file='Sender.png')
    Label(window, image=SBackground, bg='#f4fdfe').place(x=-2, y=0)

    MBackground = PhotoImage(file='id.png')
    Label(window, image=MBackground).place(x=100, y=260)

    host = socket.gethostname()
    Label(window, text=f'ID: {host}', bg='white', fg='black').place(x=140, y=290)

    Button(window, text='+ Select File', width=15, height=1, font='arial 14 bold', bg='#fff', fg='#000',
           command=select_file).place(x=140, y=150)

    Button(window, text='SEND', width=8, height=1, font='arial 14 bold', bg='#000', fg='#fff',
           command=sender).place(x=300, y=150)

    window.mainloop()

def Receive():
    window = Toplevel(root)
    window.title("Receive")
    window.geometry('450x560+500+200')
    window.configure(bg="#f4fdfe")
    window.resizable(True, True)

    def receiver():
        ID = SenderID.get()
        filename1 = incoming_file.get()

        s = socket.socket()
        port = 8080
        s.connect((ID, port))
        with open(filename1, 'wb') as file:
            while True:
                file_data = s.recv(1024)
                if not file_data:
                    break
                file.write(file_data)
        s.close()
        print('File receive successful!')

    image_icon2 = PhotoImage(file='receive.png')
    window.iconphoto(True, image_icon2)

    RBackground = PhotoImage(file='Receiver.png')
    Label(window, image=RBackground, bg='#f4fdfe').place(x=-2, y=0)

    logo = PhotoImage(file='profile.png')
    Label(window, image=logo, bg='#f4fdfe').place(x=100, y=250)

    Label(window, text='Receive', font=('Arial', 20), bg='#f4fdfe').place(x=100, y=280)

    Label(window, text='Input sender ID', font=('Arial', 10, 'bold'), bg='#f4fdfe').place(x=20, y=340)
    SenderID = Entry(window, width=25, fg='black', border=2, bg='white', font=('Arial', 15))
    SenderID.place(x=20, y=370)
    SenderID.focus()

    Label(window, text='File name for the incoming file: ', font=('Arial', 10, 'bold'), bg='#f4fdfe').place(x=20, y=420)
    incoming_file = Entry(window, width=25, fg='black', border=2, bg='white', font=('Arial', 15))
    incoming_file.place(x=20, y=450)

    imageicon = PhotoImage(file='arrow.png')
    Button(window, text='Receive', compound=LEFT, image=imageicon, width=130, bg='#39c790',font='Arial 14 bold',
           command=receiver).place(x=20, y=500)

    window.mainloop()

# Heading:'File Transfer'
Label(root, text='File Transfer', font=('Arial Black', 20, 'bold'), fg='white',bg='green').place(x=20, y=30)
Frame(root, width=400, height=2, bg='#8A33FF').place(x=25, y=80)

# send icon
send_image = PhotoImage(file='send.png')
Button(root, image=send_image, bg='#33F0FF', bd=0, command=Send).place(x=50, y=100)

# receive icon
receive_image = PhotoImage(file='receive.png')
Button(root, image=receive_image, bg='#33F0FF', bd=0, command=Receive).place(x=300, y=100)

Label(root, text='Send', font=('Consolas', 17, 'bold'), fg='white', bg='black').place(x=65, y=200)
Label(root, text='Receive', font=('Consolas', 20, 'bold'), fg='black', bg='green').place(x=300, y=200)

# background image
background = PhotoImage(file='background.png')
Label(root, image=background).place(x=-2, y=323)

root.mainloop()
