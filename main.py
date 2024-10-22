
from tkinter import *
import pandas as pd
import random as r
BACKGROUND_COLOR = "#B1DDC6"


to_learn={}
#,--------read file--------------
try:
    data=pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data=pd.read_csv("data/french_words.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")

#. random french word funct
current_card={}
def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card=r.choice(to_learn)
    canvas.itemconfig(language_title,text="French",fill="black")
    canvas.itemconfig(word_title,text=current_card["French"],fill="black")
    canvas.itemconfig(card_bg,image=front_img)
    timer=window.after(3000,func=flip_card)
def flip_card():
    canvas.itemconfig(language_title, text="English",fill="white")
    canvas.itemconfig(word_title,text=current_card["English"],fill="white")
    canvas.itemconfig(card_bg,image=back_img)
def is_known():
    to_learn.remove(current_card)
    data=pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()
#.Window creation
window=Tk()
window.title("Card App for learning French")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)


#* COMPONENTS 
timer=window.after(3000,func=flip_card)
#. Canva


front_img=PhotoImage(file="images/card_front.png")
back_img=PhotoImage(file="images/card_back.png")

    
    
canvas=Canvas(width=800, height=526, bg=BACKGROUND_COLOR,highlightthickness=0)
card_bg=canvas.create_image(400,263,image=front_img)
canvas.grid(column=0,row=0, columnspan=2)
language_title=canvas.create_text(400,150,text="Title", font=("Ariel",40,"italic")) 
word_title=canvas.create_text(400,263,text="word", font=("Ariel",60,"bold"))
#. Button Right
button_img_right=PhotoImage(file="images/right.png")
button_right=Button(image=button_img_right,highlightthickness=0,command=is_known)
button_right.grid(column=0, row=1)
#.Button Wrong
button_img_wrong=PhotoImage(file="images/wrong.png")
button_wrong=Button(image=button_img_wrong,highlightthickness=0,command=next_card)
button_wrong.grid(column=1, row=1)
next_card()
window.mainloop()