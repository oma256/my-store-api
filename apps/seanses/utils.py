import random


def generate_random_number(length=13):
    digits = [str(random.randint(0, 9)) for _ in range(length)]
    return ''.join(digits)
