# # Giao diện PhiKinhDoanh chứa chức năng tính phí kinh doanh
# class PhiKinhDoanh:
#     def TinhPhiKinhDoanh(self):
#         raise NotImplementedError("Phương thức này cần được triển khai trong các lớp con")

# # Lớp cha BatDongSan chứa các thuộc tính và phương thức chung
# class BatDongSan:
#     def __init__(self, maSo: str, chieuDai: float, chieuRong: float):
#         self.maSo = maSo
#         self.chieuDai = chieuDai
#         self.chieuRong = chieuRong
    
#     def DienTich(self):
#         return self.chieuDai * self.chieuRong

#     def InThongTin(self):
#         print(f"Mã số: {self.maSo}")
#         print(f"Chiều dài: {self.chieuDai}")
#         print(f"Chiều rộng: {self.chieuRong}")
#         print(f"Diện tích: {self.DienTich()}")

#     def TinhGiaTri(self):
#         raise NotImplementedError("Phương thức này cần được triển khai trong các lớp con")

# # Lớp con DatTrong kế thừa từ BatDongSan
# class DatTrong(BatDongSan):
#     def TinhGiaTri(self):
#         return self.DienTich() * 30_000_000

#     def InThongTin(self):
#         super().InThongTin()
#         print(f"Giá trị đất trồng: {self.TinhGiaTri()}")

# # Lớp con NhaO kế thừa từ BatDongSan
# class NhaO(BatDongSan):
#     def __init__(self, maSo: str, chieuDai: float, chieuRong: float, soLau: int):
#         super().__init__(maSo, chieuDai, chieuRong)
#         self.soLau = soLau
    
#     def TinhGiaTri(self):
#         return self.DienTich() * 60_000_000 + self.soLau * 100_000_000

#     def InThongTin(self):
#         super().InThongTin()
#         print(f"Số lầu: {self.soLau}")
#         print(f"Giá trị nhà ở: {self.TinhGiaTri()}")

# # Lớp con BietThu kế thừa từ BatDongSan và triển khai giao diện PhiKinhDoanh
# class BietThu(BatDongSan, PhiKinhDoanh):
#     def TinhGiaTri(self):
#         return self.DienTich() * 100_000_000

#     def TinhPhiKinhDoanh(self):
#         return self.chieuRong * 5000

#     def InThongTin(self):
#         super().InThongTin()
#         print(f"Giá trị biệt thự: {self.TinhGiaTri()}")
#         print(f"Phí kinh doanh: {self.TinhPhiKinhDoanh()}")

# # Lớp con KhachSan kế thừa từ BatDongSan và triển khai giao diện PhiKinhDoanh
# class KhachSan(BatDongSan, PhiKinhDoanh):
#     def __init__(self, maSo: str, chieuDai: float, chieuRong: float, soSao: int):
#         super().__init__(maSo, chieuDai, chieuRong)
#         self.soSao = soSao
    
#     def TinhGiaTri(self):
#         return self.DienTich() * 70_000_000 + self.soSao * 50_000_000

#     def TinhPhiKinhDoanh(self):
#         return self.chieuRong * 10000

#     def InThongTin(self):
#         super().InThongTin()
#         print(f"Số sao: {self.soSao}")
#         print(f"Giá trị khách sạn: {self.TinhGiaTri()}")
#         print(f"Phí kinh doanh: {self.TinhPhiKinhDoanh()}")

# # Hàm nhập bất động sản từ bàn phím
# def NhapBatDongSan():
#     loai = input("Nhập loại bất động sản (DatTrong, NhaO, BietThu, KhachSan): ")
#     maSo = input("Nhập mã số: ")
#     chieuDai = float(input("Nhập chiều dài: "))
#     chieuRong = float(input("Nhập chiều rộng: "))
    
#     if loai == "DatTrong":
#         return DatTrong(maSo, chieuDai, chieuRong)
    
#     elif loai == "NhaO":
#         soLau = int(input("Nhập số lầu: "))
#         return NhaO(maSo, chieuDai, chieuRong, soLau)
    
