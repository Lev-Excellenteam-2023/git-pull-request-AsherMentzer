def group_by(func, iterable):
    """
    the function group in dictionary each value in the iterable by the
    return value of operating the function on this value
    :param func: the function
    :param iterable: the collection
    :return: the dictionary
    """
    group = {}
    for i in iterable:
        k = func(i)
        if k not in group:
            group[k] = [i]
        else:
            group[k].append(i)
    return group


def main():
    print(group_by(len, ["hi", "bye", "yo", "try"]))


if __name__ == "__main__":
    main()