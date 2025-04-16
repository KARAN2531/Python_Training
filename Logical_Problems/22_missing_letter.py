'''
22.Given a string containing unique letters, return a sorted string with the letters
that don't appear in the string.

Examples:
get_missing_letters("abcdefgpqrstuvwxyz") ➞ "hijklmno"
get_missing_letters("zyxwvutsrq") ➞ "abcdefghijklmnop"
get_missing_letters("abc") ➞ "defghijklmnopqrstuvwxyz"
get_missing_letters("abcdefghijklmnopqrstuvwxyz") ➞ ""
Notes:
The combination of both strings should be 26 elements long, including all the letters in the alphabet.

Letters will all be in lowercase.
'''

import string

def get_missing_letters(s):
    all_letters = set(string.ascii_lowercase)
    input_letters = set(s)
    missing = sorted(all_letters - input_letters)
    return ''.join(missing)

print(get_missing_letters("abcdefgpqrstuvwxyz"))  
print(get_missing_letters("zyxwvutsrq"))           
print(get_missing_letters("abc"))                 
print(get_missing_letters("abcdefghijklmnopqrstuvwxyz"))