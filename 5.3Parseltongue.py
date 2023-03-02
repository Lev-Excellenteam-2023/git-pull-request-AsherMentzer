def find_secrets(file_name):
    """
    find the secret messages in the resources/logo.jpg file
    :param file_name: the resources/logo.jpg file
    :return: generator for the secret messages
    """
    with open(file_name, 'rb') as file:
        word = b''
        while True:
            byte = file.read(1)
            if not byte:
                break
            if byte.isalpha() and byte.islower():
                word += byte
            elif byte == b'!':
                if word:
                    yield word.decode()
                    word = b''
            else:
                word = b''
