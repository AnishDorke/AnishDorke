# Password Generator (Using Python Programming)

import random
import string

def generate_password(min_length, numbers=True, special_charachters=True):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijlmnopqrstuvwxyz"
    digits = "0123456789"
    special = "!@$%^&*()_-?/><.,~|\#+`"
    
    charachters = letters
    if numbers:
        charachters += digits
    if special_charachters:
        charachters += special

    pwd = ""
    meets_criteria = False
    has_numbers = False
    has_special =  False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(charachters)
        pwd += new_char

        if new_char in digits:
            has_numbers = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_numbers
        if special:
            meets_criteria = meets_criteria and has_special

    return pwd  



min_length = int(input("Enter the desired length of password: "))
has_numbers = input("Do you want digts to be included (y/n)? ")
has_special = input("Do you want special charachters to be included (y/n)? ")
pwd = generate_password(min_length,has_numbers,has_special)
print("The generated password is : ",pwd)