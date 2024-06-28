def are_anagrams(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

string1 = "Listen"
string2 = "Silent"

if are_anagrams(string1, string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")
