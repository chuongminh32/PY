# # import bai9 

# def sumDigit(n):
#     s = 0
#     while n != 0:
#         s += (n % 10)
#         n //= 10
#     return s

# def demoImport(yourName):
#     return f"Hello {yourName}"

# def main():
#     while 1:
#         try:
#             n = int(input("Nhap mot so nguyen duong: "))
#             if n > 0:
#                 result = sumDigit(n)
#                 print(f"Tong cac chu so cua so ban vua nhap: {result}")
#                 break
#             else:
#                 print("Nhap sai, Vui long nhap lai!")
#         except ValueError:
#             print("Vui long nhap dung so nguyen !")

# if __name__ == "__main__":
#     main()
# # else :
# #     # khi file bai10 duoc import (bai 11) => __name__ = ten module (bai10)
# #     print(f"__name__ == {__name__}")
# #     print("bai10 has imported!")
