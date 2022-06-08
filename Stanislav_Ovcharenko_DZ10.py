# Задача 0
def one():
    x = ["one", "two"]
    def inner():
        print(x)
        print(id(x))
        return inner

o = one()

# Задача 1

def tel_number(a):
    tel_code = '+380'

    def user_number(a):
        return tel_code + str(a)

    return user_number(a)


print(tel_number(951154511))


# Задача 2

def decorator_no_magik_met(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(len(result))
        return result

    return wrapper


@decorator_no_magik_met
def no_magik_met(n):
    new_object = dir(n)
    methods = list(new_object)
    clear_methods = [q for q in methods if not q.startswith('__')]
    return clear_methods


print(no_magik_met([]))


# Задача 3

def decorator_no_magik_met_with_print(arg):
    print(arg)

    def print_str(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(len(result))
            return result

        return wrapper

    return print_str


@decorator_no_magik_met_with_print('need to learn')
def no_magik_met(n):
    new_object = dir(n)
    methods = list(new_object)
    clear_methods = [q for q in methods if not q.startswith('__')]
    return clear_methods


print(no_magik_met(()))

# Задача 4

base = {}


def decor_hash_info(func):
    def wrapper(*args):
        result = func(*args)
        for args in args:
            if args in base:
                print(base.get(args))
        return result

    return wrapper


@decor_hash_info
def hash_info(*args):
    if args not in base:
        base1 = {k: hash(k) for k in args}
    base.update(base1)
    return base


print(hash_info("t"))
print(hash_info("u"))
print(hash_info("u"))
print(hash_info("k"))
