import math

class Triangle:
    def __init__(self, side1, side2, side3, color):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.color = color

    # Hàm tính chu vi
    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

    # Hàm tính diện tích bằng công thức Heron
    def calculate_area(self):
        s = self.calculate_perimeter() / 2
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return area

    # Hàm hiển thị thông tin tam giác
    def display_info(self):
        print(f"Tam giác với các cạnh: {self.side1}, {self.side2}, {self.side3}")
        print(f"Màu sắc: {self.color}")
        print(f"Chu vi: {self.calculate_perimeter()}")
        print(f"Diện tích: {self.calculate_area():.2f}")
        print(f"Loại tam giác: {self.triangle_type()}")

    # Hàm hiển thị loại tam giác
    def triangle_type(self):
        a, b, c = sorted([self.side1, self.side2, self.side3])  # Sắp xếp các cạnh để so sánh dễ hơn
        if a + b <= c:
            return "Không phải tam giác hợp lệ"
        elif a == b == c:
            return "Tam giác đều"
        elif a == b or b == c:
            if c**2 == a**2 + b**2:
                return "Tam giác vuông cân"
            return "Tam giác cân"
        elif c**2 == a**2 + b**2:
            return "Tam giác vuông"
        else:
            return "Tam giác thường"

# Tạo đối tượng tam giác và hiển thị thông tin
triangle = Triangle(3, 4, 5, "Xanh")
triangle.display_info()
