import math

class Point:
    def __init__(self, x, y, color):
        self.x = x  # Hoành độ
        self.y = y  # Tung độ
        self.color = color  # Màu sắc của điểm

    # Hàm hiển thị thông tin điểm
    def display_info(self):
        print(f"Điểm: ({self.x}, {self.y}), Màu sắc: {self.color}")

    # Hàm tịnh tiến điểm theo trục hoành
    def TinhTien(self, x_shift):
        self.x += x_shift

    # Hàm tịnh tiến điểm theo cả hai hướng
    def TinhTien(self, x_shift, y_shift=None):
        if y_shift is None:
            self.x += x_shift  # Tịnh tiến chỉ theo trục hoành
        else:
            self.x += x_shift  # Tịnh tiến theo hoành độ
            self.y += y_shift  # Tịnh tiến theo tung độ

    # Hàm tính khoảng cách từ điểm tới gốc tọa độ O(0, 0)
    def KhoangCach1(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    # Hàm tính khoảng cách giữa hai điểm
    def KhoangCach2(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

# Tạo đối tượng điểm và hiển thị thông tin
point1 = Point(3, 4, "Đỏ")
point1.display_info()
print(f"Khoảng cách tới gốc tọa độ O(0, 0): {point1.KhoangCach1():.2f}")

# Tạo một điểm khác và tính khoảng cách giữa hai điểm
point2 = Point(6, 8, "Xanh")
print(f"Khoảng cách giữa hai điểm: {point1.KhoangCach2(point2):.2f}")

# Tịnh tiến điểm 1 theo cả hai hướng
point1.TinhTien(2, 3)
point1.display_info()
