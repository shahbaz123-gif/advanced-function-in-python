# Example 1: Squares of numbers
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(f"Squares: {squares}")  # Output: [1, 4, 9, 16, 25]

# Example 2: Convert to uppercase
words = ['hello', 'world', 'python']
uppercase_words = [word.upper() for word in words]
print(f"Uppercase: {uppercase_words}")  # Output: ['HELLO', 'WORLD', 'PYTHON']

# Example 3: Extract first characters
names = ['Alice', 'Bob', 'Charlie']
first_chars = [name[0] for name in names]
print(f"First characters: {first_chars}")  # Output: ['A', 'B', 'C']