def get_numbers():
    return [1, 2, 3]

numbers = get_numbers()
for number in numbers:
    print(number)

def get_numbers():
    yield 1
    yield 2
    yield 3

for number in get_numbers():
    print(number)