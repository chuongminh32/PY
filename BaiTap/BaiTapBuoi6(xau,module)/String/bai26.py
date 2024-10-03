# import random

# def generate_password():
#     # Định nghĩa các tập ký tự
#     letters_lower = [chr(i) for i in range(97, 123)]  # Chữ cái thường (a-z)
#     letters_upper = [chr(i) for i in range(65, 91)]   # Chữ cái hoa (A-Z)
#     digits = [chr(i) for i in range(48, 58)]          # Chữ số (0-9)
#     special_chars = ['#', '%', '@', '!', '$', '^', '&', '*', '(', ')']  # Ký tự đặc biệt
    
#     # Tạo ít nhất 1 ký tự từ mỗi loại
#     password = [
#         random.choice(letters_lower),
#         random.choice(letters_upper),
#         random.choice(digits),
#         random.choice(special_chars)
#     ]

#     # Tạo thêm các ký tự ngẫu nhiên để mật khẩu có ít nhất 8 ký tự
#     while len(password) < 8:
#         random_char = random.choice(letters_lower + letters_upper + digits + special_chars)
#         password.append(random_char)

#     # Trộn thứ tự các ký tự trong mật khẩu
#     random.shuffle(password)

#     # Chuyển danh sách các ký tự thành chuỗi
#     return ''.join(password)

# # Test chương trình
# print("Mật khẩu ngẫu nhiên:", generate_password())
