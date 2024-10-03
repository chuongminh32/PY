# x0 = x1 = float(input('nhap x '))
# y0 = y1 = float(input('nhap y '))
# s = 0.0

# while True:
#     x2 = input('nhap x ')
#     if x2 == ' ':
#         break
#     y2 = float(input('nhap y '))
#     x2 = float(x2)

#     s += ((x1 - x2)**2 + (y1 - y2)**2)**0.5
#     x1, y1 = x2, y2

# # tinh canh cuoi cung
# s += ((x0 - x1)**2 + (y0 - y1)**2)**0.5
# print(s)


# # import math


# # def calculate_distance(p1, p2):
# #     return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


# # def main():
# #     points = []
# #     while True:
# #         x = input("Nhập tọa độ x (hoặc nhấn khoảng trắng để kết thúc): ")
# #         if x.strip() == "":
# #             break
# #         y = input("Nhập tọa độ y: ")
# #         points.append((float(x), float(y)))

# #     if len(points) < 2:
# #         print("Không đủ tọa độ để tạo thành một đa giác.")
# #         return

# #     # Tính chu vi
# #     perimeter = 0
# #     for i in range(len(points)):
# #         perimeter += calculate_distance(points[i],
# #                                         points[(i + 1) % len(points)])


# #     # Hiển thị kết quả
# #     print("\nCác tọa độ của đa giác:")
# #     for point in points:
# #         print(f"({point[0]}, {point[1]})")


# #     print(f"\nChu vi của đa giác là: {perimeter:.2f}")


# # if __name__ == "__main__":
# #     main()
