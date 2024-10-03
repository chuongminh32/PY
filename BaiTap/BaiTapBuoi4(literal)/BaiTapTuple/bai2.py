# print("Press Ente(x2) to stop!")
# print("name,age,score:\n")
# data_input = input()
# tpl = []
# data = []
# while data_input != "":
#     tpl = data_input.split(",")
#     t = tuple(tpl)
#     data.append(t)
#     data_input = input()


# for i in range(len(data)):
#     min_index = i
#     for j in range(i+1, len(data)):
#         if data[j][0] < data[min_index][0] or \
#             (data[j][0] == data[min_index][0] and int(data[j][1]) < int(data[min_index][1])) or \
#                 (data[j][0] == data[min_index][0] and int(data[j][1]) == int(data[min_index][1]) and int(data[j][2]) < int(data[min_index][2])):
#             min_index = j

#         data[min_index], data[i] = data[i], data[min_index]

# print(data)
