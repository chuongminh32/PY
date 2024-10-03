# def filter_speeds(speeds, min_speed):
#     # Danh sách lưu trữ các tốc độ nhỏ hơn min
#     filtered_speeds = []
#     # Danh sách lưu trữ chỉ số của các tốc độ nhỏ hơn min
#     indices = []

#     for index, speed in enumerate(speeds):
#         if speed < min_speed:
#             filtered_speeds.append(speed)
#             indices.append(index)

#     return filtered_speeds, indices

# # Ví dụ sử dụng
# speeds = [1500, 2000, 1200, 1800, 900]
# min_speed = 1300
# result = filter_speeds(speeds, min_speed)
# print("Tốc độ nhỏ hơn min:", result[0])
# print("Chỉ số của các tốc độ nhỏ hơn min:", result[1])
