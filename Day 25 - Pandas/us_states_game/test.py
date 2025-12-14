import pandas

data = pandas.read_csv("./50_states.csv")
print(data[data.state != 'Wyoming'])