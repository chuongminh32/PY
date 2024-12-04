# from abc import ABC, abstractmethod
# import math

# # Lớp trừu tượng cho các hình
# class Shape(ABC):
#     @abstractmethod
#     def calculate_perimeter(self):
#         pass

#     @abstractmethod
#     def calculate_area(self):
#         pass

#     @abstractmethod
#     def display_info(self):
#         pass

# # Hình tròn kế thừa từ lớp Shape
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def calculate_perimeter(self):
#         return 2 * math.pi * self.radius

#     def calculate_area(self):
#         return math.pi * self.radius ** 2

#     def display_info(self):
#         print(f"Hình tròn có bán kính: {self.radius}")
#         print(f"Chu vi: {self.calculate_perimeter():.2f}")
#         print(f"Diện tích: {self.calculate_area():.2f}")

# # Hình chữ nhật kế thừa từ lớp Shape
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def calculate_perimeter(self):
#         return 2 * (self.width + self.height)

#     def calculate_area(self):
#         return self.width * self.height

#     def display_info(self):
#         print(f"Hình chữ nhật có chiều rộng: {self.width} và chiều cao: {self.height}")
#         print(f"Chu vi: {self.calculate_perimeter():.2f}")
#         print(f"Diện tích: {self.calculate_area():.2f}")

# # Hình tam giác kế thừa từ lớp Shape
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def calculate_perimeter(self):
#         return self.a + self.b + self.c

#     def calculate_area(self):
#         # Sử dụng công thức Heron để tính diện tích tam giác
#         s = self.calculate_perimeter() / 2
#         return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

#     def display_info(self):
#         print(f"Hình tam giác có các cạnh: {self.a}, {self.b}, {self.c}")
#         print(f"Chu vi: {self.calculate_perimeter():.2f}")
#         print(f"Diện tích: {self.calculate_area():.2f}")

# # Tạo các đối tượng cho từng loại hình và hiển thị thông tin
# shapes = [
#     Circle(5),
#     Rectangle(4, 7),
#     Triangle(3, 4, 5)
# ]

# for shape in shapes:
#     shape.display_info()
#     print('------------------------')