#     elif loai == "BietThu":
#         return BietThu(maSo, chieuDai, chieuRong)
    
#     elif loai == "KhachSan":
#         soSao = int(input("Nhập số sao: "))
#         return KhachSan(maSo, chieuDai, chieuRong, soSao)
    
#     else:
#         print("Loại bất động sản không hợp lệ!")
#         return None

# # Hàm chính quản lý danh sách bất động sản và các chức năng theo yêu cầu
# def main():
#     danhSachBDS = []

#     # Nhập danh sách bất động sản từ bàn phím
#     soLuong = int(input("Nhập số lượng bất động sản cần nhập: "))
#     for i in range(soLuong):
#         print(f"\nNhập thông tin bất động sản thứ {i+1}:")
#         bds = NhapBatDongSan()
#         if bds is not None:
#             danhSachBDS.append(bds)

#     # a) In thông tin danh sách bất động sản
#     print("\nDanh sách bất động sản:")
#     for bds in danhSachBDS:
#         bds.InThongTin()
#         print()  # Dòng trống để phân cách

#     # b) Cho biết số lượng bất động sản theo từng loại
#     soLuongDatTrong = len([bds for bds in danhSachBDS if isinstance(bds, DatTrong)])
#     soLuongNhaO = len([bds for bds in danhSachBDS if isinstance(bds, NhaO)])
#     soLuongBietThu = len([bds for bds in danhSachBDS if isinstance(bds, BietThu)])
#     soLuongKhachSan = len([bds for bds in danhSachBDS if isinstance(bds, KhachSan)])

#     print(f"Số lượng Đất Trồng: {soLuongDatTrong}")
#     print(f"Số lượng Nhà Ở: {soLuongNhaO}")
#     print(f"Số lượng Biệt Thự: {soLuongBietThu}")
#     print(f"Số lượng Khách Sạn: {soLuongKhachSan}")

#     # c) In ra danh sách bất động sản có diện tích trên 1000
#     print("\nBất động sản có diện tích trên 1000:")
#     for bds in danhSachBDS:
#         if bds.DienTich() > 1000:
#             bds.InThongTin()
#             print()

#     # d) Tính tổng phí kinh doanh thu được
#     tongPhiKinhDoanh = sum(bds.TinhPhiKinhDoanh() for bds in danhSachBDS if isinstance(bds, PhiKinhDoanh))
#     print(f"Tổng phí kinh doanh thu được: {tongPhiKinhDoanh}")

# if __name__ == "__main__":
#     main()


# Giao diện PhiKinhDoanh chứa chức năng tính phí kinh doanh
class PhiKinhDoanh:
    def TinhPhiKinhDoanh(self):
        raise NotImplementedError("Phương thức này cần được triển khai trong các lớp con")

# Lớp cha BatDongSan chứa các thuộc tính và phương thức chung
class BatDongSan:
    def __init__(self, maSo: str, chieuDai: float, chieuRong: float):
        self.maSo = maSo
        self.chieuDai = chieuDai
        self.chieuRong = chieuRong
    
    def DienTich(self):
        return self.chieuDai * self.chieuRong

    def InThongTin(self):
        print(f"Mã số: {self.maSo}")
        print(f"Chiều dài: {self.chieuDai}")
        print(f"Chiều rộng: {self.chieuRong}")
        print(f"Diện tích: {self.DienTich()}")

    def TinhGiaTri(self):
        raise NotImplementedError("Phương thức này cần được triển khai trong các lớp con")

# Lớp con DatTrong kế thừa từ BatDongSan
class DatTrong(BatDongSan):
    def TinhGiaTri(self):
        return self.DienTich() * 30_000_000

    def InThongTin(self):
        super().InThongTin()
        print(f"Giá trị đất trồng: {self.TinhGiaTri()}")

