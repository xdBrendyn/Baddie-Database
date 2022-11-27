from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import time
from data.Database import member_names
from data.Passwords import login

f = open('data\\Database.py', 'r')
f = open('data\\Passwords.py', 'r')

#database_current = []

def home_start():

    global homeLabel
    global info
    global infoLine

    #Button Animation
    user_panel_button.config(fg='white')
    root.update()
    time.sleep(0.01)
    user_panel_button.config(fg='#8C8C8C')

    #Add home screen
    homeLabel = Label(panel_canvas, text="Welcome", font=("Bahnschrift Bold",50),bg='#4A4A4A',fg='#8C8C8C', highlightthickness=0)
    homeLabel.place(x=700,y=250,anchor=CENTER)

    info = Label(panel_canvas, text="Baddie Database is my first ever developed GUI program. Made for my brother, it doesn't have much to offer.\nThe whole premis of this program is to add and remove 'baddies' from a 'Baddie Database'."
                                    "\nWho knows, maybe I get bored and add more features for regular users too.\nOther than that, enjoy Baddie Database!"
                 , font=("Bahnschrift",15),bg='#4A4A4A',fg='#8C8C8C', highlightthickness=0)
    info.place(x=700,y=350,anchor=CENTER)
    infoLine = panel_canvas.create_line(500,274,900,274,fill='#595959',width=5, tag='info')

def home():

    user_panel_button.config(state=DISABLED)
    user_panel_button1.config(state=ACTIVE)

    try:
        entry_label.destroy()
    except NameError:
        pass

    try:
        admin_entry.destroy()
    except NameError:
        pass

    try:
        hide_password.destroy()
    except NameError:
        pass

    try:
        show_password.destroy()
    except NameError:
        pass

    try:
        baddie_entry.destroy()
    except NameError:
        pass

    try:
        text_label.destroy()
    except NameError:
        pass

    try:
        admin_label.destroy()
    except NameError:
        pass

    global homeLabel
    global info
    global infoLine

    #Button Animation
    user_panel_button.config(fg='white')
    root.update()
    time.sleep(0.01)
    user_panel_button.config(fg='#8C8C8C')

    #Add home screen
    homeLabel = Label(panel_canvas, text="Welcome", font=("Bahnschrift Bold",50),bg='#4A4A4A',fg='#8C8C8C', highlightthickness=0)
    homeLabel.place(x=700,y=250,anchor=CENTER)

    info = Label(panel_canvas, text="Baddie Database is my first ever developed GUI program. Made for my brother, it doesn't have much to offer.\nThe whole premis of this program is to add and remove 'baddies' from a 'Baddie Database'."
                                    "\nWho knows, maybe I get bored and add more features for regular users too.\nOther than that, enjoy Baddie Database!"
                 , font=("Bahnschrift",15),bg='#4A4A4A',fg='#8C8C8C', highlightthickness=0)
    info.place(x=700,y=350,anchor=CENTER)
    infoLine = panel_canvas.create_line(500,274,900,274,fill='#595959',width=5, tag='info')

def usercheck(*args):

    global user
    user = admin_entry.get()


    #Password Check
    if user in login:
        print("Password was correct")
        admin_entry.grid_remove()
        admin_entry.delete(0, END)

        admin_access()
    else:
        entry_label.config(text="Password was incorrect")
        for i in range(15):
            root.update()
            time.sleep(0.1)
        entry_label.config(text="Enter the admin password")

def baddie_database(*args):
    global isBaddie
    isBaddie = baddie_entry.get()
    isBaddie = isBaddie.capitalize()
    is_alpha = any(not c.isalpha() for c in isBaddie)

    #Characters Filter
    if is_alpha == True:
        text_label.config(text='Please enter only characters')
        for i in range(15):
            root.update()
            time.sleep(0.1)
        text_label.config(text="Enter a name")

    elif isBaddie == '':
        text_label.config(text='Please enter a name')
        for i in range(15):
            root.update()
            time.sleep(0.1)
        text_label.config(text="Enter a name")

    elif isBaddie in member_names:
        text_label.config(text=(isBaddie + ' is already in our database'))

        #if isBaddie not in database_current:
            #database_current.append(isBaddie)

        remove_user = messagebox.askyesno('Database Removal', ("Would you like to remove " + '"' + isBaddie + '"' + ' from our database?'))

        if remove_user == True:
            #database_current.remove(isBaddie)
            text_label.config(text=(isBaddie + ' was removed from the database'))
            for i in range(15):
                root.update()
                time.sleep(0.1)
            text_label.config(text="Enter a name")

            member_names.remove(isBaddie)
            f = open('data\\Database.py', 'w')
            f.write("member_names = " + str(member_names))
            f.close()

    else:
        #database_current.append(isBaddie)
        member_names.append(isBaddie)
        f = open('data\\Database.py', 'w')
        f.write("member_names = " + str(member_names))
        f.close()

        text_label.config(text=(isBaddie + ' was added to our database!'))
        for i in range(15):
            root.update()
            time.sleep(0.1)
        text_label.config(text="Enter a name")

    #print(database_current)

