# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""
import sys
import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle(): 

    def enter_action(s):
        #Concatenating the word the user inputted
        current_row = gw.get_current_row()
        
        userWordList = []
        for letter in range(N_COLS):
            userWordList.append(WordleGWindow.get_square_letter(gw, current_row, letter))
        
        userWord = ''.join(userWordList)
        userWord = userWord.lower()
        print(userWord)
        print(word)
        
        #If word is good do this
        if userWord in FIVE_LETTER_WORDS:
            
            gw.show_message("This word is in the word list")
            
            
            for char in range(N_COLS):
                if userWord[char] in word[char]:
                    #color the letter in the right spot green
                    gw.set_square_color(current_row, char, CORRECT_COLOR)
                elif userWord[char] in word:
                    #color the letter thats in the word but not th right spot yellow
                    gw.set_square_color(current_row, char, PRESENT_COLOR)
                else:
                    #color the letter that isn't in the word grey
                    gw.set_square_color(current_row, char, MISSING_COLOR)
                    
            current_row = current_row + 1
            gw.set_current_row(current_row)
        #If word guess isn't in wordlist
        else:
            gw.show_message("Not in word list")
        
        if userWord == word:
            gw.show_message("You win! Click Enter to exit")
        
        if current_row == 6:
            gw.show_message("You lost. Better luck next time!")

    def display_word(word):
            for x in range(N_COLS):
                WordleGWindow.set_square_letter(gw, N_ROWS-6, x, word[x])
                
   
                
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    
    number = random.randint(0, len(FIVE_LETTER_WORDS)-1)
    word = FIVE_LETTER_WORDS[number]
    display_word(word)
    
    
# Startup code

if __name__ == "__main__":
    wordle()