# Lớp con NhaO kế thừa từ BatDongSan
class NhaO(BatDongSan):
    def __init__(self, maSo: str, chieuDai: float, chieuRong: float, soLau: int):
        super().__init__(maSo, chieuDai, chieuRong)
        self.soLau = soLau
    
    def TinhGiaTri(self):
        return self.DienTich() * 60_000_000 + self.soLau * 100_000_000

    def InThongTin(self):
        super().InThongTin()
        print(f"Số lầu: {self.soLau}")
        print(f"Giá trị nhà ở: {self.TinhGiaTri()}")

# Lớp con BietThu kế thừa từ BatDongSan và triển khai giao diện PhiKinhDoanh
class BietThu(BatDongSan, PhiKinhDoanh):
    def TinhGiaTri(self):
        return self.DienTich() * 100_000_000

    def TinhPhiKinhDoanh(self):
        return self.chieuRong * 5000

    def InThongTin(self):
        super().InThongTin()
        print(f"Giá trị biệt thự: {self.TinhGiaTri()}")
        print(f"Phí kinh doanh: {self.TinhPhiKinhDoanh()}")

# Lớp con KhachSan kế thừa từ BatDongSan và triển khai giao diện PhiKinhDoanh
class KhachSan(BatDongSan, PhiKinhDoanh):
    def __init__(self, maSo: str, chieuDai: float, chieuRong: float, soSao: int):
        super().__init__(maSo, chieuDai, chieuRong)
        self.soSao = soSao
    
    def TinhGiaTri(self):
        return self.DienTich() * 70_000_000 + self.soSao * 50_000_000

    def TinhPhiKinhDoanh(self):
        return self.chieuRong * 10000

    def InThongTin(self):
        super().InThongTin()
        print(f"Số sao: {self.soSao}")
        print(f"Giá trị khách sạn: {self.TinhGiaTri()}")
        print(f"Phí kinh doanh: {self.TinhPhiKinhDoanh()}")

# Hàm chính quản lý danh sách bất động sản và các chức năng theo yêu cầu
def main():
    danhSachBDS = []

    # Nhập một số bất động sản vào danh sách
    dat1 = DatTrong("DT001", 100, 50)
    nha1 = NhaO("NO001", 80, 40, 3)
    bietThu1 = BietThu("BT001", 120, 60)
    khachSan1 = KhachSan("KS001", 150, 70, 5)

    # Thêm vào danh sách bất động sản
    danhSachBDS.append(dat1)
    danhSachBDS.append(nha1)
    danhSachBDS.append(bietThu1)
    danhSachBDS.append(khachSan1)

    # a) In thông tin danh sách bất động sản
    print("Danh sách bất động sản:")
    for bds in danhSachBDS:
        bds.InThongTin()
        print()  # Dòng trống để phân cách

    # b) Cho biết số lượng bất động sản theo từng loại
    soLuongDatTrong = len([bds for bds in danhSachBDS if isinstance(bds, DatTrong)])
    soLuongNhaO = len([ bds for bds in danhSachBDS if isinstance(bds, NhaO)])
    soLuongBietThu = len([bds for bds in danhSachBDS if isinstance(bds, BietThu)])
    soLuongKhachSan = len([bds for bds in danhSachBDS if isinstance(bds, KhachSan)])

    print(f"Số lượng Đất Trồng: {soLuongDatTrong}")
    print(f"Số lượng Nhà Ở: {soLuongNhaO}")
    print(f"Số lượng Biệt Thự: {soLuongBietThu}")
    print(f"Số lượng Khách Sạn: {soLuongKhachSan}")

    # c) In ra danh sách bất động sản có diện tích trên 1000
    print("\nBất động sản có diện tích trên 1000:")
    for bds in danhSachBDS:
        if bds.DienTich() > 1000:
            bds.InThongTin()
            print()

    # d) Tính tổng phí kinh doanh thu được
    tongPhiKinhDoanh = sum(bds.TinhPhiKinhDoanh() for bds in danhSachBDS if isinstance(bds, PhiKinhDoanh))
    print(f"Tổng phí kinh doanh thu được: {tongPhiKinhDoanh}")

if __name__ == "__main__":
    main()
