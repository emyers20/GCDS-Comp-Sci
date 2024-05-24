# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 11:53:40 2023

@author: emyers26
"""
#Ar: Evan Myers
#11/13/23
#Challenges:none
#Bugs:none
#Sources: https://www.w3schools.com/python/python_lists_access.asp
#Description:Interactive program which allows user to ask computer question and get a random response


import random# puts in random  into the code

possible_responses = ["Yes", "No", "Maybye", "Ask again later"]# Sets list of possible answers computer spits back at you

print("Welcome to your magic 8 ball!")# displays what is in the qoutes.
print()# displays blank line
while True:#creates loop that is only broken when break which makes true false
    user_question = str.lower(input("Please type your question."+ " If You want to stop the ball type stop."))#displays what is in the quotes but also asks user a questioon
    print()# displays blank line
    if user_question == "stop":# if user types stop as an answer to the question
        break#stops the loop and ends the program
    response = random.choice(possible_responses)# makes a variable named response that has a random selection of inside the list in it.
    
    print(response)# displays the random selection 
    print()# displays blank line