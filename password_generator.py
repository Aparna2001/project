import random

chars = "abcdefghijklmnopqrstuvwzyzABCDEFGHIJKLMOPQRSTUVWXYZ@120853"
ch = 15

while ch:
    password_len = int(input("What should be the length of password? : "))
    password_count = int(input("How many passwords do you need? : "))
    for i in range (0,password_count):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password = password + password_char
        print("Your passwords: ",password)
    ch = int(input("Do you want to generate more?(0/1) "))

