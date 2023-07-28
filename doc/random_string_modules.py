import random
import string

ascii_letters = string.ascii_letters
# Generates a string with alphabetic in lower and upper case
digits = string.digits
# Generates a string with numbers from 0 to 9
punctuation = string.punctuation
# Generates a string with ASCII punctuation (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.)

print(ascii_letters)
print(digits)
print(punctuation)

random_ascii = random.choices(ascii_letters, k=5)
print(random_ascii)
# random.choices return a random k sized list of elements

random.shuffle(random_ascii)
print(random_ascii)
# mix a list

random_ascii = "".join(random_ascii)
print(random_ascii)
# "".join() insert a list in a unique string
