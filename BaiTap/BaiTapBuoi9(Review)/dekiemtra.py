# class Phong:
#     def __init__(self, ma_phong, day_nha, dien_tich, so_bong_den):
#         self.ma_phong = ma_phong
#         self.day_nha = day_nha
#         self.dien_tich = dien_tich
#         self.so_bong_den = so_bong_den

#     def dat_chuan(self):
#         return self.so_bong_den / self.dien_tich >= 1 / 10

#     def __str__(self):
#         return f"Mã phòng: {self.ma_phong}, Dãy nhà: {self.day_nha}, Diện tích: {self.dien_tich}, Số bóng đèn: {self.so_bong_den}"

# class PhongLyThuyet(Phong):
#     def __init__(self, ma_phong, day_nha, dien_tich, so_bong_den, co_may_chieu):
#         super().__init__(ma_phong, day_nha, dien_tich, so_bong_den)
#         self.co_may_chieu = co_may_chieu

#     def dat_chuan(self):
#         return super().dat_chuan() and self.co_may_chieu

#     def __str__(self):
#         return super().__str__() + f", Có máy chiếu: {'Có' if self.co_may_chieu else 'Không'}"

# class PhongMayTinh(Phong):
#     def __init__(self, ma_phong, day_nha, dien_tich, so_bong_den, so_may_tinh):
#         super().__init__(ma_phong, day_nha, dien_tich, so_bong_den)
#         self.so_may_tinh = so_may_tinh

#     def dat_chuan(self):
#         return super().dat_chuan() and self.dien_tich / self.so_may_tinh >= 1.5

#     def __str__(self):
#         return super().__str__() + f", Số máy tính: {self.so_may_tinh}"

# class QuanLyPhong:
#     def __init__(self):
#         self.danh_sach_phong = []

#     def them_phong(self, phong):
#         if any(p.ma_phong == phong.ma_phong for p in self.danh_sach_phong):
#             print(f"Phòng mã {phong.ma_phong} đã tồn tại!")
#         else:
#             self.danh_sach_phong.append(phong)

#     def tim_phong(self, ma_phong):
#         for p in self.danh_sach_phong:
#             if p.ma_phong == ma_phong:
#                 return p
#         return None

#     def lay_tat_ca_phong(self):
#         return self.danh_sach_phong

#     def lay_phong_dat_chuan(self):
#         return [p for p in self.danh_sach_phong if p.dat_chuan()]

#     def cap_nhat_so_may_tinh(self, ma_phong, so_may_tinh_moi):
#         phong = self.tim_phong(ma_phong)
#         if phong and isinstance(phong, PhongMayTinh):
#             phong.so_may_tinh = so_may_tinh_moi
#             print(f"Cập nhật phòng {ma_phong} với {so_may_tinh_moi} máy tính.")
#         else:
#             print("Phòng không tồn tại hoặc không phải phòng máy tính.")

#     def xoa_phong(self, ma_phong):
#         phong = self.tim_phong(ma_phong)
#         if phong:
#             xac_nhan = input(f"Bạn có chắc chắn muốn xóa phòng {ma_phong}? (y/n): ")
#             if xac_nhan.lower() == 'y':
#                 self.danh_sach_phong.remove(phong)
#                 print(f"Đã xóa phòng {ma_phong}.")
#             else:
#                 print("Hủy bỏ xóa phòng.")
#         else:
#             print("Phòng không tồn tại.")

#     def tong_so_phong(self):
#         return len(self.danh_sach_phong)

#     def lay_phong_may_60(self):
#         return [p for p in self.danh_sach_phong if isinstance(p, PhongMayTinh) and p.so_may_tinh == 60]

# def hien_thi_menu():
#     print("1. Thêm phòng")
#     print("2. Tìm phòng")
#     print("3. Xem tất cả phòng")
#     print("4. Xem phòng đạt chuẩn")
#     print("5. Cập nhật số máy tính")
#     print("6. Xóa phòng")
#     print("7. Tổng số phòng")
#     print("8. Xem phòng máy tính có 60 máy")
#     print("9. Thoát")

