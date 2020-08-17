def make_pretty(func):
    def inner():
        print("I got decorated first")
        func()
    return inner


def ordinary():
    print("I am ordinary")

#ordinary 
pretty = make_pretty(ordinary)
pretty()

#extraordinary

#parameters
def divide(a,b):
    return a/b

#division = divide(a,b)

division = divide(a = 5, b = 2)

def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    print(a/b)

divide(2, 5)