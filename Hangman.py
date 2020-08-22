# -*- coding: utf-8 -*-
"""
@author: KSHITIJ
Credits: Web Dev Junkie: "youtube.com/channel/UCsrVDPJBYeXItETFHG0qzyw"
         https://github.com/chrishorton
"""
#functions

def pr(A):
    for i in A:
        print(i," ",end = "")



#STEP 1: setup the word and hidden list

word = list("mediterranean".upper())
empty = ["-"]*len(word)


taken_attempts = 0
available_attempts = 6



HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
      |
      |
=========''']





#STEP 2: loop while game is played:
gameover = False

while not gameover:
    
    #STEP 3: display current board, guessed letters and remaining attempts
    
    print(f"\n\nWrong attempts remaining = {available_attempts-taken_attempts}\n\n")
    print("GUESSED :\n")
    pr(HANGMANPICS[taken_attempts]) 
    

    #STEP 4: input character
    
    c = input("\nEnter a char acter to guess or enter <space> to end game: ").upper()
   
    if(len(c) != 1):
        print("\nPlease enter a single character\n")
        continue
    elif(c == " "):
        print("Game aborted.")
        break
    
    
    #STEP 5: correct => reveal all matched char in empty and print empty
    if c in word:    
        print(f"\nCorrect guess (^‿^).  {c} is in the word.\n")
        for i in range(0,len(word)):
            if (word[i] == c):
                empty[i] = c
                word[i] = "-"
            
        pr(empty)
        print("\n")
        #pr(word)
    
    
    #STEP 6: incorrect => increment taken_attempts
    else:
        print(f"\nIncorrect guess (◔_◔)  \"{c}\" is not in the word.\n")
        taken_attempts += 1
        
    
    #STEP 7: End conditions
        
    if "-" not in empty:
        print("\nYou won!!! Hangman lives. ✌(-‿-)✌ \n")
        gameover = True
    
    elif taken_attempts == available_attempts:
        print("\nYou lost. Hangman is hanged. ¯\_(ツ)_/¯ \n")
        gameover = True

    
    
    
    
    
    
    
    
    
    
    