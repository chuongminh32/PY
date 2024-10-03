import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    # lay data
    def get_radius(self):
        return self.__radius
    #sua data
    def set_radius(self, new_raidus):
        self.__radius = new_raidus
    # Hàm tính chu vi hình tròn
    def calculate_circumference(self):
        return 2 * math.pi * self.__radius

    # Hàm tính diện tích hình tròn
    def calculate_area(self):
        return math.pi * self.__radius ** 2

    # Hàm hiển thị thông tin về hình tròn
    def display_info(self):
        print(f"Hình tròn có bán kính: {self.__radius}")
        print(f"Chu vi: {self.calculate_circumference():.2f}")
        print(f"Diện tích: {self.calculate_area():.2f}")

# Tạo đối tượng hình tròn và hiển thị thông tin
circle = Circle(5)
circle.display_info()
