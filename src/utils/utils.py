import uuid


def generate_random_string(length: int=15) -> str:
    """ param length: how long random string should be
     :return: random string with specified length """
    random_str = str(uuid.uuid4())
    return random_str.replace('-', '')[:length]
