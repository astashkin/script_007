import uuid


def generate_random_string(length=15):
    random_str = str(uuid.uuid4())
    return random_str.replace('-', '')[:length]
