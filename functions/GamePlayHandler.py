#############################################
#                   Import
#############################################
import random
import sys
from tkinter import messagebox

#############################################
#                   Macros
#############################################

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
##############################################
#                  Classes
##############################################


class GamePlayHandler:
    # Class Variables

    # Class Constructor
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
    messagebox.showinfo(title='Number of Games Won', message='You Have Won ' + str(match_won) + ' Games.')


def main():
    pass


if __name__ == "__main__":
   main()