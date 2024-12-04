from datetime import datetime

# Lớp GiaoDich - lớp cơ sở
class GiaoDich:
    def __init__(self, ma_gd, ngay_gd, don_gia, so_luong):
        self.ma_gd = ma_gd  # Mã giao dịch
        self.ngay_gd = datetime.strptime(ngay_gd, "%d/%m/%Y")  # Ngày giao dịch
        self.don_gia = don_gia  # Đơn giá
        self.so_luong = so_luong  # Số lượng

    def thanh_tien(self):
        pass  # Sẽ được định nghĩa lại trong lớp kế thừa

    def __str__(self):
        return f"Mã GD: {self.ma_gd}, Ngày: {self.ngay_gd.strftime('%d/%m/%Y')}, Đơn giá: {self.don_gia}, Số lượng: {self.so_luong}"

# Lớp GiaoDichVang - lớp con kế thừa từ GiaoDich
class GiaoDichVang(GiaoDich):
    def __init__(self, ma_gd, ngay_gd, don_gia, so_luong, loai_vang):
        super().__init__(ma_gd, ngay_gd, don_gia, so_luong)
        self.loai_vang = loai_vang  # Loại vàng (18k, 24k, 9999)

    def thanh_tien(self):
        return self.so_luong * self.don_gia  # Thành tiền = số lượng * đơn giá

    def __str__(self):
        return f"{super().__str__()}, Loại vàng: {self.loai_vang}, Thành tiền: {self.thanh_tien()}"

# Lớp GiaoDichTienTe - lớp con kế thừa từ GiaoDich
class GiaoDichTienTe(GiaoDich):
    def __init__(self, ma_gd, ngay_gd, don_gia, so_luong, loai_tien_te, loai_gd):
        super().__init__(ma_gd, ngay_gd, don_gia, so_luong)
        self.loai_tien_te = loai_tien_te  # Loại tiền tệ (USD, EUR, AUD)
        self.loai_gd = loai_gd  # Loại giao dịch (mua/bán)

    def thanh_tien(self):
        if self.loai_gd == "mua":
            return self.so_luong * self.don_gia  # Mua: Thành tiền = số lượng * tỷ giá
        elif self.loai_gd == "bán":
            return self.so_luong * self.don_gia * 1.05  # Bán: Thành tiền = (số lượng * tỷ giá) * 1.05
        return 0

    def __str__(self):
        return f"{super().__str__()}, Loại tiền tệ: {self.loai_tien_te}, Loại GD: {self.loai_gd}, Thành tiền: {self.thanh_tien()}"

# Lớp quản lý danh sách giao dịch
class QuanLyGiaoDich:
    def __init__(self):
        self.danh_sach_gd = []  # Danh sách các giao dịch

    def them_giao_dich(self, giao_dich):
        self.danh_sach_gd.append(giao_dich)

    def xuat_danh_sach(self):
        for gd in self.danh_sach_gd:
            print(gd)

    def tong_so_luong_theo_loai(self):
        tong_so_luong = {"Vàng": 0, "Tiền tệ": 0}
        for gd in self.danh_sach_gd:
            if isinstance(gd, GiaoDichVang):
                tong_so_luong["Vàng"] += gd.so_luong
            elif isinstance(gd, GiaoDichTienTe):
                tong_so_luong["Tiền tệ"] += gd.so_luong
        print(f"Tổng số lượng giao dịch vàng: {tong_so_luong['Vàng']}")
        print(f"Tổng số lượng giao dịch tiền tệ: {tong_so_luong['Tiền tệ']}")

    def tong_thanh_tien_theo_loai(self):
        tong_thanh_tien = {"Vàng": 0, "Tiền tệ": 0}
        for gd in self.danh_sach_gd:
            if isinstance(gd, GiaoDichVang):
                tong_thanh_tien["Vàng"] += gd.thanh_tien()
            elif isinstance(gd, GiaoDichTienTe):
                tong_thanh_tien["Tiền tệ"] += gd.thanh_tien()
        print(f"Tổng thành tiền giao dịch vàng: {tong_thanh_tien['Vàng']}")
        print(f"Tổng thành tiền giao dịch tiền tệ: {tong_thanh_tien['Tiền tệ']}")

# Hàm hiển thị menu và xử lý lựa chọn của người dùng
def show_menu():
    print("\n----- MENU -----")
    print("1. Thêm giao dịch vàng")
    print("2. Thêm giao dịch tiền tệ")
    print("3. Xuất danh sách giao dịch")
    print("4. Tính tổng số lượng giao dịch theo loại")
    print("5. Tính tổng thành tiền giao dịch theo loại")
    print("0. Thoát")
    choice = input("Chọn chức năng (0-5): ")
    return choice

def main():
    qlgd = QuanLyGiaoDich()

    while True:
        choice = show_menu()

        if choice == "1":
            ma_gd = input("Nhập mã giao dịch: ")
            ngay_gd = input("Nhập ngày giao dịch (dd/mm/yyyy): ")
            don_gia = float(input("Nhập đơn giá: "))
            so_luong = float(input("Nhập số lượng: "))
            loai_vang = input("Nhập loại vàng (18k/24k/9999): ")
            gd_vang = GiaoDichVang(ma_gd, ngay_gd, don_gia, so_luong, loai_vang)
            qlgd.them_giao_dich(gd_vang)
            print("Giao dịch vàng đã được thêm.")

        elif choice == "2":
            ma_gd = input("Nhập mã giao dịch: ")
            ngay_gd = input("Nhập ngày giao dịch (dd/mm/yyyy): ")
            don_gia = float(input("Nhập đơn giá (tỷ giá): "))
            so_luong = float(input("Nhập số lượng: "))
            loai_tien_te = input("Nhập loại tiền tệ (USD/EUR/AUD): ")
            loai_gd = input("Nhập loại giao dịch (mua/bán): ")
            gd_tt = GiaoDichTienTe(ma_gd, ngay_gd, don_gia, so_luong, loai_tien_te, loai_gd)
            qlgd.them_giao_dich(gd_tt)
            print("Giao dịch tiền tệ đã được thêm.")

        elif choice == "3":
            print("\nDanh sách giao dịch:")
            qlgd.xuat_danh_sach()

        elif choice == "4":
            print("\nTính tổng số lượng giao dịch theo loại:")
            qlgd.tong_so_luong_theo_loai()

        elif choice == "5":
            print("\nTính tổng thành tiền giao dịch theo loại:")
            qlgd.tong_thanh_tien_theo_loai()

        elif choice == "0":
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()
