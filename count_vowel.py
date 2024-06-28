def count_vowel(text):
    count = 0
    for charcter in text:
        if(charcter in "aAeEiIoOuU"):
            count += 1
    return count

Text = input('Enter a Text: ')
count = count_vowel(Text)
print('Count vowel: ',count)