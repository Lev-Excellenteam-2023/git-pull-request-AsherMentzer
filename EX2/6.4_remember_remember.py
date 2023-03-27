from PIL import Image


def find_secret(image_path):
    """
    the function get image and find the secret msg hidden there
    is reveled by finding in each column the only black pixel there
    and the letter is the ascii for is row number like 72 == 'H'
    :param image_path: the image to find the secret msg
    :return: the secret msg
    """
    image = Image.open(image_path).convert('RGB')
    # get the image size
    width, height = image.size
    secret_msg = ""
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            # if the color is black add the letter to the secret msg
            if r == 1 and g == 1 and b == 1:
                secret_msg += chr(y)
    return secret_msg


def main():
    print(find_secret("code.png"))


if __name__ == "__main__":
    main()
