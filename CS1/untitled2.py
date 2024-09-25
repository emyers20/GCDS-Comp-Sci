# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 14:18:06 2024

@author: emyers26
"""

def message_finder(message, old_alphabet, new_alphabet):
    new_message = ""
    for m in message:
        for letter in old_alphabet:
            if m == letter:
                new_message += new_alphabet[old_alphabet.index(letter)]
    return new_message
def main():
    alphabet = list(" ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    secret_alphabet = list("!@#$%^&*()qwsdfghjklmnbvcxh")
    
    message = str.upper(input("Enter a message"))
    encrypt = str.lower(input("Encrypt or decrypt"))
    
    if encrypt == "encrypt":
        new_message = message_finder(message, alphabet, secret_alphabet)
    else:
        new_message =  message_finder(message, alphabet, secret_alphabet)
                    
    print(new_message)

main()