# def main():
#     ql = QuanLyPhong()

#     while True:
#         hien_thi_menu()
#         chon = input("Nhập lựa chọn: ")

#         if chon == "1":
#             loai_phong = input("Nhập loại phòng (Lý thuyết/Máy tính): ").lower()
#             ma_phong = input("Nhập mã phòng: ")
#             day_nha = input("Nhập dãy nhà: ")
#             dien_tich = float(input("Nhập diện tích: "))
#             so_bong_den = int(input("Nhập số bóng đèn: "))

#             if loai_phong == "ly thuyet":
#                 co_may_chieu = input("Có máy chiếu không? (có/không): ").lower() == "có"
#                 phong = PhongLyThuyet(ma_phong, day_nha, dien_tich, so_bong_den, co_may_chieu)
#             elif loai_phong == "may tinh":
#                 so_may_tinh = int(input("Nhập số máy tính: "))
#                 phong = PhongMayTinh(ma_phong, day_nha, dien_tich, so_bong_den, so_may_tinh)
#             else:
#                 print("Loại phòng không hợp lệ!")
#                 continue

#             ql.them_phong(phong)

#         elif chon == "2":
#             ma_phong = input("Nhập mã phòng cần tìm: ")
#             phong = ql.tim_phong(ma_phong)
#             if phong:
#                 print(phong)
#             else:
#                 print("Không tìm thấy phòng.")

#         elif chon == "3":
#             phong = ql.lay_tat_ca_phong()
#             for p in phong:
#                 print(p)

#         elif chon == "4":
#             phong_dat_chuan = ql.lay_phong_dat_chuan()
#             for p in phong_dat_chuan:
#                 print(p)

#         elif chon == "5":
#             ma_phong = input("Nhập mã phòng cần cập nhật: ")
#             so_may_tinh_moi = int(input("Nhập số máy tính mới: "))
#             ql.cap_nhat_so_may_tinh(ma_phong, so_may_tinh_moi)

#         elif chon == "6":
#             ma_phong = input("Nhập mã phòng cần xóa: ")
#             ql.xoa_phong(ma_phong)

#         elif chon == "7":
#             print(f"Tổng số phòng: {ql.tong_so_phong()}")

#         elif chon == "8":
#             phong_60_may = ql.lay_phong_may_60()
#             for p in phong_60_may:
#                 print(p)

#         elif chon == "9":
#             print("Thoát chương trình.")
#             break
#         else:
#             print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

# if __name__ == "__main__":
#     main()




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












