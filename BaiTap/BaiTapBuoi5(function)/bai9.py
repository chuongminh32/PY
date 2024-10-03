# def so_sao_tiet_kiem(dien_nang):
#     """Hàm trả về số sao tiết kiệm năng lượng dựa trên điện năng tiêu thụ."""
#     if dien_nang < 2:
#         return 5
#     elif 2 <= dien_nang < 4:
#         return 4
#     elif 4 <= dien_nang < 6:
#         return 3
#     elif 6 <= dien_nang < 10:
#         return 2
#     else:
#         return 1

# def kiem_tra_tiet_kiem(dien_nang):
#     """Hàm kiểm tra và in ra thông báo thiết bị có tiết kiệm điện hay không."""
#     sao = so_sao_tiet_kiem(dien_nang)  # Gọi hàm để tính số sao
#     if sao < 3:
#         print("Thiết bị không tiết kiệm điện.")
#     else:
#         print("Thiết bị tiết kiệm điện.")

# def main():
#     dien_nang = float(input("Nhập điện năng tiêu thụ mỗi ngày (kWh): "))
#     kiem_tra_tiet_kiem(dien_nang)

# # Gọi chương trình chính
# if __name__ == "__main__":
#     main()
