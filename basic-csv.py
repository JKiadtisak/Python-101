from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
##############CSV###############
import csv

def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(datalist) # datalist = ['pen','pencil','eraser']


def readcsv():
    with open('data.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file) #fr = file reader
        data = list(fr)
    return data
#############################

GUI = Tk() # นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูลหนังสือ') #นี่คือชื่อโปรแกรม
GUI.geometry('1000x750') #นี่คือขนาดโปรแกรม

L1 = Label(GUI,text='โปรแกรมบันทึกข้อมูลหนังสือ',font=('Angsana New',30),fg='green')
L1.place(x=350,y=30)



################## แสดง log ด้านขวา ###############################

FB2 = LabelFrame(GUI, text='', font=('Angsana New', 16, "bold"))  # กรอบรวมด้านขวามือ
FB2.place(x=220, y=100)

# Create a Text widget to display log messages
log_text = Text(FB2, font=('Angsana New', 16), height=10, width=80)
log_text.pack(pady=20, padx=25)

# Create a Scrollbar widget and attach it to the Text widget
scrollbar = ttk.Scrollbar(FB2, orient=VERTICAL, command=log_text.yview)
scrollbar.place(x=590, y=20, height=295)
log_text.config(yscrollcommand=scrollbar.set)

# Read data from CSV and insert into Text widget
data = readcsv()
for row in data:
    log_text.insert(END, "\n")
    log_text.insert(END, row)
    log_text.insert(END, "\n")



##########SECTION RIGHT##########
LF1 = ttk.LabelFrame(GUI,text='กรอกชื่อหนังสือ')
LF1.place(x=390,y=480)


v_data = StringVar() # ตัวแปรพิเศษที่ใช้กับข้อความใน gui
E1 = ttk.Entry(LF1,textvariable=v_data,font=('Angsana New',25))
E1.pack(pady=10,padx=10)

from datetime import datetime

def SaveData():
    t = datetime.now().strftime('%Y%m%d %H%M%S')
    data = v_data.get() #ดึงข้อมูลจากตัวแปร v_data มาใช้งาน
    text = [t,data] # [เวลา,ข้อมูลที่ได้จากการกรอก]
    writecsv(text) #บันทึกลง csv
    v_data.set('') #เคลียร์ข้อมูลที่อยู่ในช่องกรอก

B4 = ttk.Button(LF1,text='บันทึก',command=SaveData)
B4.pack(ipadx=10,ipady=10)



GUI.mainloop()
