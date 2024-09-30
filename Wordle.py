########################################
# Name: Gazi Shuraim Niloy
# Collaborators (if any): Shouvik Ahmed
# GenAI Transcript (if any):
# Estimated time spent (hr): 
# Description of any added extensions:
########################################

from WordleGraphics import WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import ENGLISH_WORDS, is_english_word
import random

def wordle():
    
    gw = WordleGWindow()
    secret_word = "happy".lower()  
    current_row = 0  

    def enter_action():
        nonlocal current_row  
        if current_row < N_ROWS:  
            check_answer(gw, current_row, secret_word)  
            current_row += 1  
            if current_row < N_ROWS:  
                gw.set_current_row(current_row)  
   

    gw.add_enter_listener(enter_action)

def get_words(gw, row):
    word = ""
    for x in range(N_COLS):
        word += gw.get_square_letter(row, x)
    return word

def check_answer(gw, row, secret_word):
    user_entry = get_words(gw, row).lower()
    
    # Validate English word
    if not is_english_word(user_entry):
        gw.show_message("Not an English word")
        return

    user_words = list(user_entry)
    secret_words = list(secret_word)
    remaining_letters = list(secret_words)  #

    #  (green) letters
    for x in range(len(user_words)):
        if user_words[x] == secret_words[x]:
            gw.set_square_color(row, x, CORRECT_COLOR)
            remaining_letters[x] = None  # Mark as used

    #  (yellow) and (grey) letters
    for x in range(len(user_words)):
        if user_words[x] == secret_words[x]:
            continue
        elif user_words[x] in remaining_letters:
            gw.set_square_color(row, x, PRESENT_COLOR)
            remaining_letters[remaining_letters.index(user_words[x])] = None  
        else:
            gw.set_square_color(row, x, MISSING_COLOR)

    # Check 
    if user_words == secret_words:
        gw.show_message("You win!")

# Startup boilerplate
if __name__ == "__main__":
    wordle()
