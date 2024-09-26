########################################
# Name: Gazi Shuraim Niloy
# Collaborators (if any): Sam Holmes
# GenAI Transcript (if any):
# Estimated time spent (hr): 20 mins
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

def wordle():
    # The main function to play the Wordle game.

    def enter_action():
        # What should happen when RETURN/ENTER is pressed.
        gw.show_message("You need to implement this method")


    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    
    


# Startup boilerplate
if __name__ == "__main__":
    wordle()
