import string
import random


def generate_random_string(lengths=10):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=lengths))