# task 1. Write a decorator that ensures a function
# is only called by users with a specific role.
# Each function should have an user_type with a string type in kwargs.


def is_admin(fun):
    """Return permission denied error if customer role is not admin."""
    def wrapper(user_type: str):
        if user_type.lower().strip() == 'admin':
            fun()
        else:
            raise ValueError("Permission denied")
    return wrapper


@is_admin
def show_customer_receipt():
    """Allows the user to get the result of
    multiplying the entered number by itself."""
    user_number = int(input("Enter your number: "))
    # eval() method parses the expression passed to this method
    # and runs python expression (code) within the program
    square_number = eval('user_number * user_number')
    print(square_number)


show_customer_receipt(user_type='user')
show_customer_receipt(user_type='admin')

# task 2. Write a decorator that wraps a function in a
# try-except block and print an error if error has happened.


def catch_errors(fun):
    """Returns an error if the key entered
    by the user is not in the dictionary."""
    def wrapper(*args, **kwargs):
        try:
            fun(*args, **kwargs)
        except KeyError as e:
            print(f"Such key as {e} doesn't exist in the dictionary.")
    return wrapper


@catch_errors
def some_function_with_risky_operation(data):
    """Prints the value from the dictionary
    with the 'key' key."""
    print(data['key'])


some_function_with_risky_operation({'foo': 'bar'})
some_function_with_risky_operation({'key': 'bar'})

# task 3. Create a decorator that will check types.
# It should take a function with arguments and validate inputs with annotations.


def check_types(fun):
    """Checks the types of the arguments of
    a function using it's annotations."""
    def wrapper(*args, **kwargs):
        signature = fun.__annotations__
        for arg_name, arg_value in zip(signature, args):
            expected_type = signature[arg_name]
            if not isinstance(arg_value, expected_type):
                raise TypeError(f"{type(arg_value)} of {arg_value} should be of type {expected_type.__name__}")
        return fun(*args, **kwargs)
    return wrapper


@check_types
def add(a: int, b: int) -> int:
    return a + b


print(add(1, 2))
print(add("1", "2"))
