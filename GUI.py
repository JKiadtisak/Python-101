from tkinter import *
from tkinter import ttk
from tkinter import messagebox


GUI = Tk ()
GUI.title('โปรแกรมบันทึกการอ่าน')
GUI.geometry('500x400')

L1 = Label (GUI,text='ตารางอ่านหนังสือรายวัน',font=('sukhumvit',15),fg='black')
L1.place(x=165,y=20)

def Button1 () :
    text = 'เพราเป็นวุ่นจึงเจ็บปวด 80 หน้า'
    messagebox.showinfo ('ชื่อหนังสือ',text)


FB1 = LabelFrame(GUI)
FB1.place (x=200,y=70)
B1 = ttk.Button(FB1,text='Monday',command=Button1)
B1.pack(ipadx=20,ipady=3)

#######################################

def Button2 () :
    text = 'เจ้าชายน้อย 20 หน้า '
    messagebox.showinfo ('ชื่อหนังสือ',text)


FB1 = LabelFrame(GUI)
FB1.place (x=200,y=100)
B2 = ttk.Button(FB1,text='Tuesday',command=Button2)
B2.pack(ipadx=20,ipady=3)

################

def Button3 () :
    text = 'จิตวิทยาการรู้คิด 30 หน้า '
    messagebox.showinfo ('ชื่อหนังสือ',text)


FB1 = LabelFrame(GUI)
FB1.place (x=200,y=130)
B3 = ttk.Button(FB1,text='Wednesday',command=Button3)
B3.pack(ipadx=20,ipady=3)

####################

def Button4 () :
    text = 'อิคิไก 40 หน้า '
    messagebox.showinfo ('ชื่อหนังสือ',text)


FB1 = LabelFrame(GUI)
FB1.place (x=200,y=160)
B4 = ttk.Button(FB1,text='Thursday',command=Button3)
B4.pack(ipadx=20,ipady=3)

#############

def Button5 () :
    text = 'Into The Magic Shop 60 หน้า '
    messagebox.showinfo ('ชื่อหนังสือ',text)


FB1 = LabelFrame(GUI)
FB1.place (x=200,y=190)
B5 = ttk.Button(FB1,text='Friday',command=Button5)
B5.pack(ipadx=20,ipady=3)


##################

def Button6 () :
    text = 'Mindset 30 หน้า '
    messagebox.showinfo ('ชื่อหนังสือ',text)


FB1 = LabelFrame(GUI)
FB1.place (x=200,y=220)
B6 = ttk.Button(FB1,text='Saturday',command=Button6)
B6.pack(ipadx=20,ipady=3)


################

def Button7 () :
    text = 'Think Again 70 หน้า '
    messagebox.showinfo ('ชื่อหนังสือ',text)


FB1 = LabelFrame(GUI)
FB1.place (x=200,y=250)
B7 = ttk.Button(FB1,text='Sunday',command=Button7)
B7.pack(ipadx=20,ipady=3)






