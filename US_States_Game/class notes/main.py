import csv
import pandas

# weather_data = open("weather_data.csv", "r").readlines()
# print(weather_data)
# Similarly you can use:
# with open ("weather_data.csv", "r") as data_file:
#    data = data_file.readlines()
# print(data)

# data = []
# with open("weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    temperature = []
#    for row in data:
#        if row[1] != "temp":
#            temperature.append(int(row[1]))
#        print(temperature)

# data = pandas.read_csv("weather_data.csv")
# print(type(data), data)

# operations on columns
# temp_list = data["temp"].to_list()
# print(f" Average = {sum(temp_list) / len(temp_list)}")
# average = data["temp"].mean()
# print(f" Average = {average}")
# maximum = data["temp"].max()
# print(f" Maximum = {maximum}")
# print(f" Condition = {data.condition}")

# operations on rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print(monday)
# print(f"Monday's temp in F = {int(monday.temp) * 9/5 + 32}")


# data_dictionary = {
#    "students": ["Chuck", "Amy", "Jeff", "Chris"],
#     "scores": [86, 36, 94, 100]
# }
# student_scores = pandas.DataFrame(data_dictionary)
# print(student_scores)
# student_scores.to_csv("student_scores.csv")

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
# How many Grey, Cinnamon, Black
print(f" Gray squirrels = {gray}")
print(f" Cinnamon squirrels = {cinnamon}")
print(f" Black squirrels = {black}")

data = {
    "colors": ["gray", "cinnamon", "black"],
    "count": [gray, cinnamon, black]
}
data_frame = pandas.DataFrame(data)
data_frame.to_csv("Squirrel count by color.csv")
print(data_frame)

