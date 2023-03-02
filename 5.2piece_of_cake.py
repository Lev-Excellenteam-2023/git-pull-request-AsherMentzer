def get_recipe_price(prices, optionals=None, **ingredients):
    """
    calculate the price of all the ingredients in the recipe
    :param prices: dictionary of the price of eac ingredient
    :param optionals: optional list of ingredients to ignore in the calculation
    :param ingredients: the ingredients in the recipe and the amount of each
    :return: the total price of the recipe
    """
    total_price = 0
    for ingredient in ingredients:
        if ingredient not in optionals:
            total_price += (ingredients[ingredient] / 100) * (prices[ingredient])
    return total_price


