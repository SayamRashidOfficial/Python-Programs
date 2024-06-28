import re

# Example string
text = "The quick brown fox jumps over the lazy dog. Call 123-456-7890 for details."

# Search for a pattern
match = re.search(r"\d{3}-\d{3}-\d{4}", text)
if match:
    print(f"Phone number found: {match.group()}")  # Output: Phone number found: 123-456-7890

# Match pattern at the beginning of the string
match = re.match(r"The", text)
if match:
    print(f"Match found at the beginning: {match.group()}")  # Output: Match found at the beginning: The

# Find all occurrences of a pattern
numbers = re.findall(r"\d+", text)
print(f"All numbers found: {numbers}")  # Output: All numbers found: ['123', '456', '7890']

# Iterate over all matches
for match in re.finditer(r"\b\w{4}\b", text):
    print(f"Four-letter word found: {match.group()}")  # Output: quick, over, lazy

# Substitute patterns
new_text = re.sub(r"fox", "cat", text)
print(f"Substituted text: {new_text}")  # Output: The quick brown cat jumps over the lazy dog. Call 123-456-7890 for details.

# Split string by pattern
words = re.split(r"\s+", text)
print(f"Words: {words}")  # Output: ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.', 'Call', '123-456-7890', 'for', 'details.']