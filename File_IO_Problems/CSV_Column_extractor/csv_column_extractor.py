'''
5. CSV Column Extractor(doubt)(learn)
Write a program that reads a CSV file (without using pandas) and extracts a specific column given by the user, saving the extracted data into another file.
'''

import csv 

def extract_column(input_file, output_file, column_name):
    with open(input_file, "r", encoding="utf-8") as infile:
        reader = csv.reader(infile)
        headers = next(reader)  # Read the header row

        if column_name not in headers:
            print(f"Column '{column_name}' not found in {input_file}. Available columns: {headers}")
            return
        
        col_index = headers.index(column_name)  # Get the index of the column

        with open(output_file, "w", encoding="utf-8") as outfile:
            outfile.write(column_name + "\n")  # Write header for output file
            for row in reader:
                outfile.write(row[col_index] + "\n")  # Write the column values

    print(f"Column '{column_name}' extracted to {output_file}")


input_csv = "File_IO_Problems/CSV_Column_extractor/data.csv"
output_csv = "File_IO_Problems/CSV_Column_extractor/extracted_column.txt"
column_to_extract = "Name"  

extract_column(input_csv, output_csv, column_to_extract)