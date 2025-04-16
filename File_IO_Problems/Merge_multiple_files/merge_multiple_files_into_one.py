import os 

folder_path = r"File_IO_Problems\Merge_multiple_files\large-file-download-test-master"
output_file = r"File_IO_Problems\Merge_multiple_files\merged.txt"

with open(output_file, "w", encoding = "utf-8") as outfile:
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), "r", encoding = "utf-8") as infile:
                outfile.write(infile.read() + "\n\n")

print("Merging complete. Output saved to merged.txt")   

#            or 

# use asynch function and multithreadding to merge multiple files at once.
