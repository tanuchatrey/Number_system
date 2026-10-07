def niven(n):
    temp = n
    sum_digits = 0

    while temp > 0:
        digit = temp % 10
        sum_digits = sum_digits + digit
        temp = temp // 10

    if n % sum_digits == 0:
        return True
    else:
        return False


n = int(input("Enter a number: "))

if niven(n):
    print(n, "is a Niven number")
else:
    print(n, "is not a Niven number")
