'''
2. Reverse File Content
Write a program that reads a text file and creates a new file with the lines written in reverse order.
'''

def reverse_line(line):
    line = line[::-1]
    return "". join(line)

def reverse_file_content(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            x = reverse_line(line)
            with open(output_file, "w", encoding="utf-8") as file:
                file.write(f"{x}\n")
            x = "" 

input_file = "File_IO_Problems\Reverse_file_content\input.txt"   
output_file = "File_IO_Problems/Reverse_file_content/output.txt"  
reverse_file_content(input_file, output_file)
print(f"reversed text saved in {output_file}") 