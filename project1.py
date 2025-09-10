# Original list for all examples
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
words = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
mixed = [1, "hello", 3.14, "world", 42, "python", 7.5]

print("Original lists:")
print(f"numbers: {numbers}")
print(f"words: {words}")
print(f"mixed: {mixed}")
print("\n" + "="*50 + "\n")

# 1. Squares of numbers
squares = [x**2 for x in numbers]
print("1. Squares of numbers:")
print(f"{numbers} → {squares}")
print()

# 2. Even numbers only
evens = [x for x in numbers if x % 2 == 0]
print("2. Even numbers only:")
print(f"{numbers} → {evens}")
print()

# 3. Odd numbers only
odds = [x for x in numbers if x % 2 != 0]
print("3. Odd numbers only:")
print(f"{numbers} → {odds}")
print()

# 4. Convert numbers to strings
number_strings = [str(x) for x in numbers]
print("4. Convert numbers to strings:")
print(f"{numbers} → {number_strings}")
print()

# 5. Words with length greater than 4
long_words = [word for word in words if len(word) > 4]
print("5. Words with length > 4:")
print(f"{words} → {long_words}")
print()

# 6. Uppercase words
uppercase_words = [word.upper() for word in words]
print("6. Uppercase words:")
print(f"{words} → {uppercase_words}")
print()

# 7. Numbers multiplied by 2 if even, divided by 2 if odd
transformed = [x*2 if x % 2 == 0 else x/2 for x in numbers]
print("7. Transform numbers (2x if even, /2 if odd):")
print(f"{numbers} → {transformed}")
print()

# 8. Extract only integers from mixed list
integers_only = [x for x in mixed if isinstance(x, int)]
print("8. Integers only from mixed list:")
print(f"{mixed} → {integers_only}")
print()

# 9. Extract only strings from mixed list
strings_only = [x for x in mixed if isinstance(x, str)]
print("9. Strings only from mixed list:")
print(f"{mixed} → {strings_only}")
print()

# 10. Word lengths
word_lengths = [len(word) for word in words]
print("10. Length of each word:")
print(f"{words} → {word_lengths}")
print()

# 11. Numbers divisible by 3
divisible_by_3 = [x for x in numbers if x % 3 == 0]
print("11. Numbers divisible by 3:")
print(f"{numbers} → {divisible_by_3}")
print()

# 12. First letter of each word
first_letters = [word[0] for word in words]
print("12. First letter of each word:")
print(f"{words} → {first_letters}")
print()

# 13. Create tuples of (number, square)
number_square_tuples = [(x, x**2) for x in numbers]
print("13. Tuples of (number, square):")
print(f"{numbers} → {number_square_tuples}")
print()

# 14. Filter words containing 'a'
words_with_a = [word for word in words if 'a' in word.lower()]
print("14. Words containing 'a':")
print(f"{words} → {words_with_a}")
print()

# 15. Cube of even numbers only
even_cubes = [x**3 for x in numbers if x % 2 == 0]
print("15. Cube of even numbers:")
print(f"{numbers} → {even_cubes}")
print()

# 16. Nested list comprehension: Matrix operations
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("16. Matrix operations:")
print(f"Original matrix: {matrix}")

# Transpose matrix
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(f"Transposed: {transpose}")

# Flatten matrix
flattened = [item for row in matrix for item in row]
print(f"Flattened: {flattened}")
print()

# 17. Conditional with multiple conditions
special_numbers = [x for x in numbers if x > 3 and x < 8]
print("17. Numbers between 3 and 8:")
print(f"{numbers} → {special_numbers}")
print()

# 18. Create dictionary from list comprehension
word_dict = {word: len(word) for word in words}
print("18. Dictionary comprehension - word: length:")
print(f"{words} → {word_dict}")
print()

# 19. Set comprehension - unique word lengths
unique_lengths = {len(word) for word in words}
print("19. Set comprehension - unique word lengths:")
print(f"{words} → {unique_lengths}")
print()

# 20. Complex transformation with if-else
result = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print("20. 'Even' or 'Odd' for each number:")
print(f"{numbers} → {result}")