import re

def fetch_vehicle_numbers(text):
    pattern = r'[A-Z]{2}\d{2}[A-Z]{1,2}\d{4}'
    return re.findall(pattern, text)

def fetch_phone_numbers(text):
    pattern = r'[6-9]\d{9}'
    return re.findall(pattern, text)

def fetch_emails(text):
    pattern = r'[\w\.-]+@[\w\.-]+\.\w{2,3}'
    return re.findall(pattern, text)

def append_to_file(filename, items):
    with open(filename, "a") as f:
        for item in items:
            f.write(item + "\n")

while True:
    print("REGEX Extraction Menu")
    print("1. Fetch Vehicle Numbers")
    print("2. Fetch Phone Numbers")
    print("3. Fetch Email Addresses")
    print("Enter any other key to Exit")

    choice = int(input("Enter choice: "))

    with open("input.txt", "r") as file:
        data = file.read()

    if choice == 1:
        result = fetch_vehicle_numbers(data)
        append_to_file("vehicle.txt", result)
        print("Vehicle numbers appended to vehicle.txt")

    elif choice == 2:
        result = fetch_phone_numbers(data)
        append_to_file("phones.txt", result)
        print("Phone numbers appended to phones.txt")

    elif choice == 3:
        result = fetch_emails(data)
        append_to_file("emails.txt", result)
        print("Emails appended to emails.txt")

    else:
        print("Exiting program...")
        break
