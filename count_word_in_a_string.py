def count_words(string):
    string1 = string.strip()
    count = 1
    
    for char in string1:
        if char == " ":
            count += 1
    return count

string1 = "This is  a string"
print(f"'{string1}' has a total of {count_words(string1)} words")









# def count_words(string):
#     # Remove spaces from the start and end of the string
#     string1 = string.strip()
#     # Initialize the count to 1 because there is no space at the end
#     count = 1
#     # Iterate through the string
#     for char in string1:
#         # If we encounter a space, increment the count
#         if char == " ":
#             count += 1
#     return count

# # Example usage:
# string1 = "Python is an interpreted, high-level, general-purpose programming language"
# print(f"'{string1}' has a total of {count_words(string1)} words")

# string2 = "Hi. My name is Ashwini"
# print(f"'{string2}' has a total of {count_words(string2)} words")
