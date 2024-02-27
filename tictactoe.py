import tkinter as tk
from tkinter import messagebox
#from tkinter import Label
def start_menu():
    root=tk.Tk()
    root.geometry("400x200")
    root.title("TicTacToe!")
    label=tk.Label(text="Player1,Select The Option:")
    label.pack()
    global value
    def start_window():
        global value
        options=['X','O']
        value=tk.StringVar(root)
        value.set("Select X or O")
        menu=tk.OptionMenu(root, value, *options)
        menu.pack()
        submit_button = tk.Button(root, text='Submit', command=lambda:setopt(value.get()))
        submit_button.pack()
    global player1
    def destroyf():
        root.destroy()
    def setopt(b):
        global player1
        global player2
        global a
        a=b
        player1=b
        if b.lower()=='x':
            player2='O'
        else:
            player2='X'
        destroyf()
        game()

    
    start_window()
start_menu()
def game():
    def check_empty(c):
        if x[c['row']][c['column']]==None:
            return 1
        else:
            return 0
    def whowin(x):
        if x==player1:
            return "Player1 Won!"
        else:
            return "Player2 Won!"
    def check_win():
        if x[0][0]==x[0][1]==x[0][2] and not(x[0][0]==x[0][1]==x[0][2]==None):
            c=whowin(x[0][0])
            messagebox.showinfo("showinfo",c)
        elif x[1][0]==x[1][1]==x[1][2] and not(x[1][0]==x[1][1]==x[1][2]==None):
            c=whowin(x[1][0])
            messagebox.showinfo("showinfo",c)
        elif x[2][0]==x[2][1]==x[2][2]and not(x[2][0]==x[2][1]==x[2][2]==None):
            c=whowin(x[2][0])
            messagebox.showinfo("showinfo",c)
        elif x[0][0]==x[1][1]==x[2][2] and not(x[0][0]==x[1][1]==x[2][2]==None):
            c=whowin(x[0][0])
            messagebox.showinfo("showinfo",c)
        elif x[0][2]==x[0][1]==x[2][0] and not (x[0][2]==x[0][1]==x[2][0]==None):
            c=whowin(x[0][2])
            messagebox.showinfo("showinfo",c)
        elif x[0][0]==x[1][0]==x[2][0] and not(x[0][0]==x[1][0]==x[2][0]==None):
            c=whowin(x[0][0])
            messagebox.showinfo("showinfo",c)
        elif x[0][1]==x[1][1]==x[2][1] and not(x[0][1]==x[1][1]==x[2][1]==None):
            c=whowin(x[0][1])
            messagebox.showinfo("showinfo",c)
        elif x[0][2]==x[1][2]==x[2][2] and not(x[0][2]==x[1][2]==x[2][2]==None):
            c=whowin(x[0][2])
            messagebox.showinfo("showinfo",c)
        '''elif None not in x:
            messagebox.showinfo("Draw!","The Match is Draw!")'''
    def pl(b0):
        c=b0.grid_info()
        if check_empty(c):
            b0.config(text=a)
            x[c['row']][c['column']]=a
            check_win()
            change()
    def change():
        global a
        if a=="X":
            a="O"
        else:
            a="X"
    x=[[None,None,None],[None,None,None],[None,None,None]]
    root=tk.Tk()
    root.title("TicTacToe!")
    root.geometry("400x400")
    b0=tk.Button(root,text='',command=lambda:pl(b0))
    b1 =tk.Button(root,command=lambda:pl(b1))
    b2 =tk.Button(root,command=lambda:pl(b2))
    b3 =tk.Button(root,command=lambda:pl(b3))
    b4 =tk.Button(root,command=lambda:pl(b4))
    b5 =tk.Button(root,command=lambda:pl(b5))
    b6 =tk.Button(root,command=lambda:pl(b6))
    b7 =tk.Button(root,command=lambda:pl(b7))
    b8 =tk.Button(root,command=lambda:pl(b8))
    b9 =tk.Button(root,command=lambda:pl(b9))
    tk.Grid.rowconfigure(root,0,weight=1)
    tk.Grid.columnconfigure(root,0,weight=1)
    tk.Grid.rowconfigure(root,1,weight=1)
    tk.Grid.columnconfigure(root,1,weight=1)
    tk.Grid.rowconfigure(root,2,weight=1)
    tk.Grid.columnconfigure(root,2,weight=1)
    b0.grid(row=0,column=0,sticky='NSEW')
    b2.grid(row=0,column=1,sticky='NSEW')
    b3.grid(row=0,column=2,sticky='NSEW')
    b4.grid(row=1,column=0,sticky='NSEW')
    b5.grid(row=1,column=1,sticky='NSEW')
    b6.grid(row=1,column=2,sticky='NSEW')
    b7.grid(row=2,column=0,sticky='NSEW')
    b8.grid(row=2,column=1,sticky='NSEW')
    b9.grid(row=2,column=2,sticky='NSEW')
