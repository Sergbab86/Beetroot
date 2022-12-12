import random

# Task 1

program_number = random.randint(1, 10)
my_number = int(input('Enter your number:'))

if program_number == my_number:
    print('You guessed the number!!!\n')
else:
    print('Sorry, you didn\'t guessed the number\n')

# Task 2

my_name = input('Enter your name: ')
my_age = int(input('Enter your age: '))

print(f'Hello {my_name.capitalize()}, on your next birthday you’ll be {my_age+1} years')

# Task 3

my_string = input('Enter some string: ')

for i in range(5):
    print(''.join(random.choices(my_string, k=len(my_string))), end=' ')
