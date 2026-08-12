import hashlib
import json
from pathlib import Path
BASELINE_FILE = "baseline.json"

def calculate_hash(file_path):
    """Calculate the SHA-256 hash of a file."""
    with open(file_path, "rb") as file:
        return hashlib.sha256(file.read()).hexdigest()
    
def create_baseline(file_path):
    file_hash = calculate_hash(file_path)
    with open("baseline.txt", "w") as file:
         file.write(file_hash)
    print("\nBaseline created successfully")
    print(f"SHA-256: {file_hash}") 

def check_integrity(file_paths):
   current_hash = calculate_hash(file_paths)
   with open("baseline.txt", "r") as file:
       original_hash = file.read().strip()
   if current_hash == original_hash:
       return True
   else:
       return False
def main():
    print("File Integrity Monitor")
    print("-----------------------")
    print("1. Create Baseline")
    print("2. Check Integrity")
    choice = input("\nChoose an option: ")
    if choice == "1":
       files = input("Enter file paths spareted by commas: ").split(",")
       files = [file.strip() for file in files if file.strip()]
       create_baseline(files)
    elif choice == "2":
         files = input("Enter current file paths separated by commas: ").split(",")
         files = [file.strip() for file in files if file.strip()]
         check_integrity(files)
    else:
         print("\nInvalid option.")

if __name__ == "__main__":
    main() 