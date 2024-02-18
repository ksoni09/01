def fibonacci(limit):
    a, b = 0, 1
    fib_sequence = [a]
    while b <= limit:
        fib_sequence.append(b)
        a, b = b, a + b
    return fib_sequence

# Example usage
limit = int(input("Enter the limit for Fibonacci sequence: "))
result = fibonacci(limit)
print("Fibonacci sequence up to", limit, ":", result)
       


    
