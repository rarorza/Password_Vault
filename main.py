import random
import string


def main():
    length_pwd = int(input("Password length: "))
    min_numbers = int(input("Minimum numbers: "))
    min_special = int(input("Minimum special characters: "))
    length_pwd -= min_numbers + min_special

    pwd = gen_pwd(length_pwd, min_numbers, min_special)

    print("Your password:", pwd)


def gen_pwd(length_pwd, min_numbers, min_special):
    pwd = (
        random.choices(string.ascii_letters, k=length_pwd)
        + random.choices(string.digits, k=min_numbers)
        + random.choices("!@#$%^&*", k=min_special)
    )
    random.shuffle(pwd)
    pwd = "".join(pwd)
    return pwd


if __name__ == "__main__":
    main()

# To do:
# Avoid ambiguous characters
# Chose max password length (done)
