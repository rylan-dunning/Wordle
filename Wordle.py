# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""
import sys
import random
import tkinter as tk

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, BLACK, WHITE, op_CORRECT_COLOR, op_KEY_COLOR, op_MISSING_COLOR, op_PRESENT_COLOR, op_UNKNOWN_COLOR


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
        
        EliminateWordsList = list(word) #List to keep track of which letters have been used
        
        guessWordList = list(userWord) #List to keep track of user's word eliminating letters throughout
        
        #If word is good do this
        if userWord in FIVE_LETTER_WORDS:
            
            gw.show_message("This word is in the word list")
            
            for char in range(N_COLS):
                if guessWordList[char] in EliminateWordsList[char]:
                    #color the letter in the right spot green
                    gw.set_square_color(current_row, char, CORRECT_COLOR)
                    EliminateWordsList[char] = "#" #Placeholder for letter already being used
                    guessWordList[char] = "&" #Placeholder for letter already being used
                    
            for char in range(N_COLS):
                if guessWordList[char] in EliminateWordsList:
                    #color the letter thats in the word but not th right spot yellow
                    gw.set_square_color(current_row, char, PRESENT_COLOR)
                    
                    for char2 in range(N_COLS):
                        if guessWordList[char] in EliminateWordsList[char2]:
                            EliminateWordsList[char2] = "#"
                            guessWordList[char] = "&"
                            break
                    
            for char in range(N_COLS):
                if guessWordList[char] != "&":
                    #color the letter that isn't in the word grey
                    gw.set_square_color(current_row, char, MISSING_COLOR)
                    
            current_row = current_row + 1
            
            
            if current_row > 5:
                gw.show_message("You lost. Better luck next time!")
            
            gw.set_current_row(current_row)
        #If word guess isn't in wordlist
        else:
            gw.show_message("Not in word list")
        
        if userWord == word:
            gw.show_message("You win! Click Enter to exit")
        
        

    def display_word(word):
            for x in range(N_COLS):
                WordleGWindow.set_square_letter(gw, N_ROWS-6, x, word[x])
                
    def invert_colors():
        val = var1.get()
        if val == 1:
            row = 0
            print("val is 1")
            while row < 6:
                for letter in range(N_COLS):
                    if gw.get_square_color(row, letter) == CORRECT_COLOR:
                        gw.set_square_color(row, letter, op_CORRECT_COLOR)
                        
                    if gw.get_square_color(row, letter) == PRESENT_COLOR:
                        gw.set_square_color(row, letter, op_PRESENT_COLOR)
                        
                    if gw.get_square_color(row, letter) == MISSING_COLOR:
                        gw.set_square_color(row, letter, op_MISSING_COLOR)            
                row = row + 1
        
            
        if val == 0:
            row = 0    
            print("val is 0")
            while row < 6:
                for letter in range(N_COLS):
                    if gw.get_square_color(row, letter) == op_CORRECT_COLOR:
                        gw.set_square_color(row, letter, CORRECT_COLOR)
                        
                    if gw.get_square_color(row, letter) == op_PRESENT_COLOR:
                        gw.set_square_color(row, letter, PRESENT_COLOR)
                        
                    if gw.get_square_color(row, letter) == op_MISSING_COLOR:
                        gw.set_square_color(row, letter, MISSING_COLOR)            
                row = row + 1
                
                
    
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    
    var1 = tk.IntVar()
    checkbutton = tk.Checkbutton(text="Dark Mode", variable=var1, command=invert_colors)
    checkbutton.pack()
    
    number = random.randint(0, len(FIVE_LETTER_WORDS)-1)
    word = FIVE_LETTER_WORDS[number]
    display_word(word)
    
    
    
    
# Startup code

if __name__ == "__main__":
    wordle()
