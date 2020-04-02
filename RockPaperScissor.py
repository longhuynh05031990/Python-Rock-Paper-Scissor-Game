#############################################
#                   Import
#############################################
import tkinter as Tk
import os
import sys
import random
from PIL import Image, ImageTk
from functions import GamePlayHandler as Gp

#############################################
#                   Macros
#############################################
IMAGE_DIR = '.\\images\\'
ICON = '.\\images\\icon.ico'
ROCK_ICON = ''
PAPER_ICON = ''
SCISSOR_ICON = ''
NONE_ICON = ''
for r, d, f in os.walk(IMAGE_DIR, topdown=True):
    for name in f:
        if 'Rock' in name:
            ROCK_ICON = os.path.join(r, name)
        elif 'Paper' in name:
            PAPER_ICON = os.path.join(r, name)
        elif 'Scissor' in name:
            SCISSOR_ICON = os.path.join(r, name)
        else:
            NONE_ICON = os.path.join(r, name)
print('Printing...' + ROCK_ICON + ' ' + PAPER_ICON + ' ' + SCISSOR_ICON + ' ' + NONE_ICON)
##############################################
#             Global Variables
##############################################
opponent_name_list = ['Liam', 'Noah', 'William', 'James', 'Oliver',
                      'Emma', 'Olivia', 'Ava', 'Isabella', 'Sophia']

global_player_name = ''

##############################################
#                     UI
##############################################

main_window = Tk.Tk()
main_window.geometry('384x320')
main_window.title("Rock Paper Scissor Game")
main_window.iconbitmap(default=ICON)

# Display a prompt for the player to input their name
while global_player_name == '':
    global_player_name = Gp.on_player_name()

main_window.lift()
# Display a toolbar with File and Leaderboard submenus
menu_bar = Tk.Menu(main_window)
main_window.config(menu=menu_bar)

# File submenu
fileMenu = Tk.Menu(menu_bar)
fileMenu.add_command(label="New", command=lambda: on_new_wrapper())
fileMenu.add_command(label="Save", command=lambda: save_game_wrapper())
fileMenu.add_command(label="Load", command=lambda: load_game_wrapper())
fileMenu.add_command(label="Exit", command=sys.exit)

# Option submenu
optionMenu = Tk.Menu(menu_bar)
optionMenu.add_command(label="Check Number of Matches You Have Won", command=lambda: check_match_won_wrapper())

# Leaderboard submenu
lbMenu = Tk.Menu(menu_bar)
lbMenu.add_command(label='View Leaderboard')
lbMenu.add_command(label='Clear Leaderboard')

# About submenu
aboutMenu = Tk.Menu(menu_bar)
aboutMenu.add_command(label="About the Author")

# Display the toolbar
menu_bar.add_cascade(label="File", menu=fileMenu)
menu_bar.add_cascade(label="Option", menu=optionMenu)
menu_bar.add_cascade(label="Leaderboard", menu=lbMenu)
menu_bar.add_cascade(label="About", menu=aboutMenu)

# Display the name of the opponent
opponent_name = opponent_name_list[random.randrange(0, 9)]
opponent_name_canvas = Tk.Canvas(main_window, width=128, height=128, confine=True)
opponent_name_text = Tk.Label(opponent_name_canvas, text=opponent_name, height=1, width=10, pady=32)
opponent_name_text.config(font=("Courier", 15))
opponent_name_text.pack()
opponent_name_canvas.grid(row=0, column=0)

# Display the current score of the opponent
opponent_score_canvas = Tk.Canvas(main_window, width=128, height=128, confine=True)
opponent_score_text = Tk.Label(opponent_score_canvas, text=str(Gp.opponent_score), height=1, width=5, pady=32)
opponent_score_text.config(font=("Courier", 30))
opponent_score_text.pack()
opponent_score_canvas.grid(row=0, column=2)

# Display the current hand of the opponent
opponent_hand = ImageTk.PhotoImage(file=NONE_ICON)
opponent_hand_canvas = Tk.Canvas(main_window, width=128, height=128, bg='Red', confine=True)
opponent_hand_canvas.create_image(64, 64, image=opponent_hand)
opponent_hand_canvas.grid(row=0, column=1)

# Display the name of the player
player_name_canvas = Tk.Canvas(main_window, width=128, height=128, confine=True)
player_name_text = Tk.Label(player_name_canvas, text=global_player_name, height=1, width=10, pady=32)
player_name_text.config(font=("Courier", 15))
player_name_text.pack()
player_name_canvas.grid(row=1, column=2)

# Display the current score of the player
player_score_canvas = Tk.Canvas(main_window, width=128, height=128, confine=True)
player_score_text = Tk.Label(player_score_canvas, text=str(Gp.player_score), height=1, width=5, pady=32)
player_score_text.config(font=("Courier", 30))
player_score_text.pack()
player_score_canvas.grid(row=1, column=0)

# Display the current hand of the player
player_hand = ImageTk.PhotoImage(file=NONE_ICON)
player_hand_canvas = Tk.Canvas(main_window, width=128, height=128, bg='Blue', confine=True)
player_hand_canvas.create_image(64, 64, image=player_hand)
player_hand_canvas.grid(row=1, column=1)

##############################################
#                 Functions
##############################################
# on_play_wrapper
# Description: Wrapper of on_play - The function to display the image of player's choice
# Parameter(s): choice - input from player by pressing the buttons
# Return: void
# Note: To be used as command for each button on the UI


def on_play_wrapper(choice):
    global opponent_score_text
    global player_score_text
    image_dict = {
        0: ROCK_ICON,
        1: PAPER_ICON,
        2: SCISSOR_ICON
    }
    player_hand_tmp_img = ImageTk.PhotoImage(file=image_dict.get(choice, 'Invalid Choice'))
    player_hand_canvas.create_image(64, 64, image=player_hand_tmp_img)
    opponent_hand_tmp = Gp.on_play(choice)
    opponent_score_text.config(text=str(Gp.opponent_score))
    opponent_hand_tmp_img = ImageTk.PhotoImage(file=image_dict.get(opponent_hand_tmp, 'Invalid Choice'))
    opponent_hand_canvas.create_image(64, 64, image=opponent_hand_tmp_img)
    player_score_text.config(text=str(Gp.player_score))
    Gp.display_winner()


# check_match_won_wrapper
# Description: Wrapper of check_match_won - The function to display the number of matches won by the player
# Parameter(s): void
# Return: void
def check_match_won_wrapper():
    Gp.check_match_won()


# save_game_wrapper
# Description: Wrapper of save_game - The function to save the current game
# Parameter(s): void
# Return: void
def save_game_wrapper():
    Gp.save_game()


# load_game_wrapper
# Description: Wrapper of load_game - The function to load a save
# Parameter(s): void
# Return: void
def load_game_wrapper():
    Gp.load_game()


# on_new_wrapper
# Description: Wrapper of on_new - The function to start a new game
# Parameter(s): void
# Return: void
def on_new_wrapper():
    Gp.on_new()

# All buttons to play Rock Paper Scissor


b = Tk.Button(main_window, text='Rock', width=10, command=lambda: on_play_wrapper(0))
b.grid(row=3, column=0, pady=15)

b = Tk.Button(main_window, text='Paper', width=10, command=lambda: on_play_wrapper(1))
b.grid(row=3, column=1)

b = Tk.Button(main_window, text='Scissor', width=10, command=lambda: on_play_wrapper(2))
b.grid(row=3, column=2)

# toolbar.grid(row=3, column=1)
# Display UI
main_window.mainloop()
