# from datetime import datetime

# # Lớp DiaChi lưu trữ thông tin về địa chỉ của nhân viên
# class DiaChi:
#     def __init__(self, soNha: str, tenDuong: str, tenQuan: str, thanhPho: str):
#         self.soNha = soNha
#         self.tenDuong = tenDuong
#         self.tenQuan = tenQuan
#         self.thanhPho = thanhPho
    
#     def __str__(self):
#         return f"{self.soNha}, {self.tenDuong}, {self.tenQuan}, {self.thanhPho}"

# # Lớp cơ sở NhanVien chứa thông tin chung về nhân viên
# class NhanVien:
#     def __init__(self, hoTen: str, ngaySinh: datetime, diaChi: DiaChi):
#         self.hoTen = hoTen
#         self.ngaySinh = ngaySinh
#         self.diaChi = diaChi
    
#     def InThongTin(self):
#         print(f"Họ tên: {self.hoTen}")
#         print(f"Ngày sinh: {self.ngaySinh.strftime('%d/%m/%Y')}")
#         print(f"Địa chỉ: {self.diaChi}")

# # Lớp NhanVienSanXuat kế thừa từ lớp NhanVien và có thêm các thuộc tính riêng
# class NhanVienSanXuat(NhanVien):
#     def __init__(self, hoTen: str, ngaySinh: datetime, diaChi: DiaChi, luongCB: float, soSP: int):
#         super().__init__(hoTen, ngaySinh, diaChi)
#         self.luongCB = luongCB
#         self.soSP = soSP
    
#     def TinhLuong(self):
#         return self.luongCB + self.soSP * 5000
    
#     def InThongTin(self):
#         super().InThongTin()
#         print(f"Lương căn bản: {self.luongCB}")
#         print(f"Số sản phẩm: {self.soSP}")
#         print(f"Lương: {self.TinhLuong()}")

# # Lớp NhanVienVanPhong kế thừa từ lớp NhanVien và có thêm thuộc tính riêng
# class NhanVienVanPhong(NhanVien):
#     def __init__(self, hoTen: str, ngaySinh: datetime, diaChi: DiaChi, soNgayLamViec: int):
#         super().__init__(hoTen, ngaySinh, diaChi)
#         self.soNgayLamViec = soNgayLamViec
    
#     def TinhLuong(self):
#         return self.soNgayLamViec * 100000
    
#     def InThongTin(self):
#         super().InThongTin()
#         print(f"Số ngày làm việc: {self.soNgayLamViec}")
#         print(f"Lương: {self.TinhLuong()}")

# # Hàm chính để tạo danh sách nhân viên và in thông tin
# def main():
#     # Tạo danh sách nhân viên sản xuất
#     diaChi1 = DiaChi("123", "Nguyen Trai", "Quan 5", "Ho Chi Minh")
#     nvSanXuat1 = NhanVienSanXuat("Nguyen Van A", datetime(1990, 5, 21), diaChi1, 3000000, 150)
    
#     diaChi2 = DiaChi("456", "Le Loi", "Quan 1", "Ho Chi Minh")
#     nvSanXuat2 = NhanVienSanXuat("Le Thi B", datetime(1985, 12, 1), diaChi2, 2800000, 200)

#     # Tạo danh sách nhân viên văn phòng
#     diaChi3 = DiaChi("789", "Tran Hung Dao", "Quan 3", "Ho Chi Minh")
#     nvVanPhong1 = NhanVienVanPhong("Pham Van C", datetime(1992, 7, 15), diaChi3, 22)
    
#     diaChi4 = DiaChi("321", "Ba Trieu", "Quan 10", "Ho Chi Minh")
#     nvVanPhong2 = NhanVienVanPhong("Tran Thi D", datetime(1993, 9, 30), diaChi4, 25)

#     # In thông tin nhân viên sản xuất
#     print("Thông tin nhân viên sản xuất:")
#     nvSanXuat1.InThongTin()
#     print()  # Dòng trống để phân cách
#     nvSanXuat2.InThongTin()
    
#     print("\nThông tin nhân viên văn phòng:")
#     nvVanPhong1.InThongTin()
#     print()  # Dòng trống để phân cách
#     nvVanPhong2.InThongTin()

# if __name__ == "__main__":
#     main()



from datetime import datetime

# Lớp DiaChi lưu trữ thông tin về địa chỉ của nhân viên
class DiaChi:
    def __init__(self, soNha: str, tenDuong: str, tenQuan: str, thanhPho: str):
        self.soNha = soNha
        self.tenDuong = tenDuong
        self.tenQuan = tenQuan
        self.thanhPho = thanhPho
    
    def __str__(self):
        return f"{self.soNha}, {self.tenDuong}, {self.tenQuan}, {self.thanhPho}"

