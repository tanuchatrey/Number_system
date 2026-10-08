def print_prime_factors(n: int):
    # Handle the factor 2
    while n % 2 == 0:
        print(2, end=" ")
        n //= 2

    # Handle odd factors starting from 3 up to sqrt(n)
    i = 3
    while i * i <= n:
        while n % i == 0:
            print(i, end=" ")
            n //= i
        i += 2

    # If n is still greater than 2, then remaining n itself is a prime
    if n > 2:
        print(n, end=" ")


# Example usage:
if __name__ == "__main__":
    n = int(input("Enter N: "))
    print_prime_factors(n)
