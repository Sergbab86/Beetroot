
# Task 1  If we will raise KeyError in oops(), block try in call_oops() will execute,
#         and we will get KeyError

def oops(mylist=(1,)):
    raise IndexError


def call_oops():
    try:
        oops()
    except IndexError:
        print("This is IndexError from oops", "\n")


call_oops()

# Task 2


def myFunc():
    a = input("a = ")
    b = input("a = ")
    try:
        return int(a) / int(b)
    except ValueError:
        return "Sorry, both values must be numbers"
    except ZeroDivisionError:
        return "You cannot divide by zero"


print(myFunc())