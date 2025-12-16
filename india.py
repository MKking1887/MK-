def calculate_sums(numbers):
    odd_sum = 0
    even_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return [odd_sum, even_sum]

# Example input
numbers = [1, 2, 3, 4, 5, 6, 78, 9, 10]
result = calculate_sums(numbers)
print(result)  # Output: [odd_sum, even_sum]