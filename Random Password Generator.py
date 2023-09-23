import random

length = int(input("Enter your password length:- "))
password = ""

choice = "ABCDEFGHIJKLMNOPQRSTUVWSYZabcdefghijklmnopqrstuvwxyz1234567890!@#~$%^&*(){}[]/?\|"

for i in range(length):
    password += random.choice(choice)
print("Your Password is " + password)