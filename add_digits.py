def add_dig(temp):
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum = sum + digit
        temp = temp // 10

    return(f"Sum of digits = {sum}")

num = int(input("Enter a number: "))
print(add_dig(num))
