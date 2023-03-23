list_name = ['神里綾華', '雷電影', '八重神子']

for i, name in enumerate(list_name, start=1):
    print(f'{i}: {name}')


def enum_eq(iterable, start=0):
    n = start
    for elem in iterable:
        yield n, elem
        n += 1


print()

for i, name in enum_eq(list_name, start=1):
    print(f'{i}: {name}')
