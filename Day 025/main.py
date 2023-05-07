# with open(r"Udemy - 100 days of Python\Day 25\weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# import csv

# with open(r"Udemy - 100 days of Python\Day 25\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

data = pandas.read_csv("Udemy - 100 days of Python\Day 25\weather_data.csv")
print(data)
# print(type(data))
# print(data["temp"])
# print(type(data["temp"]))