# Lớp cơ sở NhanVien chứa thông tin chung về nhân viên
class NhanVien:
    def __init__(self, hoTen: str, ngaySinh: datetime, diaChi: DiaChi):
        self.hoTen = hoTen
        self.ngaySinh = ngaySinh
        self.diaChi = diaChi
    
    def InThongTin(self):
        print(f"Họ tên: {self.hoTen}")
        print(f"Ngày sinh: {self.ngaySinh.strftime('%d/%m/%Y')}")
        print(f"Địa chỉ: {self.diaChi}")

# Lớp NhanVienSanXuat kế thừa từ lớp NhanVien và có thêm các thuộc tính riêng
class NhanVienSanXuat(NhanVien):
    def __init__(self, hoTen: str, ngaySinh: datetime, diaChi: DiaChi, luongCB: float, soSP: int):
        super().__init__(hoTen, ngaySinh, diaChi)
        self.luongCB = luongCB
        self.soSP = soSP
    
    def TinhLuong(self):
        return self.luongCB + self.soSP * 5000
    
    def InThongTin(self):
        super().InThongTin()
        print(f"Lương căn bản: {self.luongCB}")
        print(f"Số sản phẩm: {self.soSP}")
        print(f"Lương: {self.TinhLuong()}")

# Lớp NhanVienVanPhong kế thừa từ lớp NhanVien và có thêm thuộc tính riêng
class NhanVienVanPhong(NhanVien):
    def __init__(self, hoTen: str, ngaySinh: datetime, diaChi: DiaChi, soNgayLamViec: int):
        super().__init__(hoTen, ngaySinh, diaChi)
        self.soNgayLamViec = soNgayLamViec
    
    def TinhLuong(self):
        return self.soNgayLamViec * 100000
    
    def InThongTin(self):
        super().InThongTin()
        print(f"Số ngày làm việc: {self.soNgayLamViec}")
        print(f"Lương: {self.TinhLuong()}")

# Hàm để nhập thông tin địa chỉ
def nhapDiaChi():
    soNha = input("Nhập số nhà: ")
    tenDuong = input("Nhập tên đường: ")
    tenQuan = input("Nhập tên quận: ")
    thanhPho = input("Nhập tên thành phố: ")
    return DiaChi(soNha, tenDuong, tenQuan, thanhPho)

# Hàm để nhập thông tin nhân viên sản xuất
def nhapNhanVienSanXuat():
    hoTen = input("Nhập họ tên nhân viên sản xuất: ")
    ngaySinh_str = input("Nhập ngày sinh (dd/mm/yyyy): ")
    ngaySinh = datetime.strptime(ngaySinh_str, '%d/%m/%Y')
    diaChi = nhapDiaChi()
    luongCB = float(input("Nhập lương căn bản: "))
    soSP = int(input("Nhập số sản phẩm: "))
    return NhanVienSanXuat(hoTen, ngaySinh, diaChi, luongCB, soSP)

# Hàm để nhập thông tin nhân viên văn phòng
def nhapNhanVienVanPhong():
    hoTen = input("Nhập họ tên nhân viên văn phòng: ")
    ngaySinh_str = input("Nhập ngày sinh (dd/mm/yyyy): ")
    ngaySinh = datetime.strptime(ngaySinh_str, '%d/%m/%Y')
    diaChi = nhapDiaChi()
    soNgayLamViec = int(input("Nhập số ngày làm việc: "))
    return NhanVienVanPhong(hoTen, ngaySinh, diaChi, soNgayLamViec)

# Hàm chính để tạo danh sách nhân viên và in thông tin
def main():
    danhSachNhanVien = []

    soNhanVienSanXuat = int(input("Nhập số lượng nhân viên sản xuất: "))
    for i in range(soNhanVienSanXuat):
        print(f"\nNhập thông tin nhân viên sản xuất thứ {i+1}:")
        nvSanXuat = nhapNhanVienSanXuat()
        danhSachNhanVien.append(nvSanXuat)

    soNhanVienVanPhong = int(input("Nhập số lượng nhân viên văn phòng: "))
    for i in range(soNhanVienVanPhong):
        print(f"\nNhập thông tin nhân viên văn phòng thứ {i+1}:")
        nvVanPhong = nhapNhanVienVanPhong()
        danhSachNhanVien.append(nvVanPhong)

    print("\nThông tin nhân viên:")
    for nv in danhSachNhanVien:
        nv.InThongTin()
        print()  # Dòng trống để phân cách

if __name__ == "__main__":
    main()
