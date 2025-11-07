import argparse
import hashlib
import sys
from colorama import init, Fore

# Initialise colorama for coloured text

init(autoreset=True)

# Define a function to calculate SHA-256 hash of a file

def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as file:
        while (data := file.read(65536)):
            sha256_hash.update(data)
        return sha256_hash.hexdigest()
        
# Function to verify hash of a downloaded file

def verify_file_hash(download_file, expected_hash):
    calculated_hash = calculate_hash(download_file)
    return calculated_hash.lower() == expected_hash.lower()

# Command-Line Argument Parsing

parser = argparse.ArgumentParser(description= "Is your file SAFE!? Check it now!")
parser.add_argument("-f", "--file", dest="downloaded_file", required=True, help= "Path of the downloaded file")
parser.add_argument("--hash", dest="expected_hash", required=True, help="Expected hash value")
args = parser.parse_args()

#Validate arguments and perform hash checking

if not args.downloaded_file or not args.expected_hash:
    print(
        f"{Fore.YELLOW}[-] Error: Please provide the downloaded file and expected hash.")
    sys.exit()

if verify_file_hash(args.downloaded_file, args.expected_hash):
    print(f"{Fore.GREEN}[+] Success: FILE IS SAFE! Hash match.")
else:
    print(f"{Fore.RED}[-] Warning: FILE MAY NOT BE SAFE! Hash does not matches")