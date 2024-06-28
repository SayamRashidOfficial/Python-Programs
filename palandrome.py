def ispalandrome(s):
    return s == s[ :: -1]
print(ispalandrome('racecar'))

















# def is_palindrome(s):
#     # Convert to lowercase and remove non-alphanumeric characters
#     s = ''.join(c for c in s.lower() if c.isalnum())
#     return s == s[::-1]

# user_input = "A man, a plan, a canal: Panama"
# if is_palindrome(user_input):
#     print(f"'{user_input}' is a palindrome.")
# else:
#     print(f"'{user_input}' is not a palindrome.")
