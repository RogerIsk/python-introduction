# Task 1 - write a program which asks the user three times for a number. If the number is even print ‘Even number’, if else print ‘Odd number’.
for i in range(3):                          #asking the user 3 times
    number = int(input("Task 1: Enter number: "))
    if number % 2 == 0:                     #if the number could be divided by 2 and the remainder is 0 then it is an even number
        print("Even number")
    else:
        print("Odd number")



# Task 2 - write a program which asks the user three times for a number and prints the sum of those numbers.
sum = 0                                     #creating a variable to store the sum
for i in range(3):                          #asking the user 3 times
    number = int(input("Task 2: Enter number: "))
    sum = sum + number                       #adding the input number to the sum
print(sum)                                  #print out the sum
     



# Task 3 - write a program which asks the user five times for a number and prints the maximum of those numbers.
max_number = 0                              #creating a variable to store the maximum number
for i in range(5):
    number = int(input("Task 3: Enter number: ")) #asking the user to input a number
    if number > max_number:                 #checking if the input number is greater than the maximum number
        max_number = number                 #if it is then assign the input number to the maximum number
print(max_number)                           #print out the maximum number



# Task 4 - Write a program which asks the user for a number and then prints out a list of all the divisors of that number.
number = int(input("Task 2: Enter number: ")) #asking the user to input a number
divisors = []                               #creating a list to store the divisors
for i in range(1, number+1):                #looping through the range of 1 to the input number (if number is 50 then we will loop 50 times from 1 to 51)
    if number % i == 0:                     #checking if the input number could be divided by all numbers between 1 and the input number
        divisors.append(i)                  #add i to the divisors list
print(divisors)                             #print out the divisors list



# Task 5 write a program which asks the user for a number and prints if it is even and divisible by 3.
number = int(input("Task 5: Enter number: ")) #asking the user to input a number
for i in range(1, number+1):                #looping through the range of 1 to the input number (if number is 50 then we will loop 50 times from 1 to 51)
    if number % 2 == 0 and number % 3 == 0: #checking if the input number is even and divisible by 3
        print("The number is even and divisible by 3")
        break                               #break the loop if the condition is met
    else:
        print("The number is not good enough")
        break                               #break the loop if the condition is not met



# Task 6 - write a program which asks the user for a number and prints if a number is positive, odd and divisible by 7
number = int(input("Task 6: Enter number: ")) #asking the user to input a number
for i in range(1, number+1):                #looping through the range of 1 to the input number (if number is 50 then we will loop 50 times from 1 to 51)
    if number > 0 and number % 2 ==1 and number % 7 == 0: #checking if the input number is even and divisible by 3
        print("Your number is positive, odd and divisible by 7")
        break                               #break the loop if the condition is met
    else:
        break                               #break the loop if the condition is not met

    