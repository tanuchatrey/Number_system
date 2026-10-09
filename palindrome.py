def is_palindrome(n):
    """Check if a number is a palindrome using string conversion."""
    # Negative numbers are not palindromes (e.g., -121 reversed is 121-)
    if n < 0:
        return False

    s = str(n)
    return s == s[::-1]


num = int(input("enter number:"))
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
