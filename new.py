#step one ... take irish coffee
from tkinter import *
from PIL import Image, ImageTk
from random import randint

# Main window
root = Tk()
root.title("Rock Scissors Paper")
root.configure(background="#DFC5FE")

# Load images
rock_img = ImageTk.PhotoImage(Image.open("Rock copy.png"))
paper_img = ImageTk.PhotoImage(Image.open("Paper copy.png"))
scissor_img = ImageTk.PhotoImage(Image.open("Scissor copy.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("Rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("Paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("Scissor.png"))

# Create labels
user_label = Label(root, image=scissor_img, bg="#F4BFFF")
comp_label = Label(root, image=scissor_img_comp, bg="#F4BFFF")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

# Scores
player_score = Label(root, text="0", font=("Helvetica", 36), bg="#F4BFFF", fg="black")
computer_score = Label(root, text="0", font=("Helvetica", 36), bg="#F4BFFF", fg="black")
computer_score.grid(row=1, column=1)
player_score.grid(row=1, column=3)

# Indicators
user_indicator = Label(root, text="USER", font=("Helvetica", 24), bg="#F4BFFF", fg="black")
comp_indicator = Label(root, text="COMPUTER", font=("Helvetica", 24), bg="#F4BFFF", fg="black")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

# Messages
msg = Label(root, font=("Helvetica", 18), bg="#F4BFFF", fg="black")
msg.grid(row=3, column=2)

# Update message
def update_message(x):
    msg['text'] = x

# Update user score
def update_user_score():
    score = int(player_score['text'])
    score += 1
    player_score["text"] = str(score)

# Update computer score
def update_computer_score():
    score = int(computer_score['text'])
    score += 1
    computer_score["text"] = str(score)

# Check winner
def check_win(player, computer):
    if player == computer:
        update_message("It's a tie!!")
    elif player == "rock":
        if computer == "paper":
            update_message("You lose!")
            update_computer_score()
        else:
            update_message("You win!")
            update_user_score()
    elif player == "paper":
        if computer == "scissor":
            update_message("You lose!")
            update_computer_score()
        else:
            update_message("You win!")
            update_user_score()
    elif player == "scissor":
        if computer == "rock":
            update_message("You lose!")
            update_computer_score()
        else:
            update_message("You win!")
            update_user_score()
    else:
        pass

# Update choices
choices = ["rock", "paper", "scissor"]

def update_choice(x):
    # For computer
    comp_choice = choices[randint(0, 2)]
    if comp_choice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif comp_choice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)

    # For user
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    check_win(x, comp_choice)

# Buttons
rock = Button(root, width=20, height=2, text="ROCK", bg="#FF3E4D", fg="black", command=lambda: update_choice("rock"))
paper = Button(root, width=20, height=2, text="PAPER", bg="#FF3E4D", fg="black", command=lambda: update_choice("paper"))
scissor = Button(root, width=20, height=2, text="SCISSOR", bg="#FF3E4D", fg="black", command=lambda: update_choice("scissor"))
rock.grid(row=2, column=1)
paper.grid(row=2, column=2)
scissor.grid(row=2, column=3)

root.mainloop()
