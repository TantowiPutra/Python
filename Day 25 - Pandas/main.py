
# with open("./weather_data.csv") as file:
#     data = [line.strip() for line in file]
#     print(data)

# import csv
#
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

data = pandas.read_csv("./weather_data.csv")
# print(type(data)) -> DataFrame
# print(type(data["temp"])) -> Series
data_dict = data.to_dict()
print(data_dict)

data_list = data["temp"].to_list()
print(data_list)

# Without Series Method
average = sum(data_list) / len(data_list)
print(average)

# With Series Method
average = data['temp'].mean()
print(average)

max_val = data['temp'].max()
print(max_val)

# Get Data In Row
print(data[data.day == "Monday"])
print(data[data.temp == data['temp'].max()])
print(data.temp == data['temp'].max())

# Create Dataframe From Scratch
data_dict = {
    'students': ['A', 'B', 'C'],
    'scores'  : [90, 91, 92]
}

new_data = pandas.DataFrame(data_dict)
print(new_data)
new_data.to_csv("new_data.csv")
