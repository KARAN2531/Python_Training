'''
27.Write a function that transforms a list of characters into a list of dictionaries,
where:

The keys are the characters themselves.
The values are the ASCII codes of those characters.
Examples
to_dict(["a", "b", "c"]) ➞ [{"a": 97}, {"b": 98}, {"c": 99}]

to_dict(["^"]) ➞ [{"^": 94}]

to_dict([]) ➞ []
'''

def to_dict(char_list):
    return [{char: ord(char)} for char in char_list]

print(to_dict(["a", "b", "c"]))
print(to_dict(["^"]))            