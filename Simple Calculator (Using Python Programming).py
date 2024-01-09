#Simple Calculator

num1=float(input("Enter the first number : "))
num2=float(input("Enter the second number : "))
choice=0
while choice <6:
    print("\n----------MENU----------\nChoose operation you want to perform:\n1 --> For Addition ('+')\n2 --> For Subtraction ('-')\n3 --> For Multiplication ('*')\n4 --> For Division ('/')\n5 --> To Exit\n")
    choice=int(input("Enter your choice : "))
    if choice== 1:
        print("Addition of the given two numbers is : ",num1+num2 )
    elif choice== 2:
        print("Substraction of the given two numbers is : ",num1-num2)
    elif choice== 3:
        print("Multiplication of the given two numbers is : ",num1*num2)
    elif choice== 4:
        print("Division of the given two numbers is : ",num1/num2)
    elif choice == 5:
        print("\nEXIT SUCCESSFUL\n")
        break
    elif choice == 0:
        print("Invalid Input")
        break
    else:
        print("Invalid Input...\n")
