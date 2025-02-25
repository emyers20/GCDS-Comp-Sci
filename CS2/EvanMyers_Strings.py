#Evan Myers
#Description: This program allows the user to enter their name and alter it in many diffent ways
#Bugs: none
#Features: Number 12 bonus, Number 14 bonus, Build a menu bonus, ask user if they want to change their name
#Sources: Python For Everybody
#Log 1.0 inital release
def vowel_count(user_string): 
    '''
    Takes the user input and determines the amount vowels in it  
    Args:
        user_string: This where the user inputs their name
    Returns:
        returns the vowel count
     
    '''
    vcount = 0
    vowel = list("aeiouAEIOU")
    # iterates through every letter and check if there is a vowel
    for alphabet in user_string:
        if alphabet in vowel:
            vcount = vcount + 1
    return vcount
def consonant_count(user_string): 
    '''
    Takes the user input and determines the amount consonants in it  
    Args:
        user_string: This where the user inputs their name
    Returns:
        returns the vowel count
     
    '''
    ccount = 0
    consonant = list("qQwWrRtTyYpPlLkKjJhHgGfFdDsSzZxXcCvVbBnNmM")
    # iterates through the string and checks the amount of consonants
    for alphabet in user_string:
        if alphabet in consonant:
            ccount = ccount + 1
    return ccount
def lower(userInput):
    '''
    Takes the user input and makes it into lowercase  
    Args:
        userInput: This where the user inputs their name
    Returns:
        returns the lowercase version of the userinput
     
    '''
    lowercase = ""
    # Iterates through the input and makes it lowercase
    for char in userInput:
        if 'A' <= char <= 'Z':
            lowercase += chr(ord(char) + 32)                        #makes the character lowercase by using the ordinal chart
        else:
            lowercase += char
    return lowercase
def upper(userInput):
    '''
    Takes the user input and makes it all uppercase  
    Args:
        userInput: This where the user inputs their name
    Returns:
        returns the uppercase words
     
    '''
    uppercase = ""
    #iterates through the user input and makes it uppercase
    for char in userInput:
        if 'a' <= char <= 'z':
            uppercase += chr(ord(char) - 32)                        # makes the character uppercase by using the ordinal chart
        else:
            uppercase += char
    return uppercase
def shuffler(userInput):
    '''
    Takes the user input and randomizes its contents  
    Args:
        userInput: This where the user inputs their name
    Returns:
        returns the uppercase words
     
    '''
    import random
    shuffle = ""
    index = [i for i in range(len(userInput))]
    # while the the index is being iterated through, it will swith aound the letter and make it appear in a diffrent positon
    while index:
        indexRandom = random.randint(0, len(index) - 1)
        poppedIndex = index.pop(indexRandom)
        shuffle += userInput[poppedIndex]
    return shuffle
def Palindrome(userInput): 
    '''
    Takes the user input and checks if the reverse is the same as the orgianl
    Args:
        userInput: This where the user inputs their name
    Returns:
        returns true or false based on weather it is a palindrome
     
    '''
    palindromeCheck = True
    #Checks if the userinput in reverse is the same as it in orginal 
    if(userInput == userInput[::-1]): 
        return palindromeCheck
    else: 
        palindromeCheck = False
        return palindromeCheck
def array(userInput):
    '''
    Takes the user inputs and sorts the contents by character 
    Args:
        userInput: This where the user inputs their name
    Returns:
        returns the sorted array
     
    '''
    sortedList = list(userInput)
    # itterates through the input and arrages the contents in order by aphalbetical order and freqency also the start of every word
    for i in range(len(sortedList)):
        if i != " ":
            for j in range(i + 1, len(sortedList)):
                if sortedList[i] > sortedList[j]:
                    sortedList[i], sortedList[j] = sortedList[j], sortedList[i]
        

    sortedstring = ''.join(sortedList)
    return(sortedstring)
def findTitle(userInput):
    '''
    Takes the user input and determines if it contains a title
    Args:
        userInput: This where the user inputs their name
    Returns:
        returns true or false 
     
    '''
    titles = ["Mr.", "Ms.", "Mrs.", "Dr.", "Prof.", "Sir", "Lady", "Esq", "Caesar", "Elector"]
    # checks if the input has any of the tittles list inside of it
    for title in titles:
        if title in userInput:
            return True
        else:
            return False        
