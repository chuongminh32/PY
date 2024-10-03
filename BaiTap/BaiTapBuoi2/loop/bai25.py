# def main():
#     while True:
#         bits = input("Nhap chuoi nhi phan: ")
#         if bits == "":
#             print("Kết thúc chương trình.")
#             break
#         if len(bits) != 8 or not all(bit in '01' for bit in bits):
#             print(
#                 "Lỗi: Chuỗi nhị phân phải có đúng 8 bit và chỉ chứa các ký tự 0 hoặc 1.")
#             continue
#         else:
#             cnt = 0
#             for i in range(len(bits)):
#                 if bits[i] == "1":
#                     cnt += 1

#             choosen = input("Ban muon nhap parity chan hay le (chan/le): ")

#             if choosen not in ['chan', 'le']:
#                 print("Vui long nhap dung dinh dang chan hoac le")
#                 continue
#             if choosen == "chan":
#                 if cnt % 2 == 0:
#                     print("bit parity = 0")
#                 else:
#                     print("bit parity = 1")
#             elif choosen == "le":
#                 if cnt % 2 == 0:
#                     print("bit parity = 1")
#                 else:
#                     print("bit parity = 0")
#             else:
#                 print("Lua chon khong hop le!")


# if __name__ == "__main__":
#     main()


# # def calculate_parity(bits, parity_type):
# #     # Đếm số bit 1 trong chuỗi bits
# #     count_ones = bits.count('1')

# #     # Tính toán parity chẵn hoặc lẻ dựa vào lựa chọn của người dùng
# #     if parity_type == 'even':
# #         # Parity chẵn: nếu tổng số bit 1 là chẵn, parity = 0; nếu lẻ, parity = 1
# #         return 0 if count_ones % 2 == 0 else 1
# #     elif parity_type == 'odd':
# #         # Parity lẻ: nếu tổng số bit 1 là lẻ, parity = 0; nếu chẵn, parity = 1
# #         return 1 if count_ones % 2 == 0 else 0


# # def main():
# #     while True:
# #         # Yêu cầu người dùng nhập chuỗi 8-bit nhị phân
# #         bits = input(
# #             "Nhập chuỗi nhị phân 8-bit (hoặc khoảng trắng để thoát): ").strip()

# #         # Kiểm tra nếu người dùng nhập khoảng trắng thì thoát chương trình
# #         if bits == "":
# #             print("Kết thúc chương trình.")
# #             break

# #         # Kiểm tra nếu chuỗi không có đúng 8-bit
# #         if len(bits) != 8 or not all(bit in '01' for bit in bits):
# #             print(
# #                 "Lỗi: Chuỗi nhị phân phải có đúng 8 bit và chỉ chứa các ký tự 0 hoặc 1.")
# #             continue

# #         # Hỏi người dùng muốn tính parity chẵn hay lẻ
# #         parity_type = input(
# #             "Bạn muốn tính parity chẵn hay lẻ? (even/odd): ").strip().lower()

# #         if parity_type not in ['even', 'odd']:
# #             print("Lỗi: Vui lòng nhập 'even' hoặc 'odd'.")
# #             continue

# #         # Tính toán parity
# #         parity_bit = calculate_parity(bits, parity_type)

# #         # Hiển thị kết quả
# #         print(f"Bit parity của chuỗi {bits} với parity {
# #               parity_type} là: {parity_bit}\n")


# # if __name__ == "__main__":
# #     main()
