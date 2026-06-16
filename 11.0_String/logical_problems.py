# Count total vowels in a string.
st = "programming"
count_vowel = 0
for i in st:
    if(i in "aeiouAEIOU"):
        count_vowel += 1
print(f"Total Vowels {count_vowel}")

# Count total consonants in a string.
st = "programming"
count_consonant = 0
for i in st:
    if(i not in "aeiouAEIOU"):
        count_consonant += 1
print(f"Total Consonant {count_consonant}")

# Count total spaces in a sentence.
st = "hello world"
count_space = 0
for i in st:
    if(i.isspace()):
        count_space += 1
print(f"Total Spaces {count_space}")

# Count uppercase letters.
st = "Hello World"
count_upper = 0
for i in st:
    if(i.isupper()):
        count_upper += 1
print(f"Total Uppercase Letter {count_upper}")

# Count lowercase letters.
st = "Hello World"
count_lower = 0
for i in st:
    if(i.islower()):
        count_lower += 1
print(f"Total LowerCase Letter {count_lower}")

# Count digits in a string.
st = "Hello123World"
count_digit = 0
for i in st:
    if(i.isdigit()):
        count_digit += 1
print(f"Total Digits {count_digit}")

# Count special characters.
st = "Hello123@World"
count_special_char = 0
for i in st:
    if(i in "!@#$%^&*()_-=+"):
        count_special_char += 1
print(f"Total Special Character {count_special_char}")

# Find the frequency of a character.
char_frequence = {}
st = "programming"
for i in st:
    if(i not in char_frequence):
        char_frequence[i] = 1
    else:
        char_frequence[i] += 1
print(char_frequence)

# Check whether a string is a palindrome.
st = "level"
if(st == st[::-1]):
    print("Palindrome")
else:
    print("Not Palindrome")

# Reverse a string without using slicing.
st = "welcome"
reverse = ""
for i in st:
    reverse = i + reverse
print(reverse)