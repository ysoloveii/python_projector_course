# task 1. Write a decorator that ensures a function
# is only called by users with a specific role.
# Each function should have an user_type with a string type in kwargs.


def is_admin(fun):
    def wrapper(user_type: str):
        if user_type.lower().strip() == 'admin':
            fun()
        else:
            raise ValueError("Permission denied")
    return wrapper


@is_admin
def show_customer_receipt():
    user_number = int(input("Enter your number: "))
    # eval() method parses the expression passed to this method
    # and runs python expression (code) within the program
    square_number = eval('user_number * user_number')
    print(square_number)


show_customer_receipt(user_type='user')
# show_customer_receipt(user_type='admin')

# task 2. Write a decorator that wraps a function in a
# try-except block and print an error if error has happened.


def catch_errors(fun):
    def wrapper(*args):
        try:
            fun(*args)
        except KeyError as e:
            print(f"Such key as {e} doesn't exist in the dictionary.")
    return wrapper


@catch_errors
def some_function_with_risky_operation(data):
    print(data['key'])


some_function_with_risky_operation({'foo': 'bar'})
some_function_with_risky_operation({'key': 'bar'})
