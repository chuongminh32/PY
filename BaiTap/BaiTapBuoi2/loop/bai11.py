# # import bai10

# # def main():
# #     message = bai10.demoImport("Minh Chuong")
# #     print(message)

# # main() ghi de main() tren

# # cach 1
# s = input("Nhap chuoi so: ")
# sum = 0
# for i in range(len(s)):
#     if s[i] == "0":
#         break
#     # Neu s[i] la mot ki tu so nguyen
#     elif s[i] != " " and s[i] != "-":
#         # va so nguyen do khong am
#         if s[i-1] != "-":
#             sum += int(s[i])

# print(f"Tong cac so nguyen duong: {sum}")

# # cach 2
# # def main():
# #     try:
# #         numbers = input("Nhap chuoi so nguyen: ")
# #         # tach chuoi so theo dau cach > ep kieu > dua vao mang
# #         arrayNum = [int(x) for x in numbers.split()]
# #         sum = 0
# #         for num in arrayNum:
# #             if num == 0:
# #                 break
# #             elif num > 0:
# #                 sum += num
# #             else:
# #                 continue

# #         print(f"Tong cac so nguyen duong: {sum}")
# #     except ValueError:
# #         print("Vui long nhap dung so nguyen !")


# # if __name__ == "__main__":
# #     main()
# # else :
# #     print("Chua import file")
