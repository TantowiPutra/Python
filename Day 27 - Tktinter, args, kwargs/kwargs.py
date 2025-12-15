def calculate(**kwargs):
    print(type(kwargs)) # Dictionary
    print(kwargs)

calculate(name="Tantowi", age="24")
calculate(**{
    'name': 'Tantowi',
    'age' : 24
}) # Unpack Dictionary agar bisa diakses kwargs
