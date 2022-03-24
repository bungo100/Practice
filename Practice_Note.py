def dec(func):
    def wrapper(*args):
        print('Hello')
        func(*args)
        print('Good Bye')
    return wrapper

@dec
def say_name_origin(name, origin):
    print("My name is {}. I'm from {}".format(name, origin))



if __name__ == "__main__":
    say_name_origin('Ichita', 'London')