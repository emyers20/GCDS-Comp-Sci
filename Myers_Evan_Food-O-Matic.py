# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 11:04:10 2024

@author: emyers26
"""

import random  # Imports random library
import sys# imports the sys library

foodType = ['local', 'roasted', 'grilled', 'mashed', 'oven dried', 'spiced', 'stewed', 'assorted', 'iced', 'sliced', 'braised', 'free-range', 'steamed']  # A list full of ways food can be cooked
mainDish = ['cauliflower', 'New york Strip Stake', 'pork loin', 'green beans', 'Jasmine rice', 'carrots', 'potatoes', 'sphagetti', 'Chiken', 'drumstick', 'short rib', 'duck breast', 'beef', 'baguette']  # A list of main dishes
sideDish = ['with soy sauce', 'truffle fries', 'noodles', 'with peas', 'with rice', 'with garlic and olive oil', 'with peas', 'with yogurt', 'soup', 'salad', 'with tropical fruit salad', 'over sticky rice']  # A list of sides to the main dishes
dishPrice = ['14', '23', '31', '16', '12', '14', '13', '14', '12', '12', '14', '21', '25', '31', '32', '5']  # creates a list of dish prices
print("Welcome to the Food-o-Matic, this program will create as many unique and delisious dishes as possible!")# prints a welcoming statement

while True:#creates an infinite loop
    num = input('How many dishes would you like(q for quit)?') # asks user how many dishes
    if num.lower() == 'q':  # if user types q then code ends
        sys.exit()#closes program
    else:#otherwise
        try:#except
            num = int(num) # sets a user response to a question
            if num <= 0:# if the user enters 0
                print("Why? Are you not hungry? These dishes were made espescially for you!")# prints what is inside 
            else:
                break#ends the code
        except ValueError:#does not fully go through the integer input
            print("Invalid input. Please enter an integer.")#prints the statment in the qoutes

print(f"Selecting {num} dishes for you!")#amount of dishes that were chosen printed out
for i in range(num):  # creates a for loop that will repeat for x time
    # sets the variable compType equal to a random choice form the list foodTypeCopy
    compMain = random.choice(mainDish)  # sets the variable compMain equal to a random choice form the list mainDishCopy
    # sets the variable compSide equal to a random choice form the list sideDishCopy
    print(f"{random.choice(foodType)} {compMain} {random.choice(sideDish)}. Your cost is ${dishPrice[mainDish.index(compMain)]}") # print the final dish to console and Prints the dish price to console


