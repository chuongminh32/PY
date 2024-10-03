# def is_strong_password(password):
#     # Điều kiện 1: Mật khẩu phải có độ dài ít nhất 8 ký tự
#     if len(password) < 8:
#         return False

#     # Khởi tạo các biến cờ để kiểm tra các loại ký tự
#     has_letter = False
#     has_digit = False
#     has_special_char = False

#     # Duyệt qua từng ký tự trong mật khẩu
#     for char in password:
#         if char.isalpha():  # Kiểm tra nếu là chữ cái
#             has_letter = True
#         elif char.isdigit():  # Kiểm tra nếu là chữ số
#             has_digit = True
#         else:  # Nếu không phải chữ cái hoặc số, thì là ký tự đặc biệt
#             has_special_char = True

#     # Kiểm tra nếu tất cả các loại ký tự đều có
#     if has_letter and has_digit and has_special_char:
#         return True
#     else:
#         return False

# # Test chương trình
# password = input("Nhập mật khẩu: ")
# if is_strong_password(password):
#     print("Mật khẩu mạnh")
# else:
#     print("Mật khẩu không đủ mạnh")
