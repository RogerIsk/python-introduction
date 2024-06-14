# Task 1 - Write a function `list_sum(lst)` that takes a list of numbers as input and returns the sum of all the numbers in the list.

print('\nTask 1')
numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)
    
def list_sum(lst):
    return sum(lst)
print(list_sum(numbers))

# Task 2 - Write a function `reverse_string(string)` that takes a string as input and returns the reversed string.

print('\nTask 2')
def reverse_string(string):
    return string[::-1]
print(reverse_string("Hello World"))

# Task 3 Write a function `factorial(n)` that takes a positive integer `n` as input and returns the factorial of `n`.

print('\nTask 3')
def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

# Task 4 - Write a function `fizzbuzz(n)` that takes a positive integer `n` as input and returns a string based on the following rules:
# - For numbers divisible by 3, print "Fizz" .
# - For numbers divisible by 5, print "Buzz" .
# - For numbers divisible by both 3 and 5, print "FizzBuzz" .
# - For all other numbers print the number

print('\nTask 4')
def fizzbuzz(n):
    if n <= 0:
        return 1
    elif n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 5 == 0 and n % 3 != 0:
        return "Buzz"
    elif n % 3 == 0 and n % 5 != 0:
        return "Fizz"
    else:
        return n
print(fizzbuzz(round(16,6)))

# Task 5 - Write a function `count_vowel(string)` that takes a string as input and returns the count of vowels (a, e, i, o, u) in the string.

print('\nTask 5')
def count_vowel(string):
    vowels = 'aeiou'
    count = 0
    for i in string:
        if i in vowels:
            count += 1
    return count
print(count_vowel("Hello World"))

# Task 6 - Write a function `calculator(num1, num2, operator)` that takes two numbers `num1` and `num2`, 
# and an operator (`+`, `-`, `*`, `/`) as input and returns the

print('\nTask 6')
def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return "Invalid Operator"
print(calculator(5, 6, '+'))
print(calculator(5, 6, '-'))
print(calculator(5, 6, '*'))
print(calculator(5, 6, '/'))

