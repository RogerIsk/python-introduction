import random
from click import clear

clear() # i just want my screan to be clean when i run the code, without me doing anything, i hate when my screen is full of stuff, its hard to read



# Task 1 - write a Python program to calculate the sum of three integers given (prompted) by user.  
# If the values are equal then calculate triple value of their sum.  
# Print out an appropriate message to the user.

print("\n Task 1")
for i in range(3):
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))
    if a == b == c:
        print("The sum is: ", 3 * (a + b + c))
        break
    else:
        print("The sum is: ", a + b + c)
        break


# Task 2 - write a Python program to get the difference between a two given numbers (prompted by user).  
# If the first number is greater than second then calculate double difference between numbers.  
# Otherwise calculate the **absolute** difference between numbers.  
# Print out an appropriate message to the user.

print("\n Task 2")
for i in range(2):
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    if a > b:
        print("The difference is: ", 2 * (a - b))
        break
    else:
        print("The difference is: ", abs(a - b))
        break


# Task 3 - write a Python program to find whether a given number (prompted from the user) is even or odd.  
# Print out an appropriate message to the user.

print("\n Task 3")
for i in range(1):
    a = int(input("Enter a number: "))
    if a % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")



# Task 4 - write a Python program which accepts (prompts) the **float** radius of a circle 
# from the user and compute its area. Round the result to two decimals! Print out an appropriate message to the user.

print("\n Task 4")
for i in range(1):
    r = float(input("Enter the radius of the circle: "))
    area = 3.14159 * (r ** 2)
    print("The area of the circle is: ", round(area, 2))



# Task 5 - write a Python program to guess a number between 1 to 10.
print("\n Task 5")

for i in range(1):
    a = random.randint(1, 10)
    b = int(input("Guess a number between 1 and 10: "))
    if a == b:
        print("You guessed the number!")
    else:
        print("You didn't guess the number. The number was: ", a)



# Task 6 - write a Python program to convert temperatures to and from Celsius, Fahrenheit.
# In the centigrade scale, which is also called the Celsius scale, water freezes at 0 degrees and boils at 100 degrees.  
# In the Fahrenheit scale, water freezes at 32 degrees and boils at 212 degrees. 

print("\n Task 6")
temp = float(input("Enter the temperature: "))
scale = input("Enter which scale of temperature (C for Celsius, F for Fahrenheit): ")
if scale == "C":
    f = (temp * 9 / 5) + 32
    print("The temperature in Fahrenheit is: ", "%.2f" % f)
elif scale == "F":
    c = (temp - 32) * 5 / 9
    print("The temperature in Celsius is: ", "%.2f" % c)



# Task 7 - Your task is to write a Python program to construct the following pattern. 
# Upper part should be done **in one line** of code without using a loop.  
# Lower part can be done with any kind of loop **or** also with one line of code and without loops.

# only with 1 line of code
print("\n Task 7 - 1/4")
print(1*'*' + '\n' + 2*'*' + '\n' + 3*'*' + '\n' + 4*'*' + '\n' + 5*'*' + '\n' + 4*'*' + '\n' + 3*'*' + '\n' + 2*'*' + '\n' + 1*'*')

print("\n Task 7 - 2/4")
print('*' + '\n' + '**' + '\n' + '***' + '\n' + '****' + '\n' + '*****' + '\n' + '****' + '\n' + '***' + '\n' + '**' + '\n' + '*')

#only with loops
print("\n Task 7 - 3/4")
for i in range(5):
    print("*" * (i + 1))
for i in range(4):
    print("*" * (4 - i))    

print("\n Task 7 - 4/4")
print(1*'*' + '\n' + 2*'*' + '\n' + 3*'*' + '\n' + 4*'*' + '\n' + 5*'*') # upper part - only 1 line of code
for i in range(4): print("*" * (4 - i)) # lower part with a loop and with only 1 line of code 
    

# Task 8 - write a Python program to get the Fibonacci series between 0 to 50.  
# Note: The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....  
# Every next number is found by adding up the two numbers before it.  
# Hint: There are few ways to do this task. You can use for example while loop and variable swapping.

print("\n Task 8")
a = 0
b = 1
fibonacci_sequence = []
while a <= 50:
    fibonacci_sequence.append(a)
    a, b = b , a + b 
print("The Fibonacci sequence between 0 and 50 is:", fibonacci_sequence)

# this is the only way to write a Fibonacci sequence. If I write the same code but with a = b and b = a + b separately it will not work
# It will just keep adding the value of b to itself resulting in 0/1/2/4/8/16/32
# this was the most complicated thing for me to understand. I had to write it down on a separate notepad app to understand it.
# this is how i understand this code: we simoltaneously assign the old value of b to a and the sum of the old values of a and b to b
# we have to do this at the same time because if we do one of them first on its own, the value will become new 
# and the next variable will take the new value instead of the old value, the only way to take the old values together is to assign them at the same time
# this code is pretty weird and complicated, there has to be a simpler way...