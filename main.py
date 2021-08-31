import random
import string

print("Hello, Welcome to the Password Generator!")

length = int(input("\nEnter the length of the password:"))

upper = string.ascii_uppercase

lower = string.ascii_lowercase

num = string.digits

symbols = string.punctuation

all = upper + lower + num + symbols

mix_labels = random.sample(all, length)

password = "".join(mix_labels)

print (password)



