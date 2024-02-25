def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    number = int(input("Enter the number of terms in the Fibonacci sequence: "))
    
    if number <= 0:
        print("Please enter a positive integer.")
    else:
        print("Fibonacci sequence:")
        for i in range(number):
            print(fibonacci(i), end=" ")

main()