def admin_pannel():

    user_panel_button.config(state=ACTIVE)
    user_panel_button1.config(state=DISABLED)

    #Button Animation
    user_panel_button1.config(fg='white')
    root.update()
    time.sleep(0.01)
    user_panel_button1.config(fg='#8C8C8C')

    #Remove home page
    panel_canvas.delete(False, 'info')
    homeLabel.destroy()
    info.destroy()

    global admin_entry
    global entry_label
    global show_password
    global hide_password

    #Login Prompt
    entry_label = Label(panel_canvas, text="Enter the admin password", font=("Bahnschrift",15),bg='#4A4A4A',fg='#8C8C8C', highlightthickness=0)
    entry_label.place(x=700,y=350,anchor=CENTER)

    admin_entry = Entry(panel_canvas, width=25, font=('Bahnschrift', 24), fg='#CFCFCF', bg='#2E2E2E', insertbackground='#CFCFCF',highlightthickness=0, relief=FLAT, show='*')
    admin_entry.place(x=700,y=300,anchor=CENTER)
    admin_entry.bind('<Return>',usercheck)

    #Show Password

    def show_pass():
        global hide_password
        admin_entry.config(show='')
        show_password.destroy()

        def hide_pass():
            global show_password
            admin_entry.config(show='*')
            hide_password.destroy()
            show_password = Button(panel_canvas, text='show', font=("Bahnschrift", 12), bg='#4A4A4A', fg='#8C8C8C',
                                   relief=SUNKEN,
                                   bd=0, highlightthickness=0, activebackground='#4A4A4A', activeforeground='#8C8C8C',
                                   command=show_pass)
            show_password.place(x=930, y=285)

        hide_password = Button(panel_canvas, text='hide', font=("Bahnschrift", 12), bg='#4A4A4A', fg='#8C8C8C',
                               relief=SUNKEN,
                               bd=0, highlightthickness=0, activebackground='#4A4A4A', activeforeground='#8C8C8C',command=hide_pass)
        hide_password.place(x=935, y=285)

    show_password = Button(panel_canvas, text='show', font=("Bahnschrift", 12), bg='#4A4A4A',fg='#8C8C8C', relief = SUNKEN,
                           bd = 0, highlightthickness = 0, activebackground = '#4A4A4A', activeforeground = '#8C8C8C',command=show_pass)
    show_password.place(x=930,y=285)

    #(panel_canvas, text='Home', font=("Bahnschrift", 15), bg = '#4A4A4A', fg = '#8C8C8C', relief = SUNKEN,
    #bd = 0, highlightthickness = 0, activebackground = '#4A4A4A', activeforeground = '#8C8C8C', command = home)

    #4A4A4A
    #8C8C8C

def admin_access():
    root.update()

    #Destory Admin Panel
    try:
        entry_label.destroy()
    except NameError:
        pass

    try:
        admin_entry.destroy()
    except NameError:
        pass

    try:
        hide_password.destroy()
    except NameError:
        pass

    try:
        show_password.destroy()
    except NameError:
        pass

    global baddie_entry
    global text_label
    global admin_label

    #Labels
    admin_label = Label(panel_canvas, text="ADMIN", font=("Bahnschrift Bold",25),bg='#4A4A4A',fg='#8C8C8C', highlightthickness=0)
    admin_label.place(x=700,y=200,anchor=CENTER)

    text_label = Label(panel_canvas, text="Enter a name", font=("Bahnschrift",15),bg='#4A4A4A',fg='#8C8C8C', highlightthickness=0)
    text_label.place(x=700,y=350,anchor=CENTER)

    #Login Prompt
    baddie_entry = Entry(panel_canvas, width=25, font=('Bahnschrift', 24), fg='#CFCFCF', bg='#2E2E2E', insertbackground='#CFCFCF',highlightthickness=0, relief=FLAT)
    baddie_entry.place(x=700,y=300,anchor=CENTER)
    baddie_entry.bind('<Return>',baddie_database)

def exit():
    root.quit()

