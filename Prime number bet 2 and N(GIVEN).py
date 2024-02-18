N = int(input("Enter a number (N): "))


print("Prime numbers between 2 and", N, ":")
for num in range(2, N + 1):
    is_prime = True  # Assume the number is prime initially
    for i in range(2, num):
        if num % i == 0:
            is_prime = False  # If num is divisible by any number other than 1 and itself, it's not prime
            break
    if is_prime:
        print(num, end=" ")




