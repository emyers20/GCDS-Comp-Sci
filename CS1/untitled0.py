# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 08:39:33 2024

@author: emyers26
"""
import random  # Imports random library

typeFood = ['local', 'roasted', 'grilled', 'garlic mashed', 'oven dried', 'spiced', 'stewed', 'assorted', 'iced', 'sliced', 'braised', 'free-range', 'baby', 'teripyaki glazed', 'steamed']  # A list full of ways food can be cooked
mainDish = ['cauliflower', 'tilapia fillet', 'pork loin', 'green beans', 'basmati rice', 'rainbow carrots', 'fingerling potatoes', 'three color squash', 'potatoes', 'eggplant', 'drumstick', 'short rib', 'duck breast', 'eye round of beef', 'baguette']  # A list of main dishes
sideDish = ['with fennel', 'gratin', 'bengali style', 'with peas', 'with balsamico', 'with garlic and olive oil', 'with pigeon peas', 'with minted yogurt', 'soup', 'chutney', 'salad', 'with tropical fruit salsa', 'over sticky rice', 'au jus']  # A list of sides to the main dishes
dishPrice = ['14', '23', '31', '16', '12', '14', '13', '14', '12', '12', '14', '21', '25', '31', '32', '5']  # creates a list of dish prices
print('Welcome to the Food-o-matic, this device will create as many health and unique dishes you wish!')  # prints a welcoming statement
while True:  # creates a infinite loop
    x = input('Home many dishes would you like(q for quit)?')  # sets a user response to a question equal to the variable x
    if x.isnumeric():  # if x is a number it will continue with the if statement
        print('Here are your dishes:')  # prints this statement to console
        typeFoodCopy = typeFood.copy()  # makes of copy of the list typeFood
        mainDishCopy = mainDish.copy()  # makes of copy of the list mainDish
        sideDishCopy = sideDish.copy()  # makes of copy of the list sideDish
        for i in range(int(x)):  # creates a for loop that will repeat for x time
            compType = random.choice(typeFoodCopy)  # sets the variable compType equal to a random choice form the list typeFoodCopy
            compMain = random.choice(mainDishCopy)  # sets the variable compMain equal to a random choice form the list mainDishCopy
            compSide = random.choice(sideDishCopy)  # sets the variable compSide equal to a random choice form the list sideDishCopy
            print(compType + ' ' + compMain + ' ' + compSide)  # print the final dish to console
            print(f'The price for this meal is: ${dishPrice[mainDish.index(compMain)]}')  # Prints the dish price to console
            typeFoodCopy.remove(compType)  # removes compType from the list typeFoodCopy
            mainDishCopy.remove(compMain)  # removes compMain from the list mainDishCopy
            sideDishCopy.remove(compSide)  # removes compSide from the list sideDishCopy
    elif x == 'q':  # if x is equal to q it ends the code
        break  # breaks the loop
    else:  # otherwise
        print('That is not a valid answer.')  # prints this statement to console
