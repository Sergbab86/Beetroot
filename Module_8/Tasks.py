# Task 1

# def favorite_movie(name: str):
#     print(f"My favorite movie is named {name}", "\n")
#
#
# favorite_movie("Hobbit trilogy")
#
#
# # Task 2
#
#
# def make_country(country: str, capital: str):
#     my_dict = {}
#     my_dict.update({country: capital})
#     print(f"The capital of {country} is {my_dict[country]} or {my_dict.get(country)}")
#
#
# make_country("Ukraine", "Kiev")


# Task 3 TODO Переробити!!!!!!!


def make_operation(operator: str, *args):
    res = args[0]
    if operator == "+":
        for i in range(1, len(args)): # args[1:]
            res += args[i]
    elif operator == "-":
        for i in range(1, len(args)):
            res -= args[i]
    elif operator == "*":
        for i in range(1, len(args)):
            res *= args[i]

    return res


print(make_operation("+", 5, 5, 6))
