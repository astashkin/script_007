import os
from src.utils import utils


class RandomNameGenerationError(Exception):
    pass


def read_file(filename):
    with open(filename, 'r') as f:
        content = f.read()
    return content


def create_file(content):
    try:
        filename = __generate_random_filename()
    except RandomNameGenerationError as e:
        raise e
    with open(filename, 'w') as f:
        f.write(content)
    return filename


def delete_file(filename):
    os.remove(filename)


def list_dir():
    return os.listdir()


def change_dir(directory):
    os.chdir(directory)


def get_current_dir():
    return os.getcwd()


def __generate_random_filename(attempts=10000):
    for i in range(attempts):
        filename = utils.generate_random_string() + '.txt'
        if not os.path.isfile(filename):
            return filename
    raise RandomNameGenerationError(f"Failed to generate unique file name after {attempts} attempts")
