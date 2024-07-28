import random
print("Welcome to password generator")
password="1234567890!@#$%^&*()abcdefghijklmnopqrstuvwxyz"
length_password=int(input("Enter the length of pasword:"))
a="".join(random.sample(password,length_password))
print(f"The password is:{a}")

