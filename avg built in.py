def calculate_average(numbers):
    if len(numbers) == 0:
        return 0  # Avoid division by zero for empty list
    
    total = sum(numbers)  # Calculate the sum of numbers using sum() function
    average = total / len(numbers)  # Calculate the average
    
    return average

# Example usage:
numbers_list = [10, 20, 30, 40, 50]
avg = calculate_average(numbers_list)
print("Average:", avg)