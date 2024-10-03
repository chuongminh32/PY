
# s = input("Nhap xau s: ")

# # Không cần dùng split để chia chuỗi thành danh sách ký tự, chỉ cần sử dụng list(s)
# temp_s = list(s)

# # Sắp xếp danh sách các ký tự
# sorted_temp_s = sorted(temp_s)

# # In danh sách ký tự đã sắp xếp
# print(sorted_temp_s)

# # Ghép các ký tự đã sắp xếp lại thành chuỗi
# print(''.join(sorted_temp_s))

# sorted(str) -> lst[] -> join -> str 


print(''.join(sorted(input("Nhap chuoi s: "))))

