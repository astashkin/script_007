import hashlib


def md5_signature(data):
    return hashlib.md5(data.encode()).hexdigest()


def sha512_signature(data):
    return hashlib.sha512(data.encode()).hexdigest()


signers = {'md5': md5_signature, 'sha512': sha512_signature}
