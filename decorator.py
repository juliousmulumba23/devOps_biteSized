def new_decorator(original_func):
    def wrap_func():

        print('Some extra code, before the original function')
        original_func()
        print('some extra code, after the original function')
    return wrap_func


@new_decorator
def func_needs_decorator():
    print("I want to be decorated!!")

def simple_gen():
    for x in range(3):
        yield x

for number in simple_gen():
    print(number)


def gensquares(N):
    for i in range(N):
        yield i**2

for n in gensquares(10):
    print(n)


func_needs_decorator()
