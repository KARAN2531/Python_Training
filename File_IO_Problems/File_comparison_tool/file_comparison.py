'''
6. File Comparison Tool
Write a program that compares two text files line by line and reports the differences in a third file.
'''

def compare_files(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        max_len = max(len(lines1), len(lines2))

        for i in range(max_len):
            line1 = lines1[i].strip() if i < len(lines1) else "[No Line]"
            line2 = lines2[i].strip() if i < len(lines2) else "[No Line]"

            if line1 != line2:
                out.write(f"Line {i+1}:\nFile1: {line1}\nFile2: {line2}\n\n")

file1 = r"File_IO_Problems\File_comparison_tool\file1.txt"
file2 = r"File_IO_Problems\File_comparison_tool\file2.txt"
output_file = r"File_IO_Problems\File_comparison_tool\output.txt"

compare_files(file1, file2, output_file)