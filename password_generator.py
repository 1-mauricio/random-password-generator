import random

charts ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123234567890!@#$%&()<>"

while 1:
    password_len = int(input("Qual o tamanho da senha que você gostaria? (What length would you like your password to be): "))
    password_count = int(input("De quantas senhas você gostaria? (How many passwords would you like) "))
    for i in range(0, password_count):
        password = ""
        for j in range(0, password_len):
            password_char = random.choice(charts)
            password += password_char
        print(f"Aqui está a sua senha(Here is your password): {password}")