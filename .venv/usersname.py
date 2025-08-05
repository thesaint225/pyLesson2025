name = input("Enter your userName: ")
password = input("Enter your password: ")

if isinstance(name, str) and isinstance(password, str):
    print(f"your name is {name}")
else:
    "access denied"

# print("\nYour UserName is:" + name)
# print("your password is :" + password)
