#!/usr/bin/python3


def decorator(func):

    def wrapper():
        print("before")
        ret = func()
        print("after")
        return ret

    return wrapper


def base():
    print("base function")


if __name__ == "__main__":
    print("Run decorator")
    decorator(base)()

    # or
    arg = base
    f = decorator(arg)
    f()
