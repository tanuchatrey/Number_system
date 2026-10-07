def hcf(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    max_num = max(a, b)

    while True:
        if max_num % a == 0 and max_num % b == 0:
            return max_num
        max_num += 1


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("HCF =", hcf(num1, num2))
print("LCM =", lcm(num1, num2))
