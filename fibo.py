def fibonacci(n):
    """Generate a list containing the Fibonacci series up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    series = [0, 1]
    for _ in range(2, n):
        series.append(series[-1] + series[-2])
    return series


# Example usage:
num_terms = 10
print(f"Fibonacci series ({num_terms} terms): {fibonacci(num_terms)}")
