import pandas

squirrel_data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

print("======================================")
counts = squirrel_data["Primary Fur Color"].value_counts()
print(counts)

print("======================================")
counts = squirrel_data.groupby("Primary Fur Color").size()
print(counts, type(counts))
print("======================================")
counts = (
    squirrel_data[["Primary Fur Color", "Age"]]
        .groupby("Primary Fur Color")
)
print(counts.get_group("Gray"))
print("======================================")
gray_squirrels_count = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Gray']['Primary Fur Color'])
red_squirrels_count = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Cinnamon']['Primary Fur Color'])
black_squirrels_count = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Black']['Primary Fur Color'])

data = {
    'Color': [
        'Gray',
        'Cinnamon',
        'Black'
    ],
    'Count': [
        gray_squirrels_count,
        red_squirrels_count,
        black_squirrels_count
    ]
}

squirrel_count = pandas.DataFrame(data)
print(squirrel_count)