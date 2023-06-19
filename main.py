import random
import string

length_pwd = int(input("What is the password length? "))
min_numbers = int(input("Minimum numbers? "))
min_special = int(input("Minimum special characters? "))
length_pwd -= min_numbers + min_special

pwd = (
    random.choices(string.ascii_letters, k=length_pwd)
    + random.choices(string.digits, k=min_numbers)
    + random.choices("!@#$%^&*", k=min_special)
)

random.shuffle(pwd)
pwd = "".join(pwd)

print("Sua senha gerada", pwd)

# To do:
# Avoid ambiguous characters
# Chose max password length (done)
