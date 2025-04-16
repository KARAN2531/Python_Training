'''
3.For a given sentence, return the average word length.
Note: Remember to remove punctuation first.
sentence1 = "Hi all, my name is Tom...I am originally from Australia."
'''

import string  # noqa: E402

def remove_punctuation(input_string):
    result = input_string
    for char in string.punctuation:
        result = result.replace(char, '')
    return result

Sentence1 = "Hi all, my name is Tom...I am originally from Australia."
input_string = Sentence1

string_for_average= remove_punctuation(input_string)

words = string_for_average.split()

x = len(words)
y = [len(word) for word in words]

average_word_length = sum(y) / x if x > 0 else 0  # Avoid division by zero

print(average_word_length)