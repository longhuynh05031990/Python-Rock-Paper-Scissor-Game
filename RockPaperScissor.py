#############################################
#                   Import
#############################################
import tkinter as Tk
import os
import random
from PIL import Image, ImageTk
#############################################
#                   Macros
#############################################
IMAGE_DIR = '.\\images\\'
ICON = '.\\images\\icon.ico'
ROCK_ICON = ''
PAPER_ICON = ''
SCISSOR_ICON = ''
for r, d, f in os.walk(IMAGE_DIR, topdown=True):
    for name in f:
        if 'Rock' in name:
            ROCK_ICON = os.path.join(r, name)
        elif 'Paper' in name:
            PAPER_ICON = os.path.join(r, name)
        else:
            SCISSOR_ICON = os.path.join(r, name)
print('Printing...' + ROCK_ICON + ' ' + PAPER_ICON + ' ' + SCISSOR_ICON)
##############################################
#             Global Variables
##############################################
opponent_name_list = ['Liam', 'Noah', 'William', 'James', 'Oliver',
                      'Emma', 'Olivia', 'Ava', 'Isabella', 'Sophia']

##############################################
#                     UI
##############################################
main_window = Tk.Tk()
main_window.geometry('384x320')
main_window.title("Rock Paper Scissor Game")
main_window.iconbitmap(default=ICON)

# Display a toolbar with File and Leaderboard submenus
menu_bar = Tk.Menu(main_window)
main_window.config(menu=menu_bar)

# File submenu
fileMenu = Tk.Menu(menu_bar)
fileMenu.add_command(label="New")
fileMenu.add_command(label="Save")
fileMenu.add_command(label="Load")

# Leaderboard submenu
lbMenu = Tk.Menu(menu_bar)
lbMenu.add_command(label='View Leaderboard')
lbMenu.add_command(label='Clear Leaderboard')

# Display the toolbar
menu_bar.add_cascade(label="File", menu=fileMenu)
menu_bar.add_cascade(label="Leaderboard", menu=lbMenu)

# Display the name of the opponent
opponent_name = opponent_name_list[random.randrange(0, 9)]
opponent_name_canvas = Tk.Canvas(main_window, width=128, height=128, confine=True)
opponent_name_text = Tk.Label(opponent_name_canvas, text=opponent_name, height=1, width=10, pady=32)
opponent_name_text.config(font=("Courier", 15))
opponent_name_text.pack()
opponent_name_canvas.grid(row=0, column=0)

# Display the current score of the opponent
opponent_score_canvas = Tk.Canvas(main_window, width=128, height=128, confine=True)
opponent_score_text = Tk.Label(opponent_score_canvas, text='1', height=1, width=5, pady=32)
opponent_score_text.config(font=("Courier", 30))
opponent_score_text.pack()
opponent_score_canvas.grid(row=0, column=2)

# Display the name of the player
player_name = opponent_name_list[random.randrange(0, 9)]
player_name_canvas = Tk.Canvas(main_window, width=128, height=128, confine=True)
player_name_text = Tk.Label(player_name_canvas, text=player_name, height=1, width=10, pady=32)
player_name_text.config(font=("Courier", 15))
player_name_text.pack()
player_name_canvas.grid(row=1, column=2)

# Display the current score of the player
player_score_canvas = Tk.Canvas(main_window, width=128, height=128, confine=True)
player_score_text = Tk.Label(player_score_canvas, text='1', height=1, width=5, pady=32)
player_score_text.config(font=("Courier", 30))
player_score_text.pack()
player_score_canvas.grid(row=1, column=0)

# Display the current hand of the opponent
opponent_hand = ImageTk.PhotoImage(file=ROCK_ICON)
opponent_hand_canvas = Tk.Canvas(main_window, width=128, height=128, bg='Red', confine=True)
opponent_hand_canvas.create_image(64, 64, image=opponent_hand)
opponent_hand_canvas.grid(row=0, column=1)

# Display the current hand of the player
player_hand = ImageTk.PhotoImage(file=SCISSOR_ICON)
player_hand_canvas = Tk.Canvas(main_window, width=128, height=128, bg='Blue', confine=True)
player_hand_canvas.create_image(64, 64, image=player_hand)
player_hand_canvas.grid(row=1, column=1)

# Display the name of the player

# toolbar = Tk.Frame(main_window)

# All buttons to play Rock Paper Scissor
b = Tk.Button(main_window, text='Rock', width=10)
b.grid(row=3, column=0, pady=15)

b = Tk.Button(main_window, text='Paper', width=10)
b.grid(row=3, column=1)

b = Tk.Button(main_window, text='Scissor', width=10)
b.grid(row=3, column=2)

# toolbar.grid(row=3, column=1)
# Display UI
main_window.mainloop()