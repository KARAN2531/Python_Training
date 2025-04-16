'''
1. Word Frequency Counter
Write a program that reads a text file and counts the frequency of each word. Ignore case and punctuation. Save the results to another file in the format:
 word: count
'''

import string

def count_word_frequency(input_file, output_file):
    word_count = {}

    # Read the input file
    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            # Remove punctuation and convert to lowercase
            line = line.translate(str.maketrans("", "", string.punctuation)).lower()
            words = line.split()

            # Count word frequencies
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1

    # Write results to the output file
    with open(output_file, "w", encoding="utf-8") as file:
        for word, count in sorted(word_count.items()):
            file.write(f"{word}: {count}\n")

# Example usage
input_file = r"File_IO_Problems\word_frequency_counter\input.txt"   
output_file = r"File_IO_Problems/word_frequency_counter/output.txt"
count_word_frequency(input_file, output_file)
print(f"Word frequency count saved in {output_file}")
