# File-Checker-Integrity-Tool

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: AADITYA JAISWAL

*INTERN ID*: CT04DR1407

*DOMAIN*: CYBER SECURITY AND ETHICAL HACKING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

*DESCRIPTION*:

In this program, several libraries are imported to handle specific tasks. The argparse library is used to parse command-line arguments, hashlib provides cryptographic hash functions, sys is used for system-related operations such as exiting the program, and colorama is used to display colored output messages in the terminal.
The function calculate_hash takes a file path as input and computes the SHA-256 hash value of the file. The file is opened in binary mode and read in chunks of 64KB to ensure that even large files can be processed efficiently without using unnecessary memory. As each chunk is read, it is passed into the hash object to update the hash calculation. After processing the entire file, the hexadecimal representation of the hash is returned.
The verify_file_hash function accepts the downloaded file path and an expected hash value. It calculates the actual hash of the provided file using the calculate_hash function and compares it with the expected hash. The function returns True if both values match, indicating that the file has not been tampered with or altered. If the values do not match, it returns False, suggesting that the file may not be safe or has been modified.
The script uses argparse to create a command-line interface. Two arguments are required: the -f or --file argument to specify the file that needs to be checked, and the --hash argument to provide the expected hash value. After parsing these arguments, the program checks if they were provided. If either argument is missing, an error message is printed to the console, and the program exits.
If both arguments are correctly provided, the script proceeds to verify the file by calling the verify_file_hash function. If the calculated hash matches the expected hash, a success message is displayed in green, indicating that the file is safe. If the hash does not match, a warning message is printed in red, informing the user that the file may not be safe to use.

*OUTPUT*: https://github.com/user-attachments/assets/ace6916b-c343-4437-9c05-9f910fe4b71c
