import os # import os module to use system commands. this is the second library that lets us clear the console screen.
os.system('clear') # clear the console

'''
    equal                     - ==
    not equal                 - !=
    greater than              - >
    less than                 - <
    greater than or equal to  - >=
    less than or equal to     - <=

    and, or, not -logical operators,
    
    None.
'''

# Task 1 - write a program which asks the user three times about two integer numbers to compare. 
# Hint: Use `while` loop to perform the same operation more than once!  
# Use both comparison and logical operators, for example use logical comparison between two or more comparion operators:  

#im not sure if i understood the task correctly but the code works
print("Task 1: ")

a = 0
while a < 3: 
    a += 1
    if a == 1:
        print("\nFirst comparison: ")
    elif a == 2:
        print("\nSecond comparison: ")
    else:
        print("\nThird comparison: ")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if num1 > 1000 and num2 < 1000 or num1 < 1000 and num2 > 1000:
        if num1 == num2:
            print("Both numbers are equal.")
            print('One of the numbers is greater than 1000')
        elif num1 != num2 and num1 > num2:
            print("Both numbers are not equal")
            print("and the first number is greater than the second number.")
            print('One of the numbers is greater than 1000')
        elif num1 != num2 and num1 < num2:
            print("Both numbers are not equal")
            print("and the second number is greater than the first number.")
            print('One of the numbers is greater than 1000')
    
    if num1 > 1000 and num2 > 1000:
        if num1 == num2:
            print("Both numbers are equal.")
            print('Both numbers are greater than 1000')
        elif num1 != num2 and num1 > num2:
            print("Both numbers are not equal")
            print("and the first number is greater than the second number.")
            print('Both numbers are greater than 1000')
        elif num1 != num2 and num1 < num2:
            print("Both numbers are not equal")
            print("and the second number is greater than first number.")
            print('Both numbers are greater than 1000')
    
    if num1 < 1000 and num2 < 1000:
        if num1 == num2:
            print("Both numbers are equal.")
            print("Both numbers are smaller than 1000")
        elif num1 != num2 and num1 > num2:
            print("Both numbers are not equal")
            print("and the first number is greater than the second number.")
            print("Both numbers are smaller than 1000")
        elif num1 != num2 and num1 < num2:
            print("Both numbers are not equal")
            print("and the second number is greater than the first number.")
            print("Both numbers are smaller than 1000")


# Task 2 - write a Python program to convert month name to a number of days.
# Hint: Print list of months at the beginning.
# User should be prompted to enter name of the month and the output should be the number of days in given month.

print("\nTask 2: ")
months_list = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print("\nList of months: \n" + ", ".join(months_list)) # i used join() to print the list of months without the brackets, commas and quotes, 
month = input("\nEnter the name of the month: (only small letters for simplicity) \n") #i added a comma and a space between the months to make it look good
print("Number of days : " + str(months_days[months_list.index(month)]))                