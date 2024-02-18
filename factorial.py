# Step 1: Take input from the user
num = int(input("Enter a number to calculate its factorial: "))

# Step 2: Initialize factorial variable and start loop
factorial = 1
for i in range(1, num + 1):
    factorial *= i

# Step 3: Print the factorial
print("Factorial of", num, ":", factorial)



    
