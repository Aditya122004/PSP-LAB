from AddressBook.addressbook import AddressBook

ab = AddressBook()

while True:
    print("1. Add New Record")
    print("2. Search in Binary File")
    print("Enter any other key to Exit")
    ch=int(input("Enter a choice: "))
    if ch == 1:
        print("Enter Details:")
        name = input("Name: ")
        phone = input("Phone: ")
        dob = input("DOB (dd-mm-yyyy): ")
        email = input("Email: ")
        ab.add_record(name, phone, dob, email)
        ab.save_json("addressbook.json")
        ab.save_csv("addressbook.csv")
        ab.save_binary("addressbook.dat")
        print("Saved to JSON, CSV and Binary Files Successfully!")
        
    elif ch == 2:
        print("Search by:")
        print("1. Name")
        print("2. Phone")
        print("3. DOB")
        print("4. Email")

        key_choice = int(input("Enter choice: "))
        keys = ["name", "phone", "dob", "email"]

        if 1 <= key_choice <= 4:
            key = keys[key_choice - 1]
            value = input(f"Enter {key}: ")

            result = ab.search_in_binary("addressbook.dat", key, value)

            if result:
                print("Record Found:")
                print("Name :", result["name"])
                print("Phone:", result["phone"])
                print("DOB  :", result["dob"])
                print("Email:", result["email"])
            else:
                print("No matching record found.")
        else:
            print("Invalid search option!")

    else:
        print("Exiting Program")
        break
