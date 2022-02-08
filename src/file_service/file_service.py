import os
from src.utils import utils


class UniqueFilenameGenerationError(Exception):
    """ Raised when unique filename generation failed """
    pass


def read_file(filename: str) -> str:
    """ :param filename: name or path of file to read
     :return: content of specified file """
    with open(filename, 'r') as f:
        content = f.read()
    return content


def create_file(content: str) -> str:
    """ Creates file in current directory with random filename
     :param content: content to write to file
     :return: filename of created file """
    try:
        filename = __generate_random_filename()
    except UniqueFilenameGenerationError as e:
        raise e
    with open(filename, 'w') as f:
        f.write(content)
    return filename


def delete_file(filename: str):
    """ Deletes specified file
    :param filename: filename or path to file """
    os.remove(filename)


def list_dir() -> list:
    """ :return: list with content of current directory """
    return os.listdir()


def change_dir(directory: str):
    """ Changes current working directory
    :param directory: directory name or path """
    os.chdir(directory)


def get_current_dir() -> str:
    """ :return: path of current working directory """
    return os.getcwd()


def __generate_random_filename(attempts: int=10000) -> str:
    """ Attempts to randomly generate filename that does not exist in current directory
    :raise: RandomNameGenerationError if unique filename was not generated after specified amount of attempts
    :param attempts: how many times to try before raising exception
    :return: string with unique filename """
    name_length = 15
    for i in range(attempts):
        filename = utils.generate_random_string(length=name_length)
        if not os.path.exists(filename):
            return filename
        if attempts > 0 and attempts % 1000 == 0:
            name_length += 1
    raise UniqueFilenameGenerationError(f"Failed to generate unique file name after {attempts} attempts")
