import string
import random

passwords = {}

def generate_password(length, include_special):
    characters = string.ascii_letters + string.digits
    if include_special:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

while True:
    ask=input("Whether you need to store a new password(s) or need to retrive(r) : ")
    if ask=="s":
        website = input("\nEnter website name: ")
        password = input(f"Enter password for {website}: ")
        passwords[website] = password
        print(f"Password saved for {website}.")
    elif ask=="r":
        retrieve = input("Do you want to retrieve a password by website name? (yes/no): ").lower()
        if retrieve == "yes":
            site = input("Enter website name: ")
            print("Password:", passwords.get(site, "No password found."))
        update = input("Do you want to change the password or just save it? (change/save): ").lower()

        if update == "change":
            choice = input("Do you want to create a new password yourself or auto-generate? (manual/auto): ").lower()
            if choice == "manual":
                new_pass = input("Enter new password: ")
            else:
                length = int(input("Enter desired password length (in numbers): "))
                special = input("Include special characters? (yes/no): ").lower() == "yes"
          
                new_pass = generate_password(length, special)
                print("Generated password:", new_pass)

        
                passwords[website] = new_pass
                print(f"Password updated for {website}.")
        else:
            print("No changes made. Password saved.")
        continue_prompt = input("\nDo you want to continue using the password manager? (yes/no): ").lower()
        if continue_prompt != "yes":
                print("Exiting password manager.")
                break
