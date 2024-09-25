"""
Created on Mon Apr  8 10:56:03 2024

@author: emyers26
CHALLENGE--created background of "in" functionality
    for item in my_list:
        if item == element:
            return True
        else:
            return False

    if "-" in number:
        number = number[1:]
    if number.isnumeric():
        return True
    else:
        return False
    

"""


#Author: Evan Myers
#Date: 4/18/24
#Challenges:  initals, reoginize functions, alternative for one of the functions above
#Bugs: none
#Sources: Ms. Marciano,https://www.w3schools.com/python/ref_string_split.asp
#Description:Interactive program which executes written functions that complete various tasks
import random#imports random library


def singsong():#defines function with parameters
    print("Hey")#prints what ever is within parenthesses 
    print("hi")#prints what ever is within parenthesses 


def add(num1, num2):#defines function with parameters
    print(num1 + num2)#adds both variables 


def print_list(list_to_print):#defines function with parameters
    for element in list_to_print:#takes an element from the list and print it vertaclly 
        print(element)#prints the element


def contains_element(my_list, element):#defines function with parameters
    if element in my_list:#asks if the element is in the my list
        return True#prints true
    else:#otherwise
        return False#prints false


def get_integer(order):#defines function with parameters
    while True:#loop if true is ture
        try:#try what is under this 
            number = int(input(f"Enter the {order} number: "))#checks if the number is an integer
            return number#returns the number
        except ValueError:#if try is not satified 
            print("Please enter an integer!")#print what is whithin the qoutes


def random_number():#defines function with parameters
    number1 = get_integer("lower boundary")#setting varibale to what is within the parenthenses 
    number2 = get_integer("upper boundary")#setting varibale to what is within the parenthenses 
    print(random.randint(number1, number2))#picks random number in between number1 and number2
def name():#defines function with parameters
    nameI = input("please enter your first and last name")#prints what ever is within parenthesses 
    nameR = nameI.split(' ')#turns name into list
    initials = ""#creates empty string
    for n in nameR:#gets first character of the list
        initials += n[0]#gets first character of the list
    print(f"Your initals are:{initials}")#prints what ever is within parenthesses 
   


def main():#defines function with parameters
    singsong()#calls function
    singsong()#calls function
    singsong()#calls function
    singsong()#calls function
    foods = ["pizza", "corn", "meat", [4, 3, 5]]#created the list of foods
    print_list(foods)#calls function
    numbers = ["six", "one", "three"]#creates list of numbers
    check = str.lower(input("What element do you want to look for: "))#prints what ever is within parenthesses 
    print(contains_element(numbers, check))#calls contains element function with those parameters
    num1 = get_integer("first")#replaces the previous Enter the blank number with what is inside the qoutes
    num2 = get_integer("Second")#replaces the previous Enter the blank number with what is inside the qoutes
    add(num1, num2)#adds two numbers
    random_number()#calls function
    name()#calls function


main()#calls function
