def our_decorator(some_function):
    def wrapper(*args):
        print(f'{some_function.__name__} has been executed')
        res = some_function(*args)
        return res

    return wrapper


@our_decorator
def new_function(x, y):
    return x * y


@our_decorator
def very_new_function(x, y):
    return x - y


print(new_function(10, 12))
print(very_new_function(100, 25))