#Strings

#1. Write a Python program to calculate the length of a string.

s = input("Enter the string to get its length: ")
s_length = len(s)
print(s_length)

#2. Write a Python program to count the number of characters (character frequency) in a string.
   #Sample String : google.com
   #Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

s = "google.com"  
dict = {}
for char in s: 
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1    
         
print(dict)    

#          or 

from collections import Counter  # noqa: E402

s = "google.com"
char_count = Counter(s)

print(dict(char_count))

#3. Write a Python program to get a string from a given string where all occurrences of its 
# first char have been changed to '$', except the first char itself.
    #Sample String : 'restart'
    #Expected Result : 'resta$t'

sample_string = 'restart'
fst_chr = sample_string[0]

modified_string = fst_chr + sample_string[1:].replace(fst_chr, '$')

print(modified_string)

#4. Write a Python program to add 'ing' at the end of a given string (length should be atleast 3).
 
try:
    input_str = input("Enter your string : ")
    x = "ing"
    if len(input_str) > 2:
        print(input_str + x)
    else:
        print("the string should have more than 2 characters")
except Exception as e:
    print(f"An unexpected error has occured: {e}")         

# If the given string already ends with 'ing' then add 'ly' instead. 
# If the string length of the given string is less than 3, leave it unchanged.
    #Sample String : 'abc'
    #Expected Result : 'abcing'
    #Sample String : 'string'
    #Expected Result : 'stringly'

try:
    input_str = input("Enter your string : ")
    x = "ing"
    y = len(input_str)
    check_str = input_str[y-3:]
    if len(input_str) < 3:
        print("no changes made")
    elif check_str == x:
        print(input_str + "ly")
except Exception as e:
    print(f"An unexpected error has occured: {e}")    
 
#5. Write a Python function that takes a list of words and returns the length of the longest one.

def longest_string():
    try: 
        input_list = input("Enter words seperated by spaces : ").split(" ")
        word_length = {word : len(word) for word in input_list}

        if not word_length:
            print("No words entered: ")
            return None

        longest = max(word_length, key= word_length.get)  
        return longest
    except Exception as e:
        print(f"an unexpected error has occurred: {e}")    

longest_string()

#6. Write a Python script that takes input from the user and displays that input back in upper and lower cases.

def switch_to_upper_case():
    x = input("Enter your string to change to uppercase: ")
    res = x.upper()
    return res
switch_to_upper_case()

def switch_to_lower_case():
    x = input("Enter your string to change to lowercase: ")
    res = x.lower()
    return res
switch_to_lower_case()

#7. Write a Python program that accepts a comma separated sequence of words as input and prints the 
# unique words in sorted form (alphanumerically).
    #Sample Words : red, white, black, red, green, black
    #Expected Result : black, green, red, white,red

try:
    input_str = input("enter words seperated by commas: ")

    words = input_str.split(",")
    words = [word.strip() for word in words]
    unique_words = sorted(set(words))

    print(",".join(unique_words))

except Exception as e:
    print(f"an unexpected error has occurred: {e}")    

#8. Write a Python program to get the last part of a string before a specified character
    #https://www.w3resource.com/python-exercises
    #https://www.w3resource.com/python

def get_before_character(string, char):
    return string.rsplit(char, 1)[0]  # Splits from the right and takes the first part

url = "https://www.w3resource.com/python-exercises"
result = get_before_character(url, "/")
print(result)  

#9. Write a Python program to display formatted text (width=50) as output.

import textwrap  # noqa: E402

try:
    input_text = input("Enter your text: ")
    formatted_text = textwrap.fill(input_text, width=50)  # Wraps text to 50 characters per line
    
    print("\nFormatted Text:\n")
    print(formatted_text)

except Exception as e:
    print(f"An unexpected error occurred: {e}")

#10. Write a Python program to count occurrences of a substring in a string.

input_string = input("Enter your string: ")
substring = input("Enter the substring: ")
count = input_string.count(substring)
print(f"The substring {substring} occurs {count} times")

#11. Write a Python program to reverse a string.

x = input("Enter your string to reverse: ")
y = x[::-1]
print(f"Reversed string : {y} ", y)

#12. Write a Python program to lowercase first n characters in a string.

n = int(input("Enter the value of n: "))
input_str = input("Enter your string: ")
first_part = input_str[:n+1].lower() 
last_part = input_str[n+1:]   
final = first_part + last_part
print(final)