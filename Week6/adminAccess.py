admins={"admin1":"Aditya","admin2":"Adi"}
user=input("Enter username: ")
password=input("Enter password: ")
if(admins.get(user)!=None):
    if(password==admins.get(user)):
        print("Admin Access")
    else:
        print("Admin Access denied")
else:
    print("Admin Access denied")
