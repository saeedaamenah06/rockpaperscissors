import tkinter
import random
from tkinter import *
root = Tk()
#Tk() use to initialize Tkinter to create window
root.geometry('400x400')
#geometry() sets the window width and height
root.resizable(0,0)
#resizable(0,0) by this command we can fix the size of the window
root.title('Rock, Paper, Scissors')
#title() used to set the title of the window
root.config(bg = '#7695B1')
#bg = ‘’ use to set the color of the background
Label(root, text = 'Rock, Paper , Scissors' , font='arial 20 bold', bg = '#7695B1').pack()
#Label() widget used when we want to display text that users can’t modify.
#root is the name of our window
#text which displays on the label as the title of that label
#font in which form the text is written
#pack used to the organized widget in form of block
user_take = StringVar()
Label(root, text = 'choose one: rock, paper , scissors' , font='arial 15 bold', bg = 'white').place(x = 20,y=70)
Entry(root, font = 'arial 15', textvariable = user_take , bg = 'white').place(x=90 , y = 130)
#user_take is a string type variable that stores the choice that the user enters.
#Entry() widget used when we want to create an input text field.
#textvariable used to retrieve the text to entry widget
#place() - place widgets at specific position
comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick ==2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'
#random.randint() function will randomly take any number from the given number.
Result = StringVar()
def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('tie, you both have made the same selection.')
    elif user_pick == 'r' and comp_pick == 'paper':
        Result.set('you lose,the computer selected paper')
    elif user_pick == 'r' and comp_pick == 'scissors':
        Result.set('you win,the computer selected scissors.')
    elif user_pick == 'p' and comp_pick == 'scissors':
        Result.set('you lose,the computer selected scissors')
    elif user_pick == 'p' and comp_pick == 'rock':
        Result.set('you win,the computer selected rock')
    elif user_pick == 's' and comp_pick == 'rock':
        Result.set('you lose,the computer selected rock')
    elif user_pick == 's' and comp_pick == 'paper':
        Result.set('you win , the computer selected paper')
    else:
        Result.set('invalid: choose one -- rock, paper, scissors')
def Reset():
    Result.set("") 
    user_take.set("")
def Exit():
    root.destroy()
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='white',width = 50,).place(x=25, y = 250)
Button(root, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='#D0E2F2' ,command = play).place(x=150,y=190)
Button(root, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='#D0E2F2' ,command = Reset).place(x=70,y=310)
Button(root, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='#D0E2F2' ,command = Exit).place(x=230,y=310)
root.mainloop()
#Button() widget used when we want to display a button.
#command called the specific function when the button will be clicked.
#root.mainloop() method executes when we run our program.
