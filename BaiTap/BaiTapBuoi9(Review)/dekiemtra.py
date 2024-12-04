class Phong:
    def __init__(self, ma_phong, day_nha, dien_tich, so_bong_den):
        self.ma_phong = ma_phong
        self.day_nha = day_nha
        self.dien_tich = dien_tich
        self.so_bong_den = so_bong_den

    def dat_chuan(self):
        return self.so_bong_den / self.dien_tich >= 1 / 10

    def __str__(self):
        return f"Mã phòng: {self.ma_phong}, Dãy nhà: {self.day_nha}, Diện tích: {self.dien_tich}, Số bóng đèn: {self.so_bong_den}"

class PhongLyThuyet(Phong):
    def __init__(self, ma_phong, day_nha, dien_tich, so_bong_den, co_may_chieu):
        super().__init__(ma_phong, day_nha, dien_tich, so_bong_den)
        self.co_may_chieu = co_may_chieu

    def dat_chuan(self):
        return super().dat_chuan() and self.co_may_chieu

    def __str__(self):
        return super().__str__() + f", Có máy chiếu: {'Có' if self.co_may_chieu else 'Không'}"

class PhongMayTinh(Phong):
    def __init__(self, ma_phong, day_nha, dien_tich, so_bong_den, so_may_tinh):
        super().__init__(ma_phong, day_nha, dien_tich, so_bong_den)
        self.so_may_tinh = so_may_tinh

    def dat_chuan(self):
        return super().dat_chuan() and self.dien_tich / self.so_may_tinh >= 1.5

    def __str__(self):
        return super().__str__() + f", Số máy tính: {self.so_may_tinh}"

class QuanLyPhong:
    def __init__(self):
        self.danh_sach_phong = []

    def them_phong(self, phong):
        if any(p.ma_phong == phong.ma_phong for p in self.danh_sach_phong):
            print(f"Phòng mã {phong.ma_phong} đã tồn tại!")
        else:
            self.danh_sach_phong.append(phong)

    def tim_phong(self, ma_phong):
        for p in self.danh_sach_phong:
            if p.ma_phong == ma_phong:
                return p
        return None

    def lay_tat_ca_phong(self):
        return self.danh_sach_phong

    def lay_phong_dat_chuan(self):
        return [p for p in self.danh_sach_phong if p.dat_chuan()]

    def cap_nhat_so_may_tinh(self, ma_phong, so_may_tinh_moi):
        phong = self.tim_phong(ma_phong)
        if phong and isinstance(phong, PhongMayTinh):
            phong.so_may_tinh = so_may_tinh_moi
            print(f"Cập nhật phòng {ma_phong} với {so_may_tinh_moi} máy tính.")
        else:
            print("Phòng không tồn tại hoặc không phải phòng máy tính.")

    def xoa_phong(self, ma_phong):
        phong = self.tim_phong(ma_phong)
        if phong:
            xac_nhan = input(f"Bạn có chắc chắn muốn xóa phòng {ma_phong}? (y/n): ")
            if xac_nhan.lower() == 'y':
                self.danh_sach_phong.remove(phong)
                print(f"Đã xóa phòng {ma_phong}.")
            else:
                print("Hủy bỏ xóa phòng.")
        else:
            print("Phòng không tồn tại.")

    def tong_so_phong(self):
        return len(self.danh_sach_phong)

    def lay_phong_may_60(self):
        return [p for p in self.danh_sach_phong if isinstance(p, PhongMayTinh) and p.so_may_tinh == 60]

def hien_thi_menu():
    print("1. Thêm phòng")
    print("2. Tìm phòng")
    print("3. Xem tất cả phòng")
    print("4. Xem phòng đạt chuẩn")
    print("5. Cập nhật số máy tính")
    print("6. Xóa phòng")
    print("7. Tổng số phòng")
    print("8. Xem phòng máy tính có 60 máy")
    print("9. Thoát")

