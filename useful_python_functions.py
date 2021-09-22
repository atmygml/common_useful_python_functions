# Unpacking

tup = (1, 2, 3, 4, 5)

list_a = [1, 2, 3, 4, 5]

string_a = "hello"

dictio = {"a": 1, "b": 2}

coords = [4, 5]

a, b, c, d, e = tup

print(a)

a1, b1 = dictio.items()

c1, d1 = dictio.values()

print(a1)
print(c1)

x, y = coords

print(x)


# List comprehension - to initialize lists

x = [0 for i in range(20)]

print(x)

y = [[i for i in range(5)] for i in range(5)]

print(y)


z = (i for i in "hello")

print(tuple(z))

sentence = "hello world in peace"

fu = {char: sentence.count(char) for char in set(sentence)}

print(fu)


names = ["Alan", "Convy", "Tess"]
ages = [21, 18, 36]

for names, ages in zip(names, ages):
    if ages > 20:
        print(names)


def funct01(arg1, arg2, arg3):
    print(arg1, arg2, arg3)


def funct02(arg1=None, arg2=None, arg3=None):
    print(arg1, arg2, arg3)


args = [1, 2, 3]

kwargs = {"arg2": 4, "arg3": 6, "arg1": 2}

funct01(*args)
funct02(**kwargs)

# for else or while else loop

search = [1, 2, 3, 4, 5, 6, 7]
target = 8

for element in search:
    if element == target:
        print("I have found it!")
        break
else:
    print("I didn't find it!")

# sort by key using lambda function

lst_b = [[1, 2], [3, 4], [4, 2], [-1, 3], [4, 5], [2, 3]]

e, f, g = [], [], []
lst_b.sort()
e = lst_b
print(e)
lst_b.sort(reverse=True)
f = lst_b
print(f)
lst_b.sort(key=lambda x: x[1])
g = lst_b
print(g)

# lambda function


def funct003(x):
    return x[0] + x[1]

# equivalent to :


lambda x: x[0] + x[1]
