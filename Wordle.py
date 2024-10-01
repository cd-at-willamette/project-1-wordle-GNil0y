########################################
# Name: Gazi Shuraim Niloy
# Collaborators (if any): Shouvik Ahmed, Kara Dryer
# GenAI Transcript (if any):
# Estimated time spent (hr): 
# Description of any added extensions:
########################################

from WordleGraphics import WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import ENGLISH_WORDS, is_english_word
import random

def get_random_five_letter_word():
    while True:
        word = random.choice(ENGLISH_WORDS)
        if len(word) == 5:
         return word.lower() 

def wordle():
    gw = WordleGWindow()
    secret_word = get_random_five_letter_word()  
    print(f"Secret word: {secret_word}")  
    
    current_row = 0
   
    def enter_action():
        check_answer(gw, gw.get_current_row(), secret_word)   

    gw.add_enter_listener(enter_action)

def get_words(gw, row):
    
    word = ""
    for x in range(N_COLS):
        word += gw.get_square_letter(row, x)
    return word

def check_answer(gw, row, secret_word):
    user_entry = get_words(gw, row).lower()
    if not is_english_word(user_entry):
        gw.show_message("Not an English word")
        return


    user_words = list(user_entry)
    secret_words = list(secret_word)
    remaining_letters = list(secret_words)

    # First pass for correct (green) letters
    for x in range(len(user_words)):
        if user_words[x] == secret_words[x]:
            gw.set_square_color(row, x, CORRECT_COLOR)  
            remaining_letters[x] = None  

    # Second pass for present (yellow) and missing (grey) letters
    for x in range(len(user_words)):
        if user_words[x] == secret_words[x]:
            continue
        elif user_words[x] in remaining_letters:
            gw.set_square_color(row, x, PRESENT_COLOR)
            remaining_letters[remaining_letters.index(user_words[x])] = None  
        else:
            gw.set_square_color(row, x, MISSING_COLOR)

    new_row=gw.get_current_row()+1
    gw.set_current_row(new_row)

    # Check 
    if user_words == secret_words:
        gw.show_message("You win!")

        


# Startup boilerplate
if __name__ == "__main__":
    wordle()