"""
* THEORY 

Demo OOP:
from abc import ABC, abstractmethod


class Common(ABC):
    def __init__(self, id="", d=0, r=0):
        self.id = id
        self.d = d
        self.r = r

    def __str__(self):
        return f"Mã số: {self.id}, Chiều dài: {self.d}, Chiều rộng: {self.r}"

    def nhap(self):
        self.id = input("Nhập ID: ")
        self.d = int(input("Nhập chiều dài: "))
        self.r = int(input("Nhập chiều rộng: "))

    @abstractmethod
    def cal(self):
        pass

    def dienTich(self):
        return self.d * self.r


class DatTrong(Common):
    def cal(self):
        return self.d * self.r * 30000000


class BietThu(Common):
    def phiKinhDoanh(self):
        return self.r * 5000

    def cal(self):
        return self.d * self.r * 100000000


class NhaO(Common):
    def __init__(self, id="", d=0, r=0, soLau=0):
        super().__init__(id, d, r)
        self.soLau = soLau

    def cal(self):
        return self.d * self.r * 60000000 + self.soLau * 100000000

class KhachSan(Common):
    def __init__(self, id="", d=0, r=0, soSao=0):
        super().__init__(id, d, r)
        self.soSao = soSao

    def cal(self):
        return self.d * self.r * 70000000 + self.soSao * 50000000

    def phiKinhDoanh(self):
        return self.r * 10000

class MainClass:
    def __init__(self):
        self.dsBds = []

    def add(self, bds):
        self.dsBds.append(bds)

    def i(self):
        for bds in self.dsBds:
            print(bds)

    def soLuongBdsTheoTungLoai(self):
        cnt_nhaO = 0
        cnt_bietThu = 0
        cnt_khachSan = 0
        cnt_datTrong = 0

        for bds in self.dsBds:
            if isinstance(bds, NhaO):
                cnt_nhaO += 1
            elif isinstance(bds, BietThu):
                cnt_bietThu += 1
            elif isinstance(bds, KhachSan):
                cnt_khachSan += 1
            elif isinstance(bds, DatTrong):
                cnt_datTrong += 1

        print(f"Có {cnt_bietThu} biệt thự, {cnt_nhaO} nhà ở, {cnt_khachSan} khách sạn, {cnt_datTrong} đất trống.")

    def dsBdsCoDienTichTren1000(self):
        result = [bds for bds in self.dsBds if bds.dienTich() > 1000]
        for bds in result:
            print(bds)

    def tongPhiKinhDoanh(self):
        phi = 0
        for bds in self.dsBds:
            if isinstance(bds, BietThu) or isinstance(bds, KhachSan):
                phi += bds.phiKinhDoanh()
        return phi

def inputBds():
    typeBds = input("Nhập loại bất động sản (nhao, biethu, khachsan, dattrong): ").lower()
    id = input("Nhap id: ")
    d = int(input("Nhap chieu dai: "))
    r = int(input("Nhap chieu rong: "))
    if typeBds == "dattrong":
        return DatTrong(id, d, r)
    elif typeBds == "bietthu":
        return BietThu(id, d, r)
    elif typeBds == "nhao":
        soLau = int(input("Nhap so lau: "))
        return NhaO(id, d, r, soLau)
    elif typeBds == "khachsan":
        soSao = int(input("Nhap so sao: "))
        return KhachSan(id,d,r,soSao)
    else: 
        return None


def main():
    dsBds = MainClass()
    n = int(input("Nhập số lượng bất động sản: "))

    for i in range(n):
        print(f"Nhập thông tin cho bất động sản thứ {i + 1}: ")
        dsBds.add(inputBds())

    print("\nDanh sách bất động sản:")
    dsBds.i()

    print("\nThống kê số lượng bất động sản:")
    dsBds.soLuongBdsTheoTungLoai()

    print("\nDanh sách bất động sản có diện tích trên 1000m²:")
    dsBds.dsBdsCoDienTichTren1000()

    print("\nTổng phí kinh doanh:")
    print(f"{dsBds.tongPhiKinhDoanh():,.0f} VND")


if __name__ == "__main__":
    main()



MATPLOTLIB
plt.plot()
Dùng để vẽ đồ thị đường.
Cú pháp: plt.plot(x, y, [format])
x: Dữ liệu cho trục x (có thể là một mảng hoặc một danh sách).
y: Dữ liệu cho trục y.
[format]: Tùy chọn định dạng cho đồ thị (ví dụ: 'r-' cho đường màu đỏ).
Ví dụ:

plt.plot([1, 2, 3], [4, 5, 6], 'g--')  # Vẽ đường kẻ gạch màu xanh lá cây
2. plt.scatter()
Dùng để vẽ biểu đồ phân tán (scatter plot).
Cú pháp: plt.scatter(x, y, [size], [color])
x, y: Dữ liệu điểm tương ứng trên trục x và y.
size: Kích thước của các điểm (tuỳ chọn).
color: Màu sắc của các điểm (tuỳ chọn).
Ví dụ:

plt.scatter([1, 2, 3], [4, 5, 6], color='red')  # Vẽ các điểm đỏ
3. plt.bar()
Dùng để vẽ biểu đồ thanh (bar plot).
Cú pháp: plt.bar(x, height, [width], [color])
x: Các giá trị trên trục x.
height: Chiều cao của các thanh.
width: Chiều rộng của các thanh (tuỳ chọn).
color: Màu sắc của các thanh (tuỳ chọn).
Ví dụ:

plt.bar([1, 2, 3], [4, 5, 6], color='blue')  # Vẽ các thanh màu xanh
4. plt.hist()
Dùng để vẽ biểu đồ histogram.
Cú pháp: plt.hist(data, [bins], [color])
data: Dữ liệu cần phân bố.
bins: Số lượng thùng (tuỳ chọn, mặc định là 10).
color: Màu sắc của các thanh (tuỳ chọn).
Ví dụ:

plt.hist([1, 2, 2, 3, 3, 3, 4], bins=4, color='skyblue')  # Vẽ histogram
5. plt.boxplot()
Dùng để vẽ biểu đồ hộp (box plot).
Cú pháp: plt.boxplot(data)
data: Dữ liệu cần biểu diễn dưới dạng hộp.
Ví dụ:

plt.boxplot([1, 2, 3, 4, 5])  # Vẽ biểu đồ hộp
6. plt.pie()
Dùng để vẽ biểu đồ tròn (pie chart).
Cú pháp: plt.pie(sizes, [labels], [colors], [autopct])
sizes: Giá trị phần trăm hoặc kích thước các phần trong biểu đồ.
labels: Nhãn cho các phần (tuỳ chọn).
colors: Màu sắc của các phần (tuỳ chọn).
autopct: Hiển thị phần trăm trên các phần (tuỳ chọn).
Ví dụ:

plt.pie([20, 30, 50], labels=["A", "B", "C"], autopct='%1.1f%%')  # Biểu đồ tròn
7. plt.xlabel() và plt.ylabel()
Dùng để thêm nhãn cho trục x và trục y.
Cú pháp: plt.xlabel('Tên trục x'), plt.ylabel('Tên trục y')
Ví dụ:

plt.xlabel('Trục X')
plt.ylabel('Trục Y')
8. plt.title()
Dùng để thêm tiêu đề cho đồ thị.
Cú pháp: plt.title('Tiêu đề đồ thị')
Ví dụ:

plt.title('Biểu đồ đường')
9. plt.legend()
Dùng để thêm chú giải (legend) cho đồ thị.
Cú pháp: plt.legend([labels])
labels: Danh sách các nhãn để hiển thị trong legend.
Ví dụ:

plt.plot([1, 2, 3], [4, 5, 6], label='Đường 1')
plt.legend()
10. plt.grid()
Dùng để hiển thị lưới (grid) trong biểu đồ.
Cú pháp: plt.grid(True/False)
Ví dụ:

plt.grid(True)  # Hiển thị lưới
11. plt.show()
Dùng để hiển thị đồ thị.
Cú pháp: plt.show()
Ví dụ:

plt.plot([1, 2, 3], [4, 5, 6])
plt.show()  # Hiển thị đồ thị
12. plt.subplots()
Dùng để tạo một figure và các axes (trục con) cho nhiều biểu đồ.
Cú pháp: fig, ax = plt.subplots(nrows=1, ncols=2) (tạo một figure với 2 trục con).
Ví dụ:

fig, ax = plt.subplots(1, 2)
ax[0].plot([1, 2, 3], [4, 5, 6])
ax[1].scatter([1, 2, 3], [4, 5, 6])
plt.show()
13. plt.xticks() và plt.yticks()
Dùng để điều chỉnh các giá trị nhãn trên trục x và y.
Cú pháp: plt.xticks(ticks, labels), plt.yticks(ticks, labels)
Ví dụ:

plt.xticks([0, 1, 2], ['A', 'B', 'C'])  # Đổi nhãn trên trục x
14. plt.savefig()
Dùng để lưu biểu đồ vào file (hình ảnh).
Cú pháp: plt.savefig('file_name.png')
Ví dụ:

plt.plot([1, 2, 3], [4, 5, 6])
plt.savefig('chart.png')  # Lưu biểu đồ vào file
15. plt.xlim() và plt.ylim()
Dùng để điều chỉnh phạm vi giá trị trên trục x và y.
Cú pháp: plt.xlim([xmin, xmax]), plt.ylim([ymin, ymax])
Ví dụ:

plt.xlim(0, 10)  # Điều chỉnh phạm vi trục x
plt.ylim(0, 20)  # Điều chỉnh phạm vi trục y





BT MATPLOTLIB 
import numpy as np
import matplotlib.pyplot as plt

# Tạo giá trị cho x
x = np.arange(-3 * np.pi, 0, 0.1)
x2 = np.arange(0, 3 * np.pi, 0.1)
theta = np.arange(0, 2*np.pi ,0.01)
   

# Hàm y = 1.5 * sin(x)
y = 1.5 * np.sin(x)
r = 2 + np.cos(10 * theta) + 2 * np.sin(5 * theta)
y2 = 1.5 * np.sin(x2)


# Tạo figure cho đồ thị
plt.figure(figsize=(8, 6))

# Vẽ đồ thị 1  với đường màu đỏ 
plt.plot(x, y, 'r:', label=r"$y = 1.5\sin(x)$ with $x \in [-3\pi; 0]$", linewidth=3)

# Đồ thị thứ hai: r = 2 + cos(10θ) + 2sin(5θ)
plt.plot(theta, r, 'g-', label=r"$r = 2 + \cos(10\theta) + 2\sin(5\theta)$", linewidth=3)

# Vẽ đồ thị 2  với đường màu đỏ 
plt.plot(x2, y2, 'b:', label=r"$y = 1.5\sin(x)$ with $x \in [0; 3\pi]$", linewidth=3)

# Cài đặt giới hạn cho trục x và y
plt.xlim(-10, 10)  # Giới hạn trục x từ -10 đến 10
plt.ylim(-6, 6)  # Giới hạn trục y từ -6 đến 6

# Thêm grid
plt.grid(True)

# # Hiển thị legend
plt.legend()

# Hiển thị đồ thị
plt.show()






PANDAS 
. pd.read_csv()
Dùng để đọc dữ liệu từ tệp CSV và lưu vào DataFrame.
Cú pháp: pd.read_csv('file_path.csv')
Ví dụ:

import pandas as pd
df = pd.read_csv('data.csv')
2. df.head()
Dùng để hiển thị một số dòng đầu tiên của DataFrame.
Cú pháp: df.head(n), mặc định n=5 (hiển thị 5 dòng đầu).
Ví dụ:

df.head(10)  # Hiển thị 10 dòng đầu tiên
3. df.tail()
Dùng để hiển thị một số dòng cuối cùng của DataFrame.
Cú pháp: df.tail(n), mặc định n=5.
Ví dụ:

df.tail(3)  # Hiển thị 3 dòng cuối cùng
4. df.info()
Dùng để xem thông tin tổng quan về DataFrame (số dòng, kiểu dữ liệu, dữ liệu null, v.v...).
Cú pháp: df.info()
Ví dụ:

df.info()  # Hiển thị thông tin DataFrame
5. df.describe()
Dùng để tính toán các thống kê cơ bản (mean, std, min, max, quartiles) cho các cột số trong DataFrame.
Cú pháp: df.describe()
Ví dụ:

df.describe()  # Thống kê mô tả cho các cột số
6. df.shape
Trả về kích thước của DataFrame (số dòng và số cột).
Cú pháp: df.shape
Ví dụ:

df.shape  # (số dòng, số cột)
7. df.isnull() và df.notnull()
df.isnull() trả về DataFrame với giá trị True cho các ô có giá trị null.
df.notnull() trả về DataFrame với giá trị True cho các ô không phải null.
Ví dụ:

df.isnull()  # Hiển thị các ô bị thiếu (null)
df.notnull()  # Hiển thị các ô không bị thiếu
8. df.fillna()
Dùng để điền giá trị thay thế cho các ô bị thiếu (null).
Cú pháp: df.fillna(value)
Ví dụ:

df.fillna(0)  # Điền 0 vào các ô bị thiếu
9. df.dropna()
Dùng để xóa các dòng hoặc cột có giá trị null.
Cú pháp: df.dropna(axis=0), axis=0 để xóa dòng, axis=1 để xóa cột.
Ví dụ:

df.dropna()  # Xóa các dòng có giá trị null
10. df.columns
Trả về danh sách tên các cột trong DataFrame.
Cú pháp: df.columns
Ví dụ:

df.columns  # Hiển thị tên các cột
11. df['column_name']
Truy cập và chọn một cột cụ thể trong DataFrame.
Cú pháp: df['column_name']
Ví dụ:

df['age']  # Chọn cột 'age'
12. df[['col1', 'col2']]
Truy cập và chọn nhiều cột trong DataFrame.
Cú pháp: df[['col1', 'col2']]
Ví dụ:

df[['name', 'age']]  # Chọn cột 'name' và 'age'
13. df.loc[] và df.iloc[]
df.loc[] dùng để truy xuất dữ liệu theo nhãn (index).
df.iloc[] dùng để truy xuất dữ liệu theo vị trí chỉ số (integer location).
Cú pháp: df.loc[row_index, column_name], df.iloc[row_index, column_index]
Ví dụ:

df.loc[0, 'name']  # Truy cập giá trị tại dòng 0 và cột 'name'
df.iloc[0, 1]  # Truy cập giá trị tại dòng 0 và cột thứ 1
14. df.sort_values()
Dùng để sắp xếp các giá trị trong DataFrame theo một cột nhất định.
Cú pháp: df.sort_values(by='column_name', ascending=True)
Ví dụ:

df.sort_values(by='age', ascending=False)  # Sắp xếp theo cột 'age' giảm dần
15. df.groupby()
Dùng để nhóm các dữ liệu theo một hoặc nhiều cột và áp dụng các phép toán tổng hợp.
Cú pháp: df.groupby('column_name')
Ví dụ:

df.groupby('gender').mean()  # Nhóm theo giới tính và tính giá trị trung bình
16. df.merge()
Dùng để kết hợp hai DataFrame theo một hoặc nhiều cột chung.
Cú pháp: df1.merge(df2, on='common_column')
Ví dụ:

df1.merge(df2, on='id')  # Kết hợp hai DataFrame theo cột 'id'
17. df.pivot_table()
Dùng để tạo bảng xoay (pivot table) cho phép tổng hợp dữ liệu.
Cú pháp: df.pivot_table(values='value_column', index='row_column', columns='column_column')
Ví dụ:

df.pivot_table(values='score', index='gender', columns='subject')
18. df.apply()
Dùng để áp dụng một hàm cho từng cột hoặc dòng của DataFrame.
Cú pháp: df.apply(function, axis=0), axis=0 cho cột, axis=1 cho dòng.
Ví dụ:

df['age'] = df['age'].apply(lambda x: x + 1)  # Tăng tuổi lên 1
19. df.to_csv()
Dùng để ghi DataFrame vào tệp CSV.
Cú pháp: df.to_csv('file_name.csv', index=False)
Ví dụ:

df.to_csv('output.csv', index=False)  # Ghi DataFrame vào tệp CSV
20. df.value_counts()
Dùng để đếm số lần xuất hiện của các giá trị trong một cột.
Cú pháp: df['column_name'].value_counts()
Ví dụ:

df['gender'].value_counts()  # Đếm số lần xuất hiện của mỗi giá trị trong cột 'gender'
21. df.corr()
Dùng để tính toán ma trận tương quan giữa các cột số.
Cú pháp: df.corr()
Ví dụ:

df.corr()  # Tính toán ma trận tương quan"""





