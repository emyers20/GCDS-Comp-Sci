# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 08:42:21 2023

@author: emyers26
"""
#Author: Evan Myers
#Date: 12/1/23
#Challenges: Typewriter effect, while loop, lowercase input, time .sleep, score, reset button
#Bugs: none
#Sources: Ms. Marciano, https://python.plainenglish.io/typewriter-animation-using-python-7f4275e812bf, 
#Description:Interactive program which allows user to play rock paper scissors with the computer


import time#bringing in the library time so that I can use the function sleep
import sys#bringing in the System library to use to write the characters and flush the terminal. 
import random#brining in the random library ot use to select a random choice

#creates the sentence and the type delay variable so that it can be plugged in and called
def typewriter_effect(sentence, type_delay):
    # for each character in sentence type it in the typewriter effect
    for char in sentence:

        # Write, display and delay
        sys.stdout.write(char)#tells system to write character
        sys.stdout.flush()#takes the data in the buffer and clears it.
        time.sleep(type_delay)#adds delay to the sleep so they are the same

    time.sleep(1)# Pause after printing the entire sentence



def main():#puts all code in a main function
    type_delay = 0.025#sets the speed that the characters are typed out in
    user_score = 0# makes the user score start at 0
    comp_score = 0# makes the Computers score start at 0
    score_limit = 5# makes the highest score possible
    weapon = ["rock", "paper", "scissors"]# list of possible weapons
    typewriter_effect("Rock, Paper, Scissors \n", type_delay)#displays words in type writter effect
    print()#prints blank line

    
          
    while True:#infinite loop that runs while the condition true is true 

        if user_score >= score_limit or comp_score >= score_limit:#does whatever is under it when the user or computer score reach the score limit
            if user_score >= score_limit: #if the user's score reaches the score limit than it does whatever is under
                typewriter_effect("You win! \n" , type_delay)#displays words in type writter effect
                print()#prints blank line


            elif comp_score >= score_limit:  #if the computer's score reaches the score limit than it does whatever is under
                typewriter_effect("I win! \n", type_delay )#displays words in type writter effect
                print()#prints blank line

                
            while True:#infinite loop that runs while the condition true is true 
            
                ply_again = str.lower(input("do you want to play again?"))#asks the user if they want to play again then puts their answer in lowercase
                print()#prints blank line

                if ply_again == "no":# if the user  answers no
                    sys.exit()# ends the code
                elif ply_again == "yes":# if the user answers yes
                    typewriter_effect("keep playing! \n", type_delay)#displays words in type writter effect
                    print()#prints blank line

                    user_score = 0# sets user score to 0
                    comp_score = 0#sets computer score to 0
                    break#Manually breaks the infinite loop
                else:# if anything else it typed
                    typewriter_effect("invalid \n", type_delay)#displays words in type writter effect
                    print()#prints blank line

        
        user_choice = str.lower(input("Enter stop to end. Enter reset to reset score. Welcome to RPS, Select your weapon from above: "))#asks user to select a weopon and puts that answer into lowercase
        print()#prints blank line

        comp_answer = random.choice(weapon)#makes computer select a random string from the list
        
        if user_choice == "stop":# if the user types stop
            break#Manually breaks the infinite loop
        elif user_choice == "reset":#or if the user types reset
            user_score = 0#set user score to 0
            comp_score = 0# set computer score to 0
        elif user_choice not in weapon:#if the user types a string that is not apart of the list of weopons
            typewriter_effect("Not a valid choice \n", type_delay)#displays words in type writter effect
            print()#prints blank line

        else:#if none of the conditions above get fufilled it goes to this
            print("I chooose: "+(comp_answer) + " and you chose: "+ (user_choice))# displays the computer random choice and adds  the user's choice
            print()#prints blank line

            if user_choice == comp_answer:# if the two answers are the same weapon
                typewriter_effect("We tied \n", type_delay)#displays words in type writter effect
                print()#prints blank line

                
            elif user_choice == "rock" and comp_answer == "paper":# condition that gets fufilled only when the user types a specific thing and the Computer picks a certain thing
                typewriter_effect("Looks like I won! \n", type_delay)#displays words in type writter effect
                print()#prints blank line

                comp_score += 1# adds a score to the user or the computer depending on who won
                
            elif user_choice == "paper" and comp_answer == "rock":# condition that gets fufilled only when the user types a specific thing and the Computer picks a certain thing
                typewriter_effect("Uh oh you beat me:/ \n", type_delay) #displays words in type writter effect
                print()#prints blank line

                user_score += 1# adds a score to the user or the computer depending on who won
                
            elif user_choice == "paper" and comp_answer == "scissors":# condition that gets fufilled only when the user types a specific thing and the Computer picks a certain thing
                typewriter_effect("Looks like I won! \n", type_delay)#displays words in type writter effect
                print()#prints blank line

                comp_score += 1# adds a score to the user or the computer depending on who won
                
            elif user_choice == "scissors" and comp_answer == "paper":# condition that gets fufilled only when the user types a specific thing and the Computer picks a certain thing
                typewriter_effect("Uh oh you beat me:/ \n", type_delay)#displays words in type writter effect
                print()#prints blank line

                user_score += 1# adds a score to the user or the computer depending on who won
                
            elif user_choice == "scissors" and comp_answer == "rock":# condition that gets fufilled only when the user types a specific thing and the Computer picks a certain thing
                typewriter_effect("Looks like I won! \n", type_delay)#displays words in type writter effect
                print()#prints blank line

                comp_score += 1# adds a score to the user or the computer depending on who won
                
            elif user_choice == "rock" and comp_answer == "scissors":# condition that gets fufilled only when the user types a specific thing and the Computer picks a certain thing
                typewriter_effect("Uh oh you beat me:/ \n", type_delay) #displays words in type writter effect
                print()#prints blank line

                user_score += 1# adds a score to the user or the computer depending on who won
            
            typewriter_effect(f"user score is: {user_score} and computer score is: {comp_score} \n", type_delay)#displays words in type writter effect
            print()#prints blank line

#but also inputs the two variables into the string
               
main()#closes the main function 