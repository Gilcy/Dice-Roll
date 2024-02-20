from tkinter import *
from PIL import ImageTk,Image
import random

win =Tk()
win.title("Dice Roll App")
score=0
def ROLL_DICE():
  global score
  Var=random.randint(1,6)
  Var2=random.randint(1,6)
  if(Var==Var2):
    score=score+1
  ScoreL.config(text="Score= "+str(score))
  if(Var==1):
    path="Dice1.jpg"
    img=ImageTk.PhotoImage(Image.open(path))
    Dice1L.config(image=img)
    Dice1L.image=img
  if(Var==2):
     path="Dice2.jpg"
     img=ImageTk.PhotoImage(Image.open(path))
     Dice1L.config(image=img)
     Dice1L.image=img
  if(Var==3):
     path="Dice3.jpg"
     img=ImageTk.PhotoImage(Image.open(path))
     Dice1L.config(image=img)
     Dice1L.image=img
  if(Var==4):
     path="Dice4.jpg"
     img=ImageTk.PhotoImage(Image.open(path))
     Dice1L.config(image=img)
     Dice1L.image=img
  if(Var==5):
     path="Dice5.jpg"
     img=ImageTk.PhotoImage(Image.open(path))
     Dice1L.config(image=img)
     Dice1L.image=img
  if(Var==6):
     path="Dice6.jpg"
     img=ImageTk.PhotoImage(Image.open(path))
     Dice1L.config(image=img)
     Dice1L.image=img
  if(Var2==1):
      path="Dice1.jpg"
      img=ImageTk.PhotoImage(Image.open(path))
      Dice2L.config(image=img)
      Dice2L.image=img
  if(Var2==2):
      path="Dice2.jpg"
      img=ImageTk.PhotoImage(Image.open(path))
      Dice2L.config(image=img)
      Dice2L.image=img
  if(Var2==3):
      path="Dice3.jpg"
      img=ImageTk.PhotoImage(Image.open(path))
      Dice2L.config(image=img)
      Dice2L.image=img
  if(Var2==4):
      path="Dice4.jpg"
      img=ImageTk.PhotoImage(Image.open(path))
      Dice2L.config(image=img)
      Dice2L.image=img
  if(Var2==5):
      path="Dice5.jpg"
      img=ImageTk.PhotoImage(Image.open(path))
      Dice2L.config(image=img)
      Dice2L.image=img
  if(Var2==6):
      path="Dice6.jpg"
      img=ImageTk.PhotoImage(Image.open(path))
      Dice2L.config(image=img)
      Dice2L.image=img


path="Dice1.jpg"
img=ImageTk.PhotoImage(Image.open(path))
Dice1L=Label(win,image=img)
Dice1L.place(x=30,y=50)
Dice1L.image=img
path="Dice2.jpg"
img=ImageTk.PhotoImage(Image.open(path))
Dice2L=Label(win,image=img)
Dice2L.place(x=270,y=50)
Dice2L.image=img
ScoreL=Label(win,text="Score=0",font=("Arial",,"bold"))
ScoreL.place(x=220,y=20)

A=Button(win, text="Roll Dice",command=ROLL_DICE)
A.place(x=200,y=240)




win.mainloop()from tkinter import *
from PIL import ImageTk,Image
import random

win =Tk()
win.title("Dice Roll App")
score=0
def ROLL_DICE():
  global score
  Var=random.randint(1,6)
  Var2=random.randint(1,6)
  if(Var==Var2):
    score=score+1
  ScoreL.config(text="Score= "+str(score))
  if(Var==1):
    path="Dice1.jpg"
    img=ImageTk.PhotoImage(Image.open(path))
    Dice1L.config(image=img)
    Dice1L.image=img
  if(Var==2):
     path="Dice2.jpg"
     img=ImageTk.PhotoImage(Image.open(path))
     Dice1L.config(image=img)
     Dice1L.image=img
  if(Var==3):
     path="Dice3.jpg"
     img=ImageTk.PhotoImage(Image.open(path))
     Dice1L.config(image=img)
     Dice1L.image=img
  if(Var==4):
     path="Dice4.jpg"
     img=ImageTk.PhotoImage(Image.open(path))
     Dice1L.config(image=img)
     Dice1L.image=img
  if(Var==5):
     path="Dice5.jpg"
     img=ImageTk.PhotoImage(Image.open(path))
     Dice1L.config(image=img)
     Dice1L.image=img
  if(Var==6):
     path="Dice6.jpg"
     img=ImageTk.PhotoImage(Image.open(path))
     Dice1L.config(image=img)
     Dice1L.image=img
  if(Var2==1):
      path="Dice1.jpg"
      img=ImageTk.PhotoImage(Image.open(path))
      Dice2L.config(image=img)
      Dice2L.image=img
  if(Var2==2):
      path="Dice2.jpg"
      img=ImageTk.PhotoImage(Image.open(path))
      Dice2L.config(image=img)
      Dice2L.image=img
  if(Var2==3):
      path="Dice3.jpg"
      img=ImageTk.PhotoImage(Image.open(path))
      Dice2L.config(image=img)
      Dice2L.image=img
  if(Var2==4):
      path="Dice4.jpg"
      img=ImageTk.PhotoImage(Image.open(path))
      Dice2L.config(image=img)
      Dice2L.image=img
  if(Var2==5):
      path="Dice5.jpg"
      img=ImageTk.PhotoImage(Image.open(path))
      Dice2L.config(image=img)
      Dice2L.image=img
  if(Var2==6):
      path="Dice6.jpg"
      img=ImageTk.PhotoImage(Image.open(path))
      Dice2L.config(image=img)
      Dice2L.image=img


path="Dice1.jpg"
img=ImageTk.PhotoImage(Image.open(path))
Dice1L=Label(win,image=img)
Dice1L.place(x=30,y=50)
Dice1L.image=img
path="Dice2.jpg"
img=ImageTk.PhotoImage(Image.open(path))
Dice2L=Label(win,image=img)
Dice2L.place(x=270,y=50)
Dice2L.image=img
ScoreL=Label(win,text="Score=0",font=("Arial",10,"bold"))
ScoreL.place(x=220,y=20)

A=Button(win, text="Roll Dice",command=ROLL_DICE)
A.place(x=200,y=240)


  

win.mainloop()
