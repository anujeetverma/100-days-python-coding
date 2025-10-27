# # with open('weather_data.csv') as data_file:
# #     data = data_file.readlines()
# # print(data)
#
# # import csv
# # with open('weather_data.csv') as data_file:
# #     data = csv.reader(data_file)
# #     temperature = []
# #     for row in data:
# #         print(row)
# #         if row[1] != "temp":
# #             temperature.append(int(row[1]))
# #     print(temperature)
# #
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data['temp'])
#
# # data_dict = data.to_dict()
# # print(data_dict )
#
# data_list = data['temp'].to_list()
# print(f"avg temp= + {sum(data_list)/len(data_list)}")
# print(data['temp'].mean())
# print(data['temp'].max())
#
# print(data["condition"])
# print(data.condition)
#
# # get data in row
# print(data[data.day == "Tuesday"])
# print(data[data.temp == data.temp.max()])
# print(data[data.temp == data.temp.max()]['day'])
# #temp of monday in farenheit
# print((data[data.day == "Monday"].temp)*1.8 + 32)
#
# data_dict ={
#     "students" : ["Amy", "James","Angela"],
#     "scores" : [76,56,65]
#
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)

import pandas
data = pandas.read_csv("squirrel_count.csv")
squirrel_color= data["Primary Fur Color"]
color_count = data["Primary Fur Color"].value_counts()
print(color_count)
color_count.to_csv("squirrel_color_count.csv")





