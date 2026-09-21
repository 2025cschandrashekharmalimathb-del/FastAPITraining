# concept decorator 
def my_decorator(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper
@my_decorator
def say_hello():
    print("Hello!")
say_hello()