import random
import string


x = 0
while x <= 12:
    password = random.choice(string.ascii_lowercase)
    print (password)
    x += 1