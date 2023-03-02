def perfect_dish_to_share():
    """
    return generator for each number if he is perfect to share
    perfect is if sum of dividers = sum of dishes pieces
    :return:the numer if he is perfect
    """
    num = 1
    while True:
        if sum_of_dividers(num) == num:
            yield num
        num += 1


def sum_of_dividers(num):
    """
    check the amount of dividers of a num
    :param num: the number
    :return: the dividers count
    """
    count = 0
    for i in range(1, num):
        if num % i == 0:
            count += i
    return count
