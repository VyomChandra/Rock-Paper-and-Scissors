from tkinter import * 
from tkinter.ttk import *
import random
import tkinter as tk


window = tk.Tk()
window.geometry("400x500")
window.title("Rock Paper and Scissors") 

USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ""
COMP_CHOICE = "" 

def choice_to_number(choice):
    rps = {'Rock':1,'Paper':2,'Scissor':3}
    return rps[choice]
def number_to_choice(number):
    rps={1:'Rock',2:'Paper',3:'Scissor'}
    return rps[number]

def random_computer_choice():
    return random.choice(['Rock','Paper','Scissor']) 

def result(human_choice,comp_choice):
    global USER_SCORE
    global COMP_SCORE
    user=choice_to_number(human_choice)
    comp=choice_to_number(comp_choice)
    if(user==comp):
        print("Since you both chose the same. It's a Tie")
    elif((user-comp)%3==1):
        print("Hurrah! You win")
        USER_SCORE+=1
    else:
        print("Oops! System wins")
        COMP_SCORE+=1
    
    
    Font_setting = ("Comic Sans MS", 12, "bold")
    text_area = tk.Text(master=window,height=12,width=30,bg="white",font = Font_setting)
    text_area.grid(column=0,row=4)
    answer = "Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n Computer Score : {c} ".format(uc=USER_CHOICE,cc=COMP_CHOICE,u=USER_SCORE,c=COMP_SCORE)    
    text_area.insert(tk.END,answer)
  
    
def rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='Rock'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)
def paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='Paper'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)
def scissor():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='Scissor'
    COMP_CHOICE=random_computer_choice() 
    result(USER_CHOICE,COMP_CHOICE)
    
    

rock_pic = PhotoImage(file = r"rock1.png")
photoimage1 = rock_pic.subsample(1)            # Resizing image to fit on button
Button1 = tk.Button(text="Rock",image= photoimage1, bg="skyblue",command=rock)
Button1.grid(column=0,row=1)

paper_pic = PhotoImage(file = r"paper1.png")
photoimage2 = paper_pic.subsample(1)            
Button2 = tk.Button(text="Paper",image= photoimage2, bg="skyblue",command=paper)
Button2.grid(column=0,row=2)

scissor_pic = PhotoImage(file = r"scissor1.png")
photoimage3 = scissor_pic.subsample(1)           
Button3 = tk.Button(text="Scissor",image= photoimage3, bg="skyblue",command=scissor)
Button3.grid(column=0,row=3)

window.mainloop()