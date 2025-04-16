'''
9. Find and Replace in a File
Write a program that asks the user for a word to find and another word to replace it with. Modify the file in-place with the replacements.
'''

def find_and_replace(file_path, find_word, replace_word):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    updated_content = content.replace(find_word, replace_word)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

    print(f"Replaced '{find_word}' with '{replace_word}' in {file_path}.")
file_path = r"File_IO_Problems\Find_and_replace_in_File\sample_file.txt"

find_and_replace(file_path, "sample", "example")