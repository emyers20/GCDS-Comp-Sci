# -*- coding: utf-8 -*-
"""
Created on Wed May  1 10:53:53 2024

@author: emyers26

"""



#Author: Evan Myers
#Date: 5/13/24
#Challenges:  number 1, number 2, number 3
#Bugs: none
#Sources: Ms. Marciano
#Description:Interactive program which asks user about their websites and their usernames and passwords
import random#imports random library

def add_entry(webs, pswds, usernames):#sets add entry fucntion equal to these parameter
  while True:#infinite loopp while true=true
    webs.append(input("Enter a Website: "))#asks user to enter the variable then adds the answer to the list
    usernames.append(input("Enter a Username: "))#asks user to enter the variable then adds the answer to the list
    
    pswds.append(input("Enter a Password: "))#asks user to enter the variable then adds the answer to the list
    
    
    keep_going = str.lower(input("Do you want to do another website? "))#asks user what is inside presented print statement
    if keep_going == 'no':# ends loop based on the answer
        break#ends loop
def main():#sets main function
    webs = []#empty list 
    pswds = []#empty list 
    usernames = []#empty list 
    
    add_entry(webs, pswds, usernames)#adds paremeters to function
    
    while True:#infinite loop while true is true
        mode = input('''What mode would you like to do?(write a number one thorugh four)
    0. End program
    1. Print all Entries
    2. Print specfic website
    3. Generate a new secure password 
    4. Change username or password
    5. Add another password
    ''')#asks user what is inside presented print statement
        if mode == '1':#if user enters this number
            for i in range(len(webs)):#for loop that looks through webs
                print(f"website {webs[i]}, passwords {pswds[i]}, usernames {usernames[i]}")#takes all of the entries and presents them
        elif mode == '2':#if user enters this number
            website_lookup = input("Which website do you want to lookup the password for?\n")  # Prints this statement to console
        
            if website_lookup in webs:  # checks if the variable "websiteLookup" is in the list 'webs'
                index = webs.index(website_lookup) # find the index value of 'websiteToLookup' in the list 'webs' and sets that equal to the varaible index
                print("The username for " + website_lookup + " is " + usernames[index] + " and the password is " + pswds[index])  # Prints this statement to console
            else: # otherwise
                print("Sorry, that website was not found.")  # Prints this statement to console 
            
        elif mode == '3':#if user enters this number
           pswd = list()#sets variable to an empty list
           digits = list("0123456789")#sets digits to this list
           letters = "abcdefghijklmnop"#sets letters to this list
           special_ch = list("!@#$%^&*()/<>")#sets specitla ch to this list
           
           for i in range(3):#in the range of the prior variables that only takes 3 off of each
               strung = ""#sets this to an empty string
               pswd.append(random.choice(digits))#adds presented list to pswd and randomizes it
               pswd.append(random.choice(list(letters)))#adds presented list to pswd and randomizes it
               pswd.append(random.choice(list(letters.upper())))#adds presented list to pswd and randomizes it
               pswd.append(random.choice(special_ch))#adds presented list to pswd and randomizes it#adds presented list to pswd and randomizes it
           random.shuffle(pswd)#shuffles all of it
           empty = strung.join(pswd)#adds the empty string and takes the lists and puts it in there
           print(f"Your random password is: {empty}")#prints final password
           
        elif mode == '4':#if user enters this number
            user_or_pass = str.lower(input("Do you want to change a username or a password \n"))#asks user what is inside presented print statement
            
            if user_or_pass == 'username':# if user says they want to change their username
                
                web = str.lower(input("Which website do you want to change \n"))#asks them which website they want to change
                
                if web in webs:# if the website they chose is in the previous webs
                    usernames[webs.index(web)] = input(f"What do you want to change your {user_or_pass} to?\n")#adds their username to the privious entry            
            elif user_or_pass == 'password':# if user says they want to change their password
                web = str.lower(input("Which website do you want to change \n"))#asks them which website they want to change
                if web in webs:# if the website they chose is in the previous webs
                    pswds[webs.index(web)] = input(f"What do you want to change your {user_or_pass} to?\n") #adds their password to the privious entry                       
        elif mode == '5':#if user chooses this number
            add_entry(webs, pswds, usernames)#calls previous function
        elif mode == '0':# if user chooses this number
            break # end the loop    
                             
main()               
            
            