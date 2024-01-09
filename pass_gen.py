import string
import random
 

length = int(input("Enter password length: "))
 
print('''Choose what you desire for password from these : 
         1. Digits/Numbers
         2. Charachters
         3. Symbols
         4. Press 4 after all above desired choices are chosen''') 
 
pwd = ""

while(True):
    choice = int(input("Pick a number "))
    if(choice == 1):
        pwd += string.ascii_letters
    elif(choice == 2):
        pwd += string.digits
    elif(choice == 3):
        pwd += string.punctuation
    elif(choice == 4):
        break
    else:
        print("Please pick a valid option!")

password = []

for i in range(length):
    randomchar = random.choice(pwd)
    password.append(randomchar)

print("The random password is " + "".join(password))