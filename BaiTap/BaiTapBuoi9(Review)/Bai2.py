from datetime import datetime
from abc import ABC, abstractmethod

# Định nghĩa lớp Address (Địa chỉ)
class Address:
    def __init__(self, s="", d="", q="", tp=""):
        self.s = s  # Số nhà
        self.d = d  # Tên đường
        self.q = q  # Quận
        self.tp = tp  # Thành phố

    def nhap(self):
        self.s = input("Nhập số nhà: ")
        self.d = input("Nhập tên đường: ")
        self.q = input("Nhập tên quận: ")
        self.tp = input("Nhập tên thành phố: ")

    def __str__(self):
        return f"Số nhà: {self.s}, Đường: {self.d}, Quận: {self.q}, Thành phố: {self.tp}"


# Định nghĩa lớp nhân viên chung (Abstract Class)
class Employee(ABC):
    def __init__(self, n="", d=None, a=None):
        self.n = n  # Tên nhân viên
        self.d = d  # Ngày sinh (kiểu datetime)
        self.a = a if a else Address()  # Địa chỉ (mặc định là một đối tượng Address rỗng)

    def __str__(self):
        return f"Tên: {self.n}, Ngày sinh: {self.d.strftime('%d/%m/%Y')}, Địa chỉ: {self.a}"

    def nhap(self):
        self.n = input("Nhập tên: ")
        ngay_sinh = input("Nhập ngày sinh (dd/mm/yyyy): ")
        self.d = datetime.strptime(ngay_sinh, "%d/%m/%Y")
        self.a.nhap()

    @abstractmethod
    def tinhLuong(self):
        pass


def nhap(self):
    self.n = n 
    ngaysinh = input("Nhap ngay sinh (dd/mm/yyyy): ")
    self.d = datetime.strptime(ngaysinh, "%d/%m/%Y")
# Nhân viên văn phòng
class OfficeEmployee(Employee):
    def __init__(self, n="", d=None, a=None, l=0, sp=0):
        super().__init__(n, d, a)
        self.l = l  # Lương cơ bản
        self.sp = sp  # Số sản phẩm

    def __str__(self):
        return f"{super().__str__()}, Lương cơ bản: {self.l}, Số sản phẩm: {self.sp}"

    def nhap(self):
        super().nhap()
        self.l = float(input("Nhập lương cơ bản: "))
        self.sp = int(input("Nhập số lượng sản phẩm: "))

    def tinhLuong(self):
        return self.l + self.sp * 5000


# Nhân viên sản xuất
class ProductionEmployee(Employee):
    def __init__(self, n="", d=None, a=None, s=0):
        super().__init__(n, d, a)
        self.s = s  # Số ngày làm việc

    def __str__(self):
        return f"{super().__str__()}, Số ngày làm việc: {self.s}"

    def nhap(self):
        super().nhap()
        self.s = int(input("Nhập số ngày làm việc: "))

    def tinhLuong(self):
        return self.s * 100000


def main():
    employees = []

    n = int(input("Nhập số lượng nhân viên: "))

    for i in range(n):
        print(f"Nhập thông tin nhân viên thứ {i + 1}: ")
        print("1. Nhân viên văn phòng")
        print("2. Nhân viên sản xuất")
        choice = int(input("Chọn loại nhân viên (1 hoặc 2): "))

        if choice == 1:
            emp = OfficeEmployee()
            emp.nhap()
            employees.append(emp)
        elif choice == 2:
            emp = ProductionEmployee()
            emp.nhap()
            employees.append(emp)
        else:
            print("Lựa chọn không hợp lệ! Bỏ qua nhân viên này.")

    print("\nDanh sách nhân viên:")
    for emp in employees:
        print(emp)
        print(f"Lương: {emp.tinhLuong():,.0f} VND")


if __name__ == "__main__":
    main()
