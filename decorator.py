def make_pretty(func):
    def inner():
        print("I got decorated first")
        func()
    return inner


def ordinarious():
    print("I am ordinary")

#ordinary 
pretti = make_pretty(ordinary)
pretty()

#extraSHIT_remote

