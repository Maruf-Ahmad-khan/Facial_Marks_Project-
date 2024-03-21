import tkinter as ttk
from tkinter import font
app = ttk.Tk()
app.title('Attendance System')
app.geometry('600x400')
app.config(background='midnightblue')
font_ = font.Font(size=20)

ttk.Label(
    app, 
    text='Face Recognition based Attendance System',
    font=font_,bg='antiquewhite'
).pack()

def register():
    app.destroy()    
    with open('opr','w') as f:
        f.write('register')
    import login_admin
    
def attendance():
    print('Attendance')
    import attendance
    attendance.attendance()

def clear_data():
    app.destroy()   
    with open('opr','w') as f:
        f.write('clear')
    import login_admin

ttk.Button(
    app, text='Register', command=register, font=font_,
    height=3, width=15,bg ='antiquewhite'
).pack(expand=True)
ttk.Button(
    app, text='Attendance', command=attendance,font=font_,
    height=3, width=15,bg ='antiquewhite'
).pack(expand=True)
ttk.Button(
    app, text='Clear Data', command=clear_data,font=font_,
    height=3, width=15,bg ='antiquewhite'
).pack(expand=True)

app.mainloop()