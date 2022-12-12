import random

# Task 1

my_list = [random.randrange(0, 100) for i in range(10)]
print(my_list)
count = 0
max_number = my_list[0]

while count < len(my_list):
    if max_number >= my_list[count]:
        pass
    else:
        max_number = my_list[count]
    count += 1

print(max_number, '\n')

# Task 2

my_list1 = [random.randint(1, 10) for i in range(10)]
my_list2 = [random.randint(1, 10) for i in range(10)]
print(my_list1)
print(my_list2)
count1 = 0
my_set = set()

while count1 < len(my_list1):
    if my_list1[count1] in my_list2:
        my_set.add(my_list1[count1])
    count1 += 1

print(my_set, '\n')

# Task 3

my_list3 = random.sample(range(1, 101), 100)
res_list = []
count3 = 0

while count3 < len(my_list3):
    if my_list3[count3] % 7 == 0 and my_list3[count3] % 5 != 0:
        res_list.append(my_list3[count3])
    count3 += 1

print(res_list)