def main():
    ql = QuanLyPhong()

    while True:
        hien_thi_menu()
        chon = input("Nhập lựa chọn: ")

        if chon == "1":
            loai_phong = input("Nhập loại phòng (Lý thuyết/Máy tính): ").lower()
            ma_phong = input("Nhập mã phòng: ")
            day_nha = input("Nhập dãy nhà: ")
            dien_tich = float(input("Nhập diện tích: "))
            so_bong_den = int(input("Nhập số bóng đèn: "))

            if loai_phong == "ly thuyet":
                co_may_chieu = input("Có máy chiếu không? (có/không): ").lower() == "có"
                phong = PhongLyThuyet(ma_phong, day_nha, dien_tich, so_bong_den, co_may_chieu)
            elif loai_phong == "may tinh":
                so_may_tinh = int(input("Nhập số máy tính: "))
                phong = PhongMayTinh(ma_phong, day_nha, dien_tich, so_bong_den, so_may_tinh)
            else:
                print("Loại phòng không hợp lệ!")
                continue

            ql.them_phong(phong)

        elif chon == "2":
            ma_phong = input("Nhập mã phòng cần tìm: ")
            phong = ql.tim_phong(ma_phong)
            if phong:
                print(phong)
            else:
                print("Không tìm thấy phòng.")

        elif chon == "3":
            phong = ql.lay_tat_ca_phong()
            for p in phong:
                print(p)

        elif chon == "4":
            phong_dat_chuan = ql.lay_phong_dat_chuan()
            for p in phong_dat_chuan:
                print(p)

        elif chon == "5":
            ma_phong = input("Nhập mã phòng cần cập nhật: ")
            so_may_tinh_moi = int(input("Nhập số máy tính mới: "))
            ql.cap_nhat_so_may_tinh(ma_phong, so_may_tinh_moi)

        elif chon == "6":
            ma_phong = input("Nhập mã phòng cần xóa: ")
            ql.xoa_phong(ma_phong)

        elif chon == "7":
            print(f"Tổng số phòng: {ql.tong_so_phong()}")

        elif chon == "8":
            phong_60_may = ql.lay_phong_may_60()
            for p in phong_60_may:
                print(p)

        elif chon == "9":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()



# Khối Thi, Khu Vực, DH1, DH2, DH3, NT1, NT2, DT, Giới Tính, Điểm ĐH
# cau 2 
# import pandas as pd

# # 1. Nạp dữ liệu và in ra 10 dòng dữ liệu đầu tiên
# def nap_du_lieu(file_path):
#     # Đọc file CSV
#     df = pd.read_csv(file_path)
#     # In ra 10 dòng đầu tiên
#     print(df.head(10))
#     return df

# # 2. Kiểm tra các kiểu dữ liệu của các trường
# def kiem_tra_kieu_du_lieu(df):
#     print("\nKiểu dữ liệu của các trường:")
#     print(df.dtypes)

# # 3. Kiểm tra tổng số dữ liệu trống của các trường dữ liệu
# def kiem_tra_du_lieu_trong(df):
#     print("\nTổng số dữ liệu trống của các trường:")
#     print(df.isnull().sum())

# # 4. Điền vào dữ liệu trống của cột 'DT' bằng giá trị 'K' và chuyển sang dữ liệu chuỗi
# def fill_and_convert_column(df):
#     # Điền vào dữ liệu trống của cột 'DT' bằng 'K'
#     df['DT'].fillna('K', inplace=True)
#     # Chuyển dữ liệu cột 'DT' sang kiểu chuỗi
#     df['DT'] = df['DT'].astype(str)
#     print("\nSau khi điền và chuyển kiểu dữ liệu của cột 'DT':")
#     print(df.head(10))

# # 5. Chuyển dữ liệu khối thi tương ứng và tạo cột 'Điểm ĐH' và 'KQ điểm sàn'
# def convert_khoi_thi_and_calculate(df):
#     # Chuyển dữ liệu khối thi tương ứng
#     khoi_thi_map = {'A': 0, 'A1': 1, 'B': 2, 'C': 3, 'D1': 4}
#     df['Khối Thi'] = df['Khối Thi'].map(khoi_thi_map)
    
#     # Tạo cột Điểm ĐH
#     df['Điểm ĐH'] = df[['DH1', 'DH2', 'DH3']].sum(axis=1)

#     # Tạo cột KQ điểm sàn
#     df['KQ điểm sàn'] = df['Điểm ĐH'].apply(lambda x: 'Đạt sàn' if x >= 15 else 'Không đạt sàn')

