def make_pretty(func):
    def inner():
        print("I got decorated first")
        func()
    return inner


def ordinary():
    print("I am ordinary")

ordinary() 
pretty = make_pretty(ordinary)
pretty()

#extraordinary
@make_pretty
def ordinary2():
    print("I am ordinary 2")

ordinary2()
