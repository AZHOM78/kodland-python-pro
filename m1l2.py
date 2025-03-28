import random
characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password_length = int(input("masukkan panjang kata sandi yang diinginkan:"))
generated_password = ""


for i in range(password_length):
    generated_password += random.choice(characters)

print("kata sandi yang dihasilkan:",generated_password)
