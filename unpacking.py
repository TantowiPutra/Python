"""
    *  : Unpacking Posisi
    ** : Unpacking Named Arguments

"""

""" Menerima banyak Argumen """
def total(*args):
    print(args)

total(1, 2, 3)

""" Menerima Banyak Named Argument """
def show(**kwargs):
    print(kwargs)

show(name="Andi", age=25)

""" Merge Dictionary"""
a = {"x": 1}
b = {"y": 2}

c = {**a, **b}
print(c)

a = [1, 2]
b = [3, 4]

""" Merge List """
c = [*a, *b]
print(c)

""" Unpacking Saat Function Call """
def func(x, y, z):
    print(x, y, z)

a = [1, 2, 3]
func(*a)  # sama dengan func(1, 2, 3)

""" Destructuring List """
user = [
    {
        "name": "Mukouda",
        "age": 27
    },

    {
        "name": "Mukouda2",
        "age": 28
    },

    {
        "name": "Mukouda3",
        "age": 30
    },

    {
        "name": "Mukouda4",
        "age": 29
    }
]

user.pop(0)

first, *middle, last = user
print(first, middle, last)

""" Unpacking Dictionary """

user2 = {
    'name': 'Fel',
    'age': 1233
}

print(*user2.items())

