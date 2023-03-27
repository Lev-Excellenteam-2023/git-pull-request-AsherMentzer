import functools


class CustomTypeError(TypeError):
    pass


def type_check(correct_type):
    def type_checker_decorator(func):
        @functools.wraps(func)
        def wrapper(arg):
            if isinstance(arg, correct_type):
                return func(arg)
            else:
                raise CustomTypeError(f"Expected argument of type {correct_type}, but got {type(arg)} instead.")

        return wrapper

    return type_checker_decorator


@type_check(int)
def times2(num):
    return num * 2
