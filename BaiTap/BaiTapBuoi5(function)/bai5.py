# def check(Pass):
#     u, l, n = 0, 0, 0
#     for p in Pass:
#         if p.isupper():  
#             u += 1
#         elif p.islower():  
#             l += 1
#         elif p.isdigit():  
#             n += 1
    
#     # Mật khẩu phải có ít nhất 8 ký tự, và có ít nhất 1 chữ in hoa, 1 chữ thường, và 1 số
#     return len(Pass) >= 8 and u >= 1 and l >= 1 and n >= 1


# def main():
#     Pass = input("Nhập mật khẩu: ")
#     if check(Pass):
#         print("Mật khẩu mạnh")
#     else:
#         print("Mật khẩu yếu")


# main()
