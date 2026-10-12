# using string 

def is_harshad_string(num):
    # Calculate sum of digits by converting to string
    digit_sum = sum(int(digit) for digit in str(num))
    
    # Check if original number is divisible by the sum
    return num % digit_sum == 0

# Example usage
number = 18
if is_harshad_string(number):
    print(f"{number} is a Harshad number.")
else:
    print(f"{number} is not a Harshad number.")

#using loops

def is_harshad_math(num):
    temp = num
    digit_sum = 0
    
    # Extract digits arithmetically
    while temp > 0:
        digit_sum += temp % 10  # Get the last digit
        temp //= 10             # Remove the last digit
        
    # Check divisibility
    return num % digit_sum == 0

# Example usage
number = 21
print(is_harshad_math(number))  # Returns True (21 is divisible by 2 + 1 = 3)
