import json
"""
Task 1 we did at practice on Saturday
Task 2 answer: you can add PYTHONPATH to sys.path by sys.path.insert(0, '/path/to/module')
               and Python will looking there first when importing modules
"""

# Task 3     I know you can open file via with open("myfile.txt") as f:
def count_lines(name: str):
    f = open(name, )
    print(f"number of lines: {len(f.readlines())}")
    f.close()


def count_chars(name: str):
    f = open(name)
    print(f"number of chars: {len(f.read())}")
    f.close()


def test(name: str):
    count_lines(name)
    count_chars(name)

l = [1,2,3]
l.append()
test("mymod.py")