def enter_text(event):
    global name
    name = panel_entry.get()
    name = name.capitalize()
    is_alpha = any(not c.isalpha() for c in name)

    #Characters Filter
    if is_alpha == True:
        panel_entry.grid_remove()
        panel_entry.delete(0, END)
        name_label = Label(root,text='Please enter only characters', font=("Bahnschrift", 20), bg='#3D3D3D',fg='#8C8C8C')
        name_label.grid(column=1,row=1)
        root.update()
        time.sleep(1)
        name_label.destroy()
        panel_entry.grid(column=1,row=1)

    elif name == '':
        panel_entry.grid_remove()
        panel_entry.delete(0, END)
        name_label = Label(root,text='Please enter a name', font=("Bahnschrift", 20), bg='#3D3D3D',fg='#8C8C8C')
        name_label.grid(column=1,row=1)
        root.update()
        time.sleep(1)
        name_label.destroy()
        panel_entry.grid(column=1,row=1)

    elif name in member_names:
        panel_entry.grid_remove()
        panel_entry.delete(0, END)
        name_label = Label(root,text=('Welcome, ' + name), font=("Bahnschrift", 20), bg='#3D3D3D',fg='#8C8C8C')
        name_label.grid(column=1,row=1)
        root.update()
        time.sleep(1.5)
        name_label.destroy()
        panel_entry.grid(column=1,row=1)

        panel_open()

    else:

        #member_names.append(name)
        #f = open('data\\Database.py', 'w')
        #f.write("member_names = " + str(member_names))
        #f.close()

        panel_entry.grid_remove()
        panel_entry.delete(0, END)
        name_label = Label(root,text=("'" + name + "'" + ' not found'), font=("Bahnschrift", 20), bg='#3D3D3D',fg='#8C8C8C')
        name_label.grid(column=1,row=1)

        for i in range(2):
            name_label.config(fg='#A21E1E')
            time.sleep(0.1)
            root.update()
            name_label.config(fg='#8C8C8C')
            time.sleep(0.1)
            root.update()

        root.update()
        time.sleep(0.5)
        name_label.destroy()
        panel_entry.grid(column=1,row=1)


root = Tk()

#Canvas
canvas = Canvas(root, width=1280, height=720, highlightthickness=0, bg="#3D3D3D")
canvas.grid(columnspan=3, rowspan=5)

# Application
root.title('Baddie Database')
app_icon = PhotoImage(file='img\\icon_small.png')
root.iconphoto(True, app_icon)
root.config(bg='#3D3D3D')
root.resizable(False, False)
#root.geometry('1280x720')

# Logo
logo = PhotoImage(file='img\\new_logo.png')
logo_label = Label(image=logo, background='#3D3D3D')
logo_label.grid(column=1, row=0)

# Instructions
instructions = Label(root, text="Enter your name to find out if you're in the Baddie Database", font=("Bahnschrift", 20), bg='#3D3D3D',fg='#8C8C8C')
instructions.grid(columnspan=3, row=5)

# Panel Entry
panel_entry = Entry(root, width=25, font=('Bahnschrift', 24), fg='#CFCFCF', bg='#2E2E2E', insertbackground='#CFCFCF',highlightthickness=0, relief=FLAT)
panel_entry.grid(column=1, row=1)
panel_entry.bind('<Return>', enter_text)

# Panel
small_logo = PhotoImage(file='img\\new_logo_diff_50.png')

def panel_open():

    #Remove Old Panel
    canvas.destroy()
    logo_label.destroy()
    instructions.destroy()
    panel_entry.destroy()

    root.geometry('1280x720')

    global panel_canvas

    #New Panel
    panel_canvas = Canvas(root,width=1260,height=700,highlightthickness=0, bg="#4A4A4A")
    panel_canvas.place(relx=.5, rely=.5,anchor= CENTER)
    small_logo_label = Label(panel_canvas,image=small_logo,background='#4A4A4A')
    small_logo_label.place(x=30,y=3)

    line1 = panel_canvas.create_line(175,1260,175,0,fill='#3D3D3D',width=10)
    line2 = panel_canvas.create_line(0,75,175,75,fill='#3D3D3D',width=10)

    welcome_label = Label(panel_canvas, text=('Hi, ' + name),font=("Bahnschrift Bold", 15),bg='#4A4A4A',fg='#8C8C8C', highlightthickness=0)
    welcome_label.place(x=85,y=105,anchor=CENTER)
    line5 = panel_canvas.create_line(5,130,165,130,fill='#595959',width=5)

    global user_panel_button
    global user_panel_button1

    #Buttons
    user_panel_button = Button(panel_canvas, text='Home',font=("Bahnschrift", 15),bg='#4A4A4A',fg='#8C8C8C',relief=SUNKEN,
                               bd=0,highlightthickness=0,activebackground='#4A4A4A',activeforeground='#8C8C8C',command=home,state=DISABLED)
    user_panel_button.place(x=50,y=154)
    line3 = panel_canvas.create_line(15,200,150,200,fill='#595959',width=1)

    user_panel_button1 = Button(panel_canvas, text='Admin',font=("Bahnschrift", 15),bg='#4A4A4A',fg='#8C8C8C',relief=SUNKEN,
                               bd=0,highlightthickness=0,activebackground='#4A4A4A',activeforeground='#8C8C8C',command=admin_pannel)
    user_panel_button1.place(x=47.5,y=215)

    user_panel_button_exit = Button(panel_canvas, text='Exit',font=("Bahnschrift", 15),bg='#4A4A4A',fg='#8C8C8C',relief=SUNKEN,
                               bd=0,highlightthickness=0,activebackground='#4A4A4A',activeforeground='#8C8C8C',command=exit)
    user_panel_button_exit.place(x=57.5,y=650)
    line4 = panel_canvas.create_line(15,640,150,640,fill='#595959',width=1)

    home_start()

root.mainloop()