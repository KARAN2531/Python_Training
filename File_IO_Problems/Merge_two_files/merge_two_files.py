'''
3. Merge Two Files
Write a program that takes two text files as input and merges their content line by line into a third file. If one file has more lines than the other, append the remaining lines at the end.
'''

def merge_file(file_1, file_2, output_file):
    with open(file_1, "r", encoding="utf-8") as f1, open(file_2, "r", encoding="utf-8") as f2, open(output_file, "w", encoding="utf-8") as out:

        lines1 = f1.readlines()
        lines2 = f2.readlines()

        for line1, line2 in zip(lines1, lines2):
            out.write(line1.strip() + " " + line2)

        remaining_lines = lines1[len(lines2):] + lines2[len(lines1):]

        out.writelines(remaining_lines) 

file_1 = r"File_IO_Problems\Merge_two_files\file_1.txt"
file_2 = r"File_IO_Problems\Merge_two_files\file_2.txt"
output_file = r"File_IO_Problems\Merge_two_files\output_file.txt"

merge_file(file_1, file_2, output_file)
print(f"out is saved in {output_file}")  
