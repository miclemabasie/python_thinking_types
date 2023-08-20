def decorator_test(func):
    def wrapper():
        print("Start")
        func()
        print("end")

    return wrapper


@decorator_test
def dosomething():
    print("Alex")


dosomething()


# do somthing a certain number of times using a decorator
from functools import wraps


def repeat_greeting(numtimes):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(numtimes):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorate


@repeat_greeting(numtimes=4)
def greet(name):
    print(f"Hello, {name}")


greet("Miclem")