def main():
    userInput = input("Type out  your first, middle, and last name: ")   #asks the user for their name
    changeName = ""
    #asks the user for their choice of things they can do to their name in a loop untill they with to exit
    while True:
        print("1. Reverse and display")
        print("2. Determine the number of vowels. You can prompt user for a particular vowel or create subtotals of each.")
        print("3. Consonant frequency. Bonus: Subtotals of each consonant")
        print("4. Return first name.")
        print("5. Return last name.")
        print("6. Return middle name(s)")
        print("7. Return boolean if last name contains a hyphen")
        print("8. Function to convert to lowercase")
        print("9. Function to convert to uppercase")
        print("10. Modify array to create a random name (mix up letters)")
        print("11. Return boolean if first name is a palindrome")
        print("12. Return full-name as a sorted array of characters (Bonus)")
        print("13. Make initials from name")
        print("14. Return boolean if name contains a title/distinction")
        print("Type 15. if you want to exit")

        userPick  = input("Okay, now pick one of these options by entering a number(1-15):  ")
        #reverses the userinput if the user picks the 1
        if userPick == "1":
            reverse = userInput[::-1]
            print(reverse)
        #if the user picks 2  it callse the vowel count function and prints it
        elif userPick == "2":
            vcount = vowel_count(userInput)
            print("number of vowels: ", vcount)
        #if the user picks 3  it callse the consonant count function and prints it
        elif userPick == "3":
            ccount = consonant_count(userInput)
            print("number of consonants:", ccount)

        #if the user picks 4 it returns the first words 
        elif userPick == "4":
            split_func = userInput.split(" ")
            print(split_func[0])
         #if the user picks 5  it returns the  last word  
        elif userPick == "5":
            split_func = userInput.split(" ")
            print(split_func[-1])
        #if the user picks 6 it returns whatever is in the between the last and the first
        elif userPick == "6":
            split_func = userInput.split(" ")
            print(' '.join((split_func[1: -1])))
        
         #if the user picks 7 then iterates through the input and checks if - is inside it then returns a boolean   
        elif userPick == "7":
            dash = False
            lastName = userInput.split(" ")
            hypLast = lastName[-1]
            for i in range(len(hypLast)):
                hyphen= list(hypLast)
                if hyphen[i] == "-":
                    dash = True
                    break
            print(dash)
         #if the user picks 8 then it calls the string lower funciton and prints it 
        elif userPick == "8":
            stringInput = userInput
            lowerString = lower(stringInput)
            print(lowerString)
         #if the user picks 9 then it calls the upperstring
            stringInput = userInput
            upperString = upper(stringInput)
            print(upperString)
         #if the user picks 10 then it calls the shuffler function and prints it   
        elif userPick == "10":
            stringInput = userInput
            shuffleYes = shuffler(stringInput)
            print(shuffleYes)
         #if the user picks 11 then it calls the palindrome funciton and prints it    
        elif userPick == "11":
            stringInput = userInput
            palindromeYes = Palindrome(stringInput)
            print(palindromeYes)
         #if the user picks 12 then it calls the array funciton and prints it    
        elif userPick == "12":
            stringInput = userInput
            arrayYes = array(stringInput)
            print(arrayYes)
         #if the user picks 13 then it gets the first letter of each word and joins it using "." then prints it    
        elif userPick == "13":
            segment = userInput.split()
            initials = " ".join([segment[0] + "." for segment in segment[:-1]]) + " " + segment[-1][0]
            print(initials)
         #if the user picks 14 then it calls the findTitle funciton and prints it    
        elif userPick == "14":
            stringInput = userInput
            titleYes = findTitle(stringInput)
            print(titleYes)
        #if the user wants to end to end the code
        elif userPick == "15":
            print("GoodBye")
            quit()
                
        else:
            print("Invalid, put something else") 
            continue
        # if the user wants to change their name it will restart the code but if the user does not then it will go back to a specific part of the code
        while True:
            changeName = input("do you want to change your name?")
            changeName = lower(changeName)
            if changeName == "yes":
                main()
            elif changeName == "no":
                break
            else: 
                print("Invalid")
            
main()
        

        



