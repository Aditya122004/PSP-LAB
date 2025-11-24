generate_password = lambda s: ''.join(
    word[0].upper() + str(len(word)) for word in s.split()
)

apps = {}
passwords = {}

n = int(input("Enter number of applications: "))

for i in range(n):
    app = input(f"\nEnter application name {i+1}: ")
    sentence = input(f"Enter sentence to remember password for {app}: ")
    apps[app] = sentence  
    
    pwd = generate_password(sentence)
    passwords[app] = pwd    

print("\nDictionary of Applications & Sentences:")
for app, sent in apps.items():
    print(f"{app}: {sent}")

print("\nDictionary of Applications & Passwords:")
for app, pwd in passwords.items():
    print(f"{app}: {pwd}")
