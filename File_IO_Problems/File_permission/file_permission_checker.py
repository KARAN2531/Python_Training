'''
10. File Permissions Checker
Write a script that checks whether a given file is readable, writable, and executable by the current user.
'''

import os

def check_file_permissions(file_path):
    permissions = os.stat(file_path)
    
    is_readable = bool(permissions.st_mode & os.R_OK)
    is_writable = bool(permissions.st_mode & os.W_OK)
    is_executable = bool(permissions.st_mode & os.X_OK)
    
    print(f"File: {file_path}")
    print(f"Readable: {is_readable}")
    print(f"Writable: {is_writable}")
    print(f"Executable: {is_executable}")

file_path = r"File_IO_Problems\File_permission\dummy_file.txt"
check_file_permissions(file_path)