#     print("\nSau khi chuyển khối thi và tính Điểm ĐH và KQ điểm sàn:")
#     print(df[['Mã SBD', 'Khối Thi', 'Điểm ĐH', 'KQ điểm sàn']].head(10))

# # Hàm chính để thực hiện các bước
# def main():
#     file_path = 'data.csv'  # Đường dẫn tới file CSV của bạn
#     df = nap_du_lieu(file_path)
    
#     kiem_tra_kieu_du_lieu(df)
#     kiem_tra_du_lieu_trong(df)
    
#     fill_and_convert_column(df)
    
#     convert_khoi_thi_and_calculate(df)

# if __name__ == "__main__":
#     main()




# cau 3 
# import pandas as pd

# # Nạp dữ liệu
# def nap_du_lieu(file_path):
#     df = pd.read_csv(file_path)
#     return df

# # 1. Thống kê các giá trị count, sum, mean, median, min, max của DH1 theo Khối Thi và Khu Vực
# def thong_ke_dh1(df):
#     print("\nThống kê DH1 theo Khối Thi và Khu Vực:")
#     stats = df.groupby(['Khối Thi', 'Khu Vực'])['DH1'].agg(['count', 'sum', 'mean', 'median', 'min', 'max'])
#     print(stats)

# # 2. Trình bày dữ liệu với các biến DH1, DH2, DH3 lớn hơn hoặc bằng 5 và thi khối A
# def du_lieu_dh_lon_hon_5_va_khoi_A(df):
#     print("\nDữ liệu DH1, DH2, DH3 >= 5 và thi khối A:")
#     filtered_df = df[(df['DH1'] >= 5) & (df['DH2'] >= 5) & (df['DH3'] >= 5) & (df['Khối Thi'] == 'A')]
#     print(filtered_df)

# # 3. Tính điểm trung bình 2NT của từng môn và điểm trung bình đại học
# def diem_trung_binh(df):
#     print("\nĐiểm trung bình 2NT của từng môn và điểm trung bình đại học:")
#     df['Trung Binh 2NT'] = df[['NT1', 'NT2']].mean(axis=1)
#     df['Trung Binh Đại Học'] = df[['DH1', 'DH2', 'DH3']].mean(axis=1)
#     print(df[['Mã SBD', 'Trung Binh 2NT', 'Trung Binh Đại Học']].head(10))

# # 4. Thống kê số lượng học sinh Nam và Nữ theo Dân tộc
# def thong_ke_sdt_theo_dt(df):
#     print("\nSố lượng học sinh Nam và Nữ theo Dân tộc:")
#     stats = df.groupby(['DT', 'Giới Tính']).size().unstack(fill_value=0)
#     print(stats)

# # 5. Trình bày dữ liệu số lượng thí sinh từng khu vực dựa trên từng nhóm khối thi
# def thong_ke_khu_vuc_theo_khoi(df):
#     print("\nSố lượng thí sinh từng khu vực dựa trên từng nhóm khối thi:")
#     stats = df.groupby(['Khối Thi', 'Khu Vực']).size().unstack(fill_value=0)
#     print(stats)

# # 6. Trình bày dữ liệu số lượng thí sinh đậu, rớt trên từng nhóm khối thi
# def thong_ke_dau_roc_theo_khoi(df):
#     print("\nSố lượng thí sinh đậu, rớt trên từng nhóm khối thi:")
#     df['KQ Điểm Sàn'] = df['Điểm ĐH'].apply(lambda x: 'Đạt sàn' if x >= 15 else 'Không đạt sàn')
#     stats = df.groupby(['Khối Thi', 'KQ Điểm Sàn']).size().unstack(fill_value=0)
#     print(stats)

# # Hàm chính để thực hiện các bước thống kê
# def main():
#     file_path = 'data.csv'  # Đường dẫn tới file CSV của bạn
#     df = nap_du_lieu(file_path)

#     thong_ke_dh1(df)
#     du_lieu_dh_lon_hon_5_va_khoi_A(df)
#     diem_trung_binh(df)
#     thong_ke_sdt_theo_dt(df)
#     thong_ke_khu_vuc_theo_khoi(df)
#     thong_ke_dau_roc_theo_khoi(df)

# if __name__ == "__main__":
#     main()
