import os
from src.utils import utils
from src.crypto import signature_easy
from src.crypto.signature import SignatureFactory


class UniqueFilenameGenerationError(Exception):
    """ Raised when unique filename generation failed """
    pass


def read_file(filename: str) -> str:
    """ :param filename: name or path of file to read
     :return: content of specified file """
    with open(filename, 'r') as f:
        content = f.read()
    return content


def create_file(content: str, filename: str='') -> str:
    """ Creates file in current directory with random filename
     :param content: content to write to file
     :param filename: name of file
     :return: filename of created file """
    if not filename:
        filename = __generate_random_filename()
    with open(filename, 'w') as f:
        f.write(content)
    return filename


def read_signed_file(filename: str) -> str:
    """ :param filename: name or path of file to read
     :return: content of specified file """
    data = read_file(filename)
    for label in SignatureFactory.signers:
        sig_filename = f"{filename}.{label}"
        if os.path.exists(sig_filename):
            signer = SignatureFactory.get_signer(label)
            with open(sig_filename, "r") as sig_file:
                actual_sig = signer(data)
                expected_sig = sig_file.read()
                if actual_sig == expected_sig:
                    return data
                else:
                    raise Exception("File broken")


def create_signed_file(content: str) -> str:
    """ Creates file in current directory with random filename
     :param content: content to write to file
     :return: filename of created file """
    filename = __generate_random_filename()
    create_file(content, filename)
    signers = signature_easy.signers
    for signer in signers:
        hash_string = signers[signer](content)
        hash_filename = filename + '.' + signer
        create_file(hash_string, hash_filename)
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


def get_file_metadata(filename: str) -> tuple:
    """
     :param filename: file to read
     :return: tuple (create_date, modification_date, filesize) """
    metadata = os.stat(filename)
    return metadata.st_ctime, metadata.st_mtime, metadata.st_size


def __generate_random_filename(attempts: int=10000) -> str:
    """ Attempts to randomly generate filename that does not exist in current directory
    :raises: RandomNameGenerationError if unique filename was not generated after specified amount of attempts
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
