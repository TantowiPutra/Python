from turtle import Turtle, Screen
import prettytable

""" Setiap Turtle Mendapatkan Akses Object Screen yang sama -- Shared Object (Singleton) """
# t = Turtle()
# t2 = Turtle()

# my_screen = Screen()
# t.shape("turtle")
# t2.shape("square")

# t.forward(100)
# t.left(120)
# t.forward(100)
# t.left(120)
# t.forward(100)
# t.left(60)
# t.forward(100)
# t.left(120)
# t.forward(100)

""" Accessing Object Attribute """
# print(my_screen.canvheight)
# my_screen.exitonclick()

table = prettytable.PrettyTable()
table.add_column("Pokemon Name", [])
table.add_column("Type", [])

dict = {
    'Pokemon': {
        'Pikachu' : "Electric",
        'Squirtle' : "Water",
        'Charmander': "Fire"
    }
}

for poke_name, type in dict['Pokemon'].items():
    table.add_row([poke_name, type])

table.align = "l"
print(table)