# using library function

import math

def is_strong_number(num):
    # Convert number to string, find factorial of each digit, and sum them up
    digit_sum = sum(math.factorial(int(digit)) for digit in str(num))
    
    # Return True if the sum matches the original number
    return digit_sum == num

# Test the program
test_num = 145
if is_strong_number(test_num):
    print(f"{test_num} is a Strong Number!")
else:
    print(f"{test_num} is NOT a Strong Number.")


# without using import.math 
def get_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def check_strong(num):
    temp = num
    digit_sum = 0
    
    # Extract digits from right to left
    while temp > 0:
        digit = temp % 10          # Gets the last digit
        digit_sum += get_factorial(digit)
        temp = temp // 10         # Removes the last digit
        
    return digit_sum == num

# User Input Example
user_input = int(input("Enter a number to check: "))
if check_strong(user_input):
    print("Strong Number")
else:
    print("Not a Strong Number")
