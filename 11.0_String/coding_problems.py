# Print each character of a string.
st = "Hello"
for i in st:
    print(i)

# Print characters using indexing.
st = "Hello"
print(st[0])
print(st[-1])

# Find string length without using len().
st = "Hello"
check_length = 0
for i in st:
    check_length += 1
print(f"String Length : {check_length}")

# Remove all spaces from a string.
st = "welcome to programming world"
# print(st)
print(st.replace(' ',''))

# Replace all vowels with *.
st = "welcome to programming world"
# print(st)
vowels = 'aeiouAEIOU'
new_st = ''
for i in st:
    if(i in vowels):
        new_st += '*'
    else:
        new_st += i
print(new_st)

# Count words in a sentence.
st = "welcome to programming world"
print(len(st.split()))

# Swap uppercase to lowercase and vice versa.
st = input("Enter any input :- ")
# print(st)
print(st.swapcase())

# Find frequency of each character.
char_frequency = {}
st = input("Enter any input :- ")
for i in st:
    if(i not in char_frequency):
        char_frequency[i] = 1
    else:
        char_frequency[i] += 1
print(char_frequency)

# Find most frequent character.
char_frequency = {}
st = input("Enter any input to check more frequent character :- ")
for i in st:
    if(i not in char_frequency):
        char_frequency[i] = 1
    else:
        char_frequency[i] += 1
for key,value in char_frequency.items():
    if(value > 1):
        print(f"{key} => {value}")

# Convert first letter of every word to uppercase manually.
st = "welcome to python programming world"
new_li = []
for i in st.split():
    new_li.append(i[0].upper()+i[1:])
print(" ".join(new_li))

# Find longest word in a sentence.
st = "welcome to python programming world"
highest_word = {}
for i in st.split():
    highest_word[i] = len(i)
# print(highest_word)
high = max(list(highest_word.values()))
# print(f"Maximum : {high}")
for key,value in highest_word.items():
    if(value == high):
        print(f"The longest word is :- {key}")

# Find shortest word in a sentence.
st = "welcome to python programming world"
smallest_word = {}
for i in st.split():
    smallest_word[i] = len(i)
# print(smallest_word)
small = min(list(smallest_word.values()))
# print(f"Minimum : {small}")
for key,value in smallest_word.items():
    if(value == small):
        print(f"The shortest word is :- {key}")

# Count occurrence of every word.
st = "welcome to python programming world"
count_occurance = {}
for word in st.split():
    if(word not in count_occurance):
        count_occurance[word] = 1
    else:
        count_occurance[word] += 1
print(f"Count occurance : {count_occurance}")

# Check whether a string contains only alphabets.
st = "welcome"
print(st.isalpha())

# Check whether a string contains only numbers.
st = "12345wlcomme"
print(st.isdigit())

# Generate all substrings.
st = "Welcome To Python Programming World"
st = st.split()
print(st)

# Compress a string (aaabbc → a3b2c1).
st = "aaabbc"
new_st = {}
for i in st:
    if(i not in new_st):
        new_st[i] = 1
    else:
        new_st[i] += 1
final_st = ""
for key,value in new_st.items():
    final_st = final_st + key + str(value)
print(final_st)

# Find second most frequent character.
char_frequency = {}
st = input("Enter any input to check more frequent character :- ")
count = 0
for i in st:
    if(i not in char_frequency):
        char_frequency[i] = 1
    else:
        char_frequency[i] += 1
print(char_frequency)
for key,value in char_frequency.items():
    if(value > 1):
        if(count > 0):
            print(f"Second Most Frequent Character : {key} => {value}")
            break
        else:
            count += 1

# Check whether two strings are anagrams.
st1 = input("Enter any input :- ")
st2 = input("Enter any input :- ")
st_1 = {}
st_2 = {}
for i in st1:
    if(i not in st_1):
        st_1[i] = 1
    else:
        st_1[i] += 1
for j in st2:
    if(j not in st_2):
        st_2[j] = 1
    else:
        st_2[j] += 1
if(st_1 == st_2):
    print("Both Strings Are Anagram")
else:
    print("Both Strings Are Not Anagram")

# Find first non-repeating character.
char_frequency = {}
st = input("Enter any input to check more frequent character :- ")
count = 0
for i in st:
    if(i not in char_frequency):
        char_frequency[i] = 1
    else:
        char_frequency[i] += 1
print(char_frequency)
for key,value in char_frequency.items():
    if(value == 1):
        print(f"First Non Repetating Character : {key}.")
        break
    else:
        continue

# Remove duplicate characters.
st = "programming"
remove_duplicate = ""
for i in st:
    if(i not in remove_duplicate):
        remove_duplicate += i
    else:
        continue
print(remove_duplicate)

# Find the longest palindrome substring.