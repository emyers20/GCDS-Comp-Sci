#Evan Myers
#Description: A program that allows the user to play tic tac toe with the user and tells you when they win
#Bugs: tie condition has issues
#Features: allows the user to randomly select their symbol
#Sources: Python For Everybody
#Log 1.0 inital release

import random                  #gives acsess to the random functions
box = [                         #assigns box to a list inside of a list to create a board
            [1,2,3],
            [4,5,6],
            [7,8,9]
]

def userWin(box, userSymbol): 
    '''
    Checks the board and determines if either user has gotten three in a row

    Args:
        box: the box that was determined above
        
        usersymbol: The option that the user picked

    Returns:
        returns which user wins
    
    
    '''
    #determing if the user has won
    if box[0][0] == box[0][1] == box[0][2]:
        print(f"{userSymbol} wins")
        exit()
    elif box[1][0] == box[1][1] == box[1][2]:
        print(f"{userSymbol} wins")
        exit()
    elif box[2][0] == box[2][1] == box[2][2]:
        print(f"{userSymbol} wins")
        exit()
    elif box[0][1] == box[1][1] == box[2][1]:
        print(f"{userSymbol} wins")
        exit()
    elif box[0][0] == box[1][0] == box[2][0]:
        print(f"{userSymbol} wins")
        exit()
    elif box[0][2] == box[1][2] == box[2][2]:
        print(f"{userSymbol} wins")
        exit()
    elif box[0][0] == box[1][1] == box[2][2]:
        print(f"{userSymbol} wins")
        exit()
    elif box[0][2] == box[1][1] == box[2][0]:
        print(f"{userSymbol} wins")
        exit()
def printBox(box):
 
    '''
    prints the box and puts spaces in between the numbers

    Args:
        box: passes the list of the numbers that is assigned to the box

    Returns:
        returns the  printed box
    
    
    '''   
#puts a space in between every colum and row to make the box more presentable
    for row in range(len(box)):
        for col in range(len(box[row])):
            print(box[row][col],end=" ")
        print("") 

print("Welcome to tic-tac-toe")          #prints whats inside the qoutations

while True:
    symbol = input(str.lower("Do you want to choose X or O or do you want to do a random? say: random or choose")) #asks the user which method they want to pick their symbol
    # allows the user to choose their symbol and pick either x or o 
    if symbol == 'choose':
        picks = input("Do you want x or o")
        if picks == 'o':
            userSymbol = 'o' 
            break
        elif picks == 'x':
            userSymbol = 'x'
            break
        else:
            print("not an option")
            
    #allows the user to get a random x or o symbol       
    elif symbol == 'random':
        symbols = ['x','o']
        userSymbol = random.choice(symbols)
        break
        
    else:
        ("Not a option")

printBox(box)      # returns the presentable box
     
    



turn = random.choice([True,False])       # assigns the random turn to turn
count = 0        # assigns the variable count to 0

print(f"Your are {userSymbol}")               # tells the user what their symbol is
while count<= 9:             #a loop that runs while there has been under 9 turns 
    # if the turn is equal to the user's turn
    if turn is True: 
        print("Your turn")
        
        while True:
            userChoice = input(" Choose your move then I will go: ")
            # adds the users input into the desired place on the board 
            if userChoice == "1" and box[0][0] == 1:
                box[0][0] = userSymbol
                break
            elif userChoice == "4" and box[1][0] == 4:
                box[1][0] = userSymbol
                break
            elif userChoice == "7" and box[2][0] == 7:
                box[2][0] = userSymbol
                break
            elif userChoice == "2" and box[0][1] == 2:
                box[0][1] = userSymbol
                break
            elif userChoice == "3" and box[0][2] == 3:
                box[0][2] = userSymbol
                break
            elif userChoice == "5" and box[1][1] == 5:
                box[1][1] = userSymbol
                break
            elif userChoice == "8" and box[2][1] == 8:
                box[2][1] = userSymbol
                break
            elif userChoice == "9" and box[2][2] == 9:
                box[2][2] = userSymbol
                break
            elif userChoice == "6" and box[1][2] == 6:
                box[1][2] = userSymbol
                break
                    
            else:
                print("Not one of the options, silly!") 
                
         
        printBox(box)       # prints the box
        
        userWin(box, userSymbol)      # checks if either of the users have won and prints who won
        input("Lets Breath: ")       # puts a pause in the code before moving on
        count +=1      # adds a turn to count
        turn = False    #switches the turn to the computer 
        
        
    else:
        while True:
            print("ok its my turn: ")      
            userChoices = random.randint(1,9)     # has the computer choose a number 1-9
            # determines which symbol the computer is based off of the user symbol
            if userSymbol =="o":
                compChoice = "x"
            else:
                compChoice = "o"
            #adds the computer's inpput to the tic tac toe board
            if userChoices == 1 and box[0][0] == 1:
                box[0][0] = compChoice
                break
            elif userChoices == 4 and box[1][0] == 4:
                box[1][0] = compChoice
                break
            elif userChoices == 7 and box[2][0] == 7:
                box[2][0] = compChoice
                break
            elif userChoices == 2 and box[0][1] == 2:
                box[0][1] = compChoice
                break
            elif userChoices == 3 and box[0][2] == 3:
                box[0][2] = compChoice
                break
            elif userChoices == 5 and box[1][1] == 5:
                box[1][1] = compChoice
                break
            elif userChoices == 8 and box[2][1] == 8:
                box[2][1] = compChoice
                break
            elif userChoices == 9 and box[2][2] == 9:
                box[2][2] = compChoice
                break
            elif userChoices == 6 and box[1][2] == 6:
                box[1][2] = compChoice
                break
                    
            else:
                print("Not one of the options, silly!") 
        printBox(box)     # prints the box
        userWin(box, userSymbol)      #checks if the user has won
        count +=1 # adds a count to the turn
        turn = True   #switches the turn to the user
# if the amount of turns equals nine and nobody has won then they have tied
if count == 9:
    print(" The game is tied")
        
    


            










