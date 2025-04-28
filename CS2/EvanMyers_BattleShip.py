#Evan Myers
#Description: A program that allows user to play Battle ship against the Computer
#Bugs: 
#Features: has emojis in the board, randomly selects who goes first, User or computer can go again if they guess a ship
#Sources: Python For Everybody
#Log 1.0 inital release

import random
import sys

def printBoard(board):
    '''
    prints the board in a clear manner that is easy to use
    Args:
        board: passes the boar variable into the print board function

    Returns:
        returns the printed box
    
    
    '''   
    #puts a space in between every colum and row to make the box more presentable
    for row in range(len(board)):
        for col in range(len(board[row])):
            print(board[row][col],end=" ")
        print("") 
def AddShips(board2):
      '''
    Adds ships to the both the user and computer board before code starts
    Args:
        board2: allows you to use the funciton with any board
    Returns:
        returns the board with 5 ships randomly placed
    
    
    '''  
      counter = 0 
      #while the ships placed is less than 5, add ships on random places on the board  and if a ship is already there pick another spot
      while counter < 5:
         
         row = random.randint(0,9)
         col = random.randint(0,9)
         if row % 2 == 1 and col % 2 == 1:
            
            board2[row][col] = "🚢"
            counter +=1
            
            if board2[row][col] == "🚢":
               continue
            else:
               board2[row][col] = "🚢" 
               counter +=1

def get_coordinates(user_guess):
     '''
    gets the coordinates of whatever the user or compurter guesses
    Args:
        user_guess: passes in user_guess so that it can be converted
    Returns:
        returns the coordinate equivilant to the printed version
    
    
     ''' 
     #iterates through every possible input then converts it to something the code can read
     if user_guess == "A1":
        return 1,1
     elif user_guess == "A2":
        return 1,3
     elif user_guess == "A3":
        return 1,5
     elif user_guess == "A4":
        return 1,7
     elif user_guess == "A5":
        return 1,9
     elif user_guess == "B1":
        return 3,1
     elif user_guess == "B2":
        return 3,3
     elif user_guess == "B3":
        return 3,5
     elif user_guess == "B4":
        return 3,7
     elif user_guess == "B5":
        return 3,9
     elif user_guess == "C1":
        return 5,1
     elif user_guess == "C2":
        return 5,3
     elif user_guess == "C3":
        return 5,5
     elif user_guess == "C4":
        return 5,7
     elif user_guess == "C5":
        return 5,9
     elif user_guess == "D1":
        return 7,1
     elif user_guess == "D2":
        return 7,3
     elif user_guess == "D3":
        return 7,5
     elif user_guess == "D4":
        return 7,7
     elif user_guess == "D5":
        return 7,9
     elif user_guess == "E1":
        return 9,1
     elif user_guess == "E2":
        return 9,3
     elif user_guess == "E3":
        return 9,5
     elif user_guess == "E4":
        return 9,7
     elif user_guess == "E5":
        return 9,9
    
