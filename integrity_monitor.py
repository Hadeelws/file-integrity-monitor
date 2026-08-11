import hashlib
def calculate_hash(file_path):
    with open(file_path, "rb") as file:
        file_data = file.read()
    return hashlib.sha256(file_data).hexdigest()
def create_baseline(file_path):
    file_hash = calculate_hash(file_path)
    with open("baseline.txt", "w") as file:
        file.write(file_hash)
    print("\nBaseline created successfully")
    print("SHA-256:", file_hash)
def check_integrity(file_path):
    current_hash = calculate_hash(file_path)
    with open("baseline.txt", "r") as file:
        original_hash = file.read()
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
    file_path = input("Enter the file path: ")
    if choice == "1":
       create_baseline(file_path)
    elif choice == "2":
         if check_integrity(file_path):
                print("\nFile is unchanged.")
         else:
                print("\n ALERT: File has been modified!")
    else:
         print("\nInvalid option.")

if __name__ == "__main__":
    main() 