import math

'''TASK 1'''
# Rounding
num1 = 3.14159
result = round(num1, 2)
print(result)  # Output: 3.14
num2 = 5.6789
result = round(num2, 1)
print(result)  # Output: 5.7

# Addition
num3 = 10
num4 = 3.5
result = num3 + num4
print(result)  # Output: 13.5
num5 = 2 + 3j
num6 = 1 + 2j
result = num5 + num6
print(result)  # Output: (3+5j)

# Subtraction
num7 = 8.5
num8 = 3
result = num7 - num8
print(result)  # Output: 5.5
num9 = 2 + 3j
num10 = 1 + 2j
result = num9 - num10
print(result)  # Output: (1+1j)

# Multiplication
num11 = 4.5
num12 = 2
result = num11 * num12
print(result)  # Output: 9.0
num13 = 2 + 3j
num14 = 1 + 2j
result = num13 * num14
print(result)  # Output: (-4+7j)

# Division
num15 = 10
num16 = 3
result = num15 / num16
print(result)  # Output: 3.3333333333333335
num17 = 7.5
num18 = 2.5
result = num17 / num18
print(result)  # Output: 3.0

# Modulo
num19 = 10
num20 = 3
result = num19 % num20
print(result)  # Output: 1
num21 = 7.5
num22 = 2.5
result = num21 % num22
print(result)  # Output: 0.0

# Exponentiation
num23 = 2
num24 = 3.5
result = num23 ** num24
print(result)  # Output: 11.313708498984761
num25 = 2.5
num26 = 2
result = num25 ** num26
print(result)  # Output: 6.25

# Floor Division
num27 = 10
num28 = 3
result = num27 // num28
print(result)  # Output: 3
num29 = 7.5
num30 = 2.5
result = num29 // num30
print(result)  # Output: 3.0

# Booleans
bool1 = True
bool2 = False
result = bool1 and bool2
print(result)  # Output: False
bool3 = True
bool4 = True
result = bool3 or bool4
print(result)  # Output: True

math_variable = 4 + 5 / 2 * 3
print(round(math_variable, 3))  # Output: 11.5


'''TASK 2'''
# Maximum
result = max(2, 2.0, -0.5)
print(result)  # Output: 2
result = max(23, 22, 55.0)
print(result)  # Output: 55.0

# Minimum
result = min(2, 2.0, -0.5)
print(result)  # Output: -0.5
result = min(23, 22, 55.0)
print(result)  # Output: 22

# Absolute
result = abs(-34.23)
print(result)  # Output: 34.23
result = abs(4 - 3j)
print(result)  # Output: 5.0

# Power
result = pow(3, 4)
print(result)  # Output: 81
result = pow(2.5, 2)
print(result)  # Output: 6.25

# Ceiling
result = math.ceil(34/5)
print(result)  # Output: 7
result = math.ceil(7.5/2.5)
print(result)  # Output: 3

# Floor
result = math.floor(34/5)
print(result)  # Output: 6
result = math.floor(7.5/2.5)
print(result)  # Output: 3

# Maximum (Boolean)
result = max(True, False)
print(result)  # Output: True
result = max(False, True)
print(result)  # Output: True