def cup_of_join(*lists, sep='-'):
    """
    get unknown lists numbers and join them by the sep
    :param lists: the lists to join
    :param sep: the seperator to join by default is '-'
    :return: the joined lists
    """
    if not lists:
        return None

    return sep.join(lists)