"""
BT PANDAS 
1/ 
import pandas as pd

# a. Đọc dữ liệu từ tập tin đã cho, sử dụng ký tự phân tách là dấu '|' 
df = pd.read_csv('D:/NamII_HK1/PY/SCHOOL/Code/BaiTap/BaiTapBuoi11(pandas)/u.user', sep='|')

# b. Độ tuổi trung bình của mỗi nghề nghiệp
avg_age_by_occupation = df.groupby('occupation')['age'].mean()
print("Độ tuổi trung bình của mỗi nghề nghiệp:\n", avg_age_by_occupation)

# c. Tỷ lệ số lượng người trên mỗi nghề và sắp xếp từ cao đến thấp
occupation_counts = df['occupation'].value_counts(normalize=True) * 100
sorted_occupation_counts = occupation_counts.sort_values(ascending=False)
print("\nTỷ lệ phần trăm trên mỗi nghề nghiệp (sắp xếp từ cao đến thấp):\n", sorted_occupation_counts)

# d. Độ tuổi nhỏ nhất và lớn nhất cho mỗi nghề nghiệp
age_min_max_by_occupation = df.groupby('occupation')['age'].agg(['min', 'max'])
print("\nĐộ tuổi nhỏ nhất và lớn nhất cho mỗi nghề nghiệp:\n", age_min_max_by_occupation)

# e. Tuổi trung bình cho mỗi tổ hợp của nghề nghiệp và giới tính
avg_age_by_occupation_gender = df.groupby(['occupation', 'gender'])['age'].mean()
print("\nTuổi trung bình cho mỗi tổ hợp của nghề nghiệp và giới tính:\n", avg_age_by_occupation_gender)

# f. Tỷ lệ phần trăm nam và nữ trên mỗi nghề nghiệp
gender_counts_by_occupation = df.groupby(['occupation', 'gender']).size().unstack(fill_value=0)
print(gender_counts_by_occupation)
# gender_percentage_by_occupation = gender_counts_by_occupation.div(gender_counts_by_occupation.sum(axis=1), axis=0) * 100
# print("\nTỷ lệ phần trăm nam và nữ trên mỗi nghề nghiệp:\n", gender_percentage_by_occupation)


2/
import pandas as pd
import matplotlib.pyplot as plt

# a. Đọc dữ liệu từ tập tin đã cho
df = pd.read_csv('D:/NamII_HK1/PY/SCHOOL/Code/BaiTap/BaiTapBuoi11(pandas)/chipotle.tsv', sep='\t')

df['item_price'] = df['item_price'].replace('[\$,]', '', regex=True).astype(float)  # Chuyển item_price thành dạng float
print("Dữ liệu đã được tải thành công!")

# b. Liệt kê những sản phẩm có giá hơn 10$ (lược bỏ những dòng trùng tên sản phẩm)
products_above_10 = df[df['item_price'] > 10]['item_name'].drop_duplicates()
print("Các sản phẩm có giá trên 10$:\n", products_above_10)

# c. Sắp xếp các sản phẩm theo tên
sorted_products = df['item_name'].drop_duplicates().sort_values()
print("Danh sách các sản phẩm đã được sắp xếp theo tên:\n", sorted_products)

# d. Tìm sản phẩm có giá cao nhất trong danh sách
most_expensive_item = df.loc[df['item_price'].idxmax()]
print("Sản phẩm có giá cao nhất là:\n", most_expensive_item)

# e. Cho biết sản phẩm “Veggie Salad Bowl” xuất hiện trong bao nhiêu đơn hàng với tổng số lượng được đặt
veggie_salad_orders = df[df['item_name'] == 'Veggie Salad Bowl']
veggie_salad_count = veggie_salad_orders['order_id'].nunique()
veggie_salad_quantity = veggie_salad_orders['quantity'].sum()
print(f"Sản phẩm 'Veggie Salad Bowl' xuất hiện trong {veggie_salad_count} đơn hàng với tổng số lượng được đặt là {veggie_salad_quantity}")

# f. Vẽ biểu đồ histogram cho 5 sản phẩm được mua nhiều nhất với tần suất mua
top_5_items = df.groupby('item_name')['quantity'].sum().nlargest(5)
plt.figure(figsize=(10, 6))
top_5_items.plot(kind='bar', color='skyblue')
plt.title('Top 5 sản phẩm được mua nhiều nhất')
plt.xlabel('Tên sản phẩm')
plt.ylabel('Tần suất mua')
plt.show()

# g. Vẽ biểu đồ scatter với số lượng mặt hàng được đặt hàng trên mỗi đơn hàng
order_items = df.groupby('order_id')['quantity'].sum()
plt.figure(figsize=(10, 6))
plt.scatter(order_items.index, order_items.values, color='blue', alpha=0.5)
plt.title('Số lượng mặt hàng được đặt trên mỗi đơn hàng')
plt.xlabel('Order ID')
plt.ylabel('Số lượng mặt hàng')
plt.show()
"""