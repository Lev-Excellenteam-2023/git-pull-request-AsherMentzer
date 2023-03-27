import re


def count_words(text):
    """

    :param text:
    :return:
    """
    return {word: len(word) for word in re.findall(r'\b[a-zA-Z]+\b', text)}


def main():
    text = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """
    print(count_words(text))


if __name__ == "__main__":
    main()
