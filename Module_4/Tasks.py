
# Task 1

sample_string = '0123456789'

if len(sample_string) < 2:
    print('')
else:
    print(sample_string[:2] + sample_string[-2:], '\n')

# Task 2

phone_number = '093-4603466'

if len(phone_number) == 10 and phone_number.isnumeric():
    print(f'Phone number {phone_number} is correct')
else:
    print(f'Phone number {phone_number} is incorrect, it must contain exactly 10 digits\n')

# Task 3

expression = '12 + 3.5'
print(expression, '= ', end='')
result = float(input())

if eval(expression) == result:
    print('Correct!!!')
else:
    print('Incorrect!!!')

# Task 4

my_name = 'sergey'
name = str(input())

if my_name.lower() == name.lower():
    print(True)
else:
    print(False)
