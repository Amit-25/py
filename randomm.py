import random
import string


def generate_random_letter():
    d = random.choices(string.ascii_letters, k=20)
    return '->'.join(d)


for i in range(0, 3):
    print(generate_random_letter())
