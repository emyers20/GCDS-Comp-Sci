#Evan Myers
#Description: A program that allows the user to guess letters of a random word and ends the game after they lose all of their lives
#Bugs: User guess changes every iteration so if the user guesses the same letter twice it removes two lives instead of just one
#Features: allows word to be generated from a library
#Sources: Python For Everybody
#Log 1.0 inital release

# creates the random word library
import random_word


# Create an instance of the RandomWords class
rw = random_word.RandomWords()

# Generate a random word
random_word = rw.get_random_word()



def main():
  #introduces the game to the user
  print("Welcome to Hangman! A random word will be generated for you from our library, best of luck!")
    
  # assigns the starting amount of lives
  lives = 5
  #displays the starting hangman display
  display_hangman(5)
  display = ""
  #get the length of whatever the word is
  wordLength = len(list(random_word))
  #assign count to 0
  count = 0
  
  while count < wordLength:
    # iterates through each letter in the random word and puts a blank down for each space
    display = display +'_'
    count +=1
  
  
  while lives > 0:
      
      #ask the user for their guess
      userGuess = input("Enter a letter that you want to guess: ").lower()
             
      #if the user guess is anything but a letter than it asks again 
      if not userGuess.isalpha():               
        print("Please type letters only ")
        continue
      # if the guess is incorrect then the user looses a life and it gets displayed
      if userGuess not in str(random_word):
         print("You guessed incorrectly ")
        
         lives = lives - 1
         display_hangman(lives)
      # if the user guess is correct than it calls the fuction display to show the correct letter in the blanks spaces 
      if userGuess in str(random_word):
        print("good guess!")
        display = displayBoard(random_word, userGuess, display)
        #once there is no _ left than the uesr wins 
        if "_" not in display:
            print(f"You win, you had {lives} lives left!")
            break
        
        
              
      
  # if the lives reach zero than the user looses   
  if lives == 0:
    print(f"YOU LOSE, the word was:{random_word}")
    
  

      
def displayBoard(word,userGuess, display):
    '''
    Takes the random word and the user guess to place the user guess into the coreect blank spot then display it
    Args:
        Word: is the random word that is turned into a list
        
        userGuess: the letter that the user guessed
        
        Display: the amount of blanks that is used to place the correct letters

    Returns:
        returns the updated display
    
    
    '''
    display = list(display)
    #every figure in the random word check if that spot equals the user guess and if it does place the user guess onto the display
    for i in range(len(random_word)):
        word = list(random_word)
        if word[i] == userGuess:
          
            display[i] = userGuess
          
   
      
    #removes unnesecary qotes and commas from display and then prints it
    display = "".join(display) 
    print(str(display))
    return display
    
def display_hangman(lives):
    '''
    Prints a specific stage of the hangman depending on the amount of lives
    Args:
        Lives: the amount of times the user has gotten the guess wrong starting from 5 and going to 0
    Returns:
        returns the specific stage figure in the list
    
    
    '''
    stages = [
        """
          --------
          |      |
          |      O
          |     \|/
          |      |
          |     / \\
          -
        """,
        """
          --------
          |      |
          |      O
          |     \|/
          |      |
          |     /
          -
        """,
        """
          --------
          |      |
          |      O
          |     \|/
          |      
          |      
          -
        """,
        """
          --------
          |      |
          |      O
          |     \|
          |      
          |     
          -
        """,

        """
          --------
          |      |
          |      O
          |    
          |      
          |     
          -
        """,
        """
          --------
          |      |
          |      
          |    
          |      
          |     
          -
        """
    ]
    #prints the specific stage based on the amount of lives left
    print(stages[lives])

   
main()