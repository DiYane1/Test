# step one ... take irish coffee
from tkinter import *
from PIL import Image, ImageTk
from random import randint

# main window
root = Tk()
root.title("Rock Scissor Paper")
root.configure(background="#DFC5FE")

# picture
rock_img = ImageTk.PhotoImage(Image.open("Rock copy.png"))
paper_img = ImageTk.PhotoImage(Image.open("Paper copy.png"))
scissor_img = ImageTk.PhotoImage(Image.open("Scissor copy.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("Rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("Paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("Scissor.png"))

# insert picture
user_label = Label(root, image=scissor_img, bg="#F4BFFF")
comp_lable = Label(root, image=scissor_img_comp, bg="#F4BFFF")
comp_lable.grid(row=1, column=0)
user_label.grid(row=1, column=4)

# scores
playerScore = Label(root, text=0, font=100, bg="#F4BFFF", fg="black")
computerScore = Label(root, text=0, font=100, bg="#F4BFFF", fg="black")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

# indicators
user_indicator = Label(root, font=50, text="USER", bg="#F4BFFF", fg="black")
comp_indicator = Label(root, font=50, text="COMPUTER", bg="#F4BFFF", fg="black")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

# messages
msg = Label(root, font=50, bg="#F4BFFF", fg="black")
msg.grid(row=3, column=2)

# update message
def updateMessage(x):
    msg['text'] = x


# update user score
def updaeUserScore():
    score = int(playScore['text'])
    score += 1
    playerScore["text"] = str(score)


# update computer score
def updateComputer():
    score = int(computerScore['text'])
    score += 1
    computerScore["text"] = str(score)


# check winner
def checkWin(player, computer):
    if player == computer:
        updateMessage("It's a tie!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You lose!")
            updateComputerScore()
        else:
            updateMessage("You win!")
            updateUserScore
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You lose!")
            updateComputerScore()
        else:
            updateMessage("You win!")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You lose!")
            updateComputerScore()
        else:
            updateMessage("You win")
            updateUserScore()

    else:
        pass

# update choices
choices = ["rock", "paper", "scissor"]


def updateChoice(x):
    # for computer
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_lable.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_lable.configure(image=paper_img_comp)
    else:
        comp_lable.configure(image=scissor_img_comp)

    # for user
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "pape":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x,compChoice)

# buttons
rock = Button(root, width=20, height=2, text="ROCK",bg="#FF3E4D", fg="black", command=lambda: updateChoice("rock")).grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER",bg="#FF3E4D", fg="black", command=lambda: updateChoice("paper")).grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR", bg="#FF3E4D", fg="black", command=lambda: updateChoice("scissor")).grid(row=2, column=3)

root.mainloop()