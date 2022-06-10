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

def decorator_foo(func):
    dict_args = dict()

    def wrapper(*args):
        args_res = args
        args_result = dict_args.get(args_res, None)
        if args_result:
            print("Found result!")
            return args_result
        else:
            result_foo = func(*args)
            dict_args[args_res] = result_foo
            return result_foo
    return wrapper


@decorator_foo
def test_function(*args):
    print("FUNCTION CALL!!!")
    str_args = [str(arg) for arg in args]
    result = " >>> ".join(str_args)
    return result



print(test_function("sklafknkalf","safasf"))
print(test_function("sklafknkalf","safasf"))
print(test_function(11111,2222,3333))
print(test_function(11111,2222,3333))