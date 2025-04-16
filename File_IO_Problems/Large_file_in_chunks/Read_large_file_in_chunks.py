'''
8. Read Large File in Chunks
Write a program that reads a large text file in chunks (e.g., 1024 bytes at a time) instead of loading it all at once into memory.
'''

def read_file_in_chunks(file_path, chunk_size=1024):
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            print(chunk)

file_path = r"File_IO_Problems\Large_file_in_chunks\large_file.txt"
read_file_in_chunks(file_path)