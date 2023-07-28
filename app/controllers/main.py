from password import Password


def main():
    while True:
        password_object = Password(input("Name: "))
        password_object.username = input("Username: ")
        option = (
            input("Do you want generate a password [y/n]").lower().strip()[0]
        )
        if "y" in option:
            length_pwd = int(input("Password length: "))
            min_numbers = int(input("Minimum numbers: "))
            min_special = int(input("Minimum special characters: "))
            password_object.gen_pwd(length_pwd, min_numbers, min_special)
        else:
            password_object.password = input("Password: ")
        password_object.url = input("URL: ")
        password_object.category = input("Category: ")
        print(
            f"""
{"-" * 35}
Name: {password_object.name}
Username: {password_object.username}
Password: {password_object.password}
URL: {password_object.url}
Category: {password_object.category}
{"-" * 35}
        """
        )
        option = (
            input("Do you want generate other password? [y/n] ")
            .lower()
            .strip()[0]
        )
        if "n" in option:
            break


if __name__ == "__main__":
    main()

# To do:
# Avoid ambiguous characters
# Chose max password length (done)
