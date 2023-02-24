from tkinter import *
import pandas as pd
import random

# ------------------------------ CONSTANTS -------------------------------

BACKGROUND_COLOR = "#B1DDC6"


# ------------------------------ DATA ------------------------------------

data = pd.read_csv("data/finnishtoenglish.csv")
word_dict = data.to_dict(orient="records")
current_card = {}


# ------------------------------ NEXT CARD ------------------------------------

def next_card():
    global current_card
    current_card = random.choice(word_dict)
    canvas.itemconfig(card_title, text="Finnish", fill="black")
    canvas.itemconfig(card_word, text=current_card["Finnish"], fill="black")
    canvas.itemconfig(card_image, image=card_front_img)


# ------------------------------ FLIP CARD ----------------------------------


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_image, image=card_back_img)




# ------------------------------ UI --------------------------------------

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas must have width and height arguments
canvas = Canvas(width=800, height=526)

# Canvas Image:-------------------------

# Any image must be made using Photoimage
card_front_img = PhotoImage(file="images/card_front.png")

card_back_img = PhotoImage(file="images/card_back.png")

# Add the photo to the canvas with create_image()
card_image = canvas.create_image(400, 263, image=card_front_img)

# Canvas Text: -------------------------

card_title = canvas.create_text(400, 150, text="Finnish", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 300, text="kippis", font=("Ariel", 60, "bold"))


canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

canvas.grid(column=0, row=0, columnspan=2)

flip_image = PhotoImage(file="images/wrong.png")
flip_button = Button(image=flip_image, highlightthickness=0, command=flip_card)
flip_button.grid(column=0, row=1)

next_image = PhotoImage(file="images/right.png")
next_button = Button(image=next_image, highlightthickness=0, command=next_card)
next_button.grid(column=1, row=1)


next_card()


window.mainloop()