#############################################
#                   Import
#############################################
import random
import sys
import os
import sqlite3
import tkinter.simpledialog
from tkinter import messagebox
from sqlite3 import Error

#############################################
#                   Macros
#############################################
SAVE_DIR = '.\\saves\\'
DB_DIR = '.\\db\\'
##############################################
#             Global Variables
##############################################
session = None
start_flag = False
win_flag = False
lose_flag = False
draw_flag = False
match_won_flag = False
match_lost_flag = False
opponent_score = 0
player_score = 0
match_won = 0
player_name = ''

##############################################
#                 Database
##############################################
def sql_connection():

    try:
        if not os.path.exists(DB_DIR):
            os.mkdir(DB_DIR)
        con = sqlite3.connect(DB_DIR + 'game_data.db')
        print(f"Connection is established: Database is created in {DB_DIR}")
        return con

    except Error:
        print(Error)


connection = sql_connection()

##############################################
#                  Classes
##############################################


class GamePlayHandler:
    # Class Variables

    # Class Default Constructor
    def __init__(self):
        self.opponent_hand = 0
        self.player_hand = 0

    # Class Functions
    def get_opponent_hand(self):
        self.opponent_hand = random.randrange(0, 2)
        return self.opponent_hand

    def set_player_hand(self, input):
        global start_flag
        start_flag = True
        self.player_hand = input

    def check_winner(self):
        global lose_flag
        global win_flag
        global draw_flag
        global opponent_score
        global player_score
        global match_won_flag
        global match_lost_flag
        global match_won

        result = self.player_hand - self.opponent_hand
        if start_flag:
            if (result == -1) or (result == 2):
                lose_flag = True
                opponent_score += 1
            elif (result == 1) or (result == -2):
                win_flag = True
                player_score += 1
            else:
                draw_flag = True
                # Do nothing
        if player_score == 3:
            match_won_flag = True
            match_won += 1
            GamePlayHandler.reset()
        if opponent_score == 3:
            match_lost_flag = True
            GamePlayHandler.reset()
            GamePlayHandler.reset_match()

    @staticmethod
    def reset():
        global opponent_score
        global player_score
        opponent_score = 0
        player_score = 0

    @staticmethod
    def reset_match():
        global match_won
        match_won = 0

##############################################
#                  Functions
##############################################


def on_new():
    global session
    session = GamePlayHandler()
    # session.reset()


def on_player_name():
    global player_name
    if player_name == '':
        player_name = tkinter.simpledialog.askstring('Name', 'What is your name?')
    return player_name


def on_opponent_choice():
    global session
    return session.get_opponent_hand()


def on_play(num):
    global session
    on_new()
    session.set_player_hand(num)
    opponent_hand_tmp = on_opponent_choice()
    session.check_winner()
    return opponent_hand_tmp


def display_winner():
    global lose_flag
    global win_flag
    global draw_flag
    global match_won_flag
    global match_lost_flag
    if lose_flag:
        messagebox.showinfo(title='You Lose', message='Sorry, The Opponent Won The Round!')
        lose_flag = False
    elif win_flag:
        messagebox.showinfo(title='You Win', message='Congratulation, You Won The Round!')
        win_flag = False
    elif draw_flag:
        messagebox.showinfo(title='Draw', message='Welp, Looks Like That\'s A Draw!')
        draw_flag = False
    else:
        messagebox.showinfo(title='???', message='Something Went Wrong!')
        sys.exit()

    if match_won_flag:
        messagebox.showinfo(title='Match Won', message='You Won The Match!')
        match_won_flag = False
    if match_lost_flag:
        messagebox.showinfo(title='Match Lost', message='Sorry, You Lost The Match!')
        match_lost_flag = False


def check_match_won():
    global match_won
    messagebox.showinfo(title='Number of Games Won', message=f'You Have Won {match_won} Games.')


def save_game():
    global opponent_score
    global player_score
    global match_won
    global player_name
    print('Saving...')
    if not os.path.exists(SAVE_DIR):
        os.mkdir(SAVE_DIR)
    save = open(SAVE_DIR + 'save_game.save', 'w')
    save.write(f'pn:{player_name}\nos:{opponent_score}\nps:{player_score}\nmw:{match_won}')
    save.close()
    messagebox.showinfo(title='Game Saved', message='Saved!')


def load_game():
    global opponent_score
    global player_score
    global match_won
    global player_name
    print('Loading...')
    line = 'a'
    if not os.path.exists(SAVE_DIR):
        messagebox.showinfo(title='Error', message='No Save Found!')
    load = open(SAVE_DIR + 'save_game.save', 'r')
    while line != '':
        line = load.readline()
        print('Reading line: ' + str(line))
        if 'pn:' in line:
            player_name = str(line[line.index(':')+1:])
        elif 'os:' in line:
            opponent_score = int(line[line.index(':')+1:])
        elif 'ps:' in line:
            player_score = int(line[line.index(':')+1:])
        elif 'mw:' in line:
            match_won = int(line[line.index(':')+1:])
        else:
            break


def main():
    pass


if __name__ == "__main__":
    main()