def main():
    #four boards that make the spaces that the user and computers guess from
    UserGuessBoard = [
                ['----1----2----3---4----5---'],
                ['A|',"🌊",'|', "🌊", '|',  "🌊", '|', "🌊", '|', "🌊",'|'],
                ['--------------------------'],
                ['B|',"🌊",'|', "🌊", '|',  "🌊", '|', "🌊", '|', "🌊",'|'],
                ['--------------------------'],
                ['C|',"🌊",'|', "🌊", '|',  "🌊", '|', "🌊", '|', "🌊",'|'],
                ['--------------------------'],
                ['D|',"🌊",'|', "🌊", '|',  "🌊", '|', "🌊", '|', "🌊",'|'],
                ['--------------------------'],
                ['E|',"🌊",'|', "🌊", '|',  "🌊", '|', "🌊", '|', "🌊",'|'],
                ['--------------------------'],
                                    ]
    ComputerDefenseBoard = [
                ['----1----2----3---4----5---'],
                ['A|',"🌊",'|', "🌊", '|',  "🌊", '|', "🌊", '|', "🌊",'|'],
                ['--------------------------'],
                ['B|',"🌊",'|', "🌊", '|',  "🌊", '|', "🌊", '|', "🌊",'|'],
                ['--------------------------'],
                ['C|',"🌊",'|', "🌊", '|',  "🌊", '|', "🌊", '|', "🌊",'|'],
                ['--------------------------'],
                ['D|',"🌊",'|', "🌊", '|',  "🌊", '|', "🌊", '|', "🌊",'|'],
                ['--------------------------'],
                ['E|',"🌊",'|', "🌊", '|',  "🌊", '|', "🌊", '|', "🌊",'|'],
                ['--------------------------'],
        ]
    ComputerGuessBoard = [
                ['----1----2----3---4----5---'],
                ['A|',"🌊",'|', "🌊", '|',  "🌊", '|', "🌊", '|', "🌊",'|'],
                ['--------------------------'],
                ['B|',"🌊",'|', "🌊", '|',  "🌊", '|', "🌊", '|', "🌊",'|'],
                ['--------------------------'],
                ['C|',"🌊",'|', "🌊", '|',  "🌊", '|', "🌊", '|', "🌊",'|'],
                ['--------------------------'],
                ['D|',"🌊", '|', "🌊", '|',  "🌊", '|', "🌊", '|', "🌊",'|'],
                ['--------------------------'],
                ['E|',"🌊",'|', "🌊", '|',  "🌊", '|', "🌊", '|', "🌊",'|'],
                ['--------------------------'],
        ]
    UserDefenseBoard = [
                ['----1----2----3---4----5---'],
                ['A|',"🌊",'|', "🌊", '|',  "🌊", '|', "🌊", '|', "🌊",'|'],
                ['--------------------------'],
                ['B|',"🌊",'|', "🌊", '|',  "🌊", '|', "🌊", '|', "🌊",'|'],
                ['--------------------------'],
                ['C|',"🌊",'|', "🌊", '|',  "🌊", '|', "🌊", '|', "🌊",'|'],
                ['--------------------------'],
                ['D|',"🌊", '|', "🌊", '|',  "🌊", '|', "🌊", '|', "🌊",'|'],
                ['--------------------------'],
                ['E|',"🌊",'|', "🌊", '|',  "🌊", '|', "🌊", '|', "🌊",'|'],
                ['--------------------------'],
        ]
    AddShips(ComputerDefenseBoard)            #calls the computer defense board
    AddShips(UserDefenseBoard)                 #calls the user defense board
    print("Here is your inital board")
    printBoard(UserGuessBoard)               #prints the board using the printBoard funciton
    print("Welcome to Battleship\n") 
    print("To decide who goes first, it will be randomly decided\n")
    input("Lets Breath(Click enter to continue): ") # puts a pause in the code before moving on
    guesses_used = set()                            #puts the userguesses into a set to use later
    acceptableInputs = ["A1","A2","A3","A4", "A5", "B1", "B2", "B3", "B4", "B5", "C1", "C2", "C3", "C4", "C5", "D1", "D2", "D3", "D4", "D5", "E1", "E2", "E3", "E4", "E5"]              #list of acceptable inputs
   
    
    turn = random.choice([True,False])                     #picks True or False from a list
    compShipCount = 0                                      #sets the ship count to 0
    userShipCount = 0                                      #sets the ship count to 0
    
    while True:                     #while loop for game
         #if the turn is True, it iterates through the user's guess
         if turn is True:
            print("Lucky you, you get to go!")
            while True:             #keep going until valid input
                  user_guess = input("Choose a coordinate based on the board please. Example: A1 for the top-left space\n ").upper()
                  #checks if the user guess has been already used
                  if user_guess in guesses_used:
                     print("You already guessed that, please try again")
                     continue
                  guesses_used.add(user_guess)
                  # check if the user entered a correct guess
                  if user_guess in acceptableInputs:
                     row,col = get_coordinates(user_guess)
                     #Puts a x if the user missed a ship on the computer board
                     if ComputerDefenseBoard[row][col] == "🌊":
                              UserGuessBoard[row][col] = "🚫"
                              printBoard(UserGuessBoard)
                              turn = False
                              break
                     #Puts a bomb if the user guesss a ship and iterates through the win condition
                     elif ComputerDefenseBoard[row][col] == "🚢":
                              UserGuessBoard[row][col] = "💥"
                              compShipCount +=1
                              if compShipCount == 5:
                                 printBoard(UserGuessBoard)
                                 print("You win, you got all of my ships")
                                 sys.exit()
                              printBoard(UserGuessBoard)
                              print("This is your guess bord")
                  else:
                     print("Please type one of the coordinates")
                     input("Lets Breath(Click enter to continue): ") 
         
         if turn is False:
            #if the turn is False, it iterates through the computer's guess
            while True:
               print("I get to go, im excited!")
               #has the computer guess a random choice from the acceptable inputs
               compGuess = random.choice(acceptableInputs)
               print(f"I guess: {compGuess}")
               row,col = get_coordinates(compGuess)
               #makes sure the computer cannot guess it again
               if ComputerGuessBoard[row][col] != "🌊":
                  continue
               #Puts a x if the computer missed a ship on the user board
               if UserDefenseBoard[row][col] == "🌊":
                        ComputerGuessBoard[row][col] = "🚫"
                        printBoard(ComputerGuessBoard)
                        print("This is my updated Computer Board")
                        turn = True 
                        break  
                      
               #Puts a bomb if the computer guesss a ship and iterates through the win condition         
               elif UserDefenseBoard[row][col] == "🚢":
                        ComputerGuessBoard[row][col] = "💥"
                        userShipCount +=1
                        if userShipCount == 5:
                                 printBoard(ComputerGuessBoard)
                                 print("I win, I got all of your ships")
                                 sys.exit()
                        printBoard(ComputerGuessBoard)
                        print("This is my updated Computer Board")
               
        
        
    
    
    #user_guess = input("There is a battleship that you are trying to hit on the other side, Enter your guess for a  row and column ")
        
    
    


    
main()