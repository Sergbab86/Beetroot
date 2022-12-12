
# Task 1

# sentence = input("Enter some sentence:")
# my_list = sentence.replace(",", " ").split()  # in case sentence has commas
# my_dict = {}
#
# for i in my_list:
#     if i in my_dict:
#         my_dict[i] += 1
#     else:
#         my_dict.update({i: 1})
#
# print(my_dict)

# Task 2

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
}
total_price = 0

for fruit, quantity in stock.items():
    if fruit in prices:
        total_price += (quantity * prices.get(fruit))

print(total_price, "\n")

# Task 3

res = [(i, i ** 2) for i in range(1, 11)]

print(res, "\n")

# Task 4

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

weekdays_dict = {k: v for k, v in zip([i for i in range(1, 8)], weekdays)}
weekdays_dict_reversed = {k: v for k, v in zip(weekdays, [i for i in range(1, 8)])}
weekdays_dict_reversed_2 = {v: k for k, v in weekdays_dict.items()}

print(weekdays_dict)
print(weekdays_dict_reversed)
print(weekdays_dict_reversed_2)




