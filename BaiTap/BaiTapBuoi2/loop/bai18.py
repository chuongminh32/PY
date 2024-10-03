# def main():
#     choose = input("Bạn có muốn tự nhập mảng chuỗi số (Y/N) : ")
#     if choose == "Y":
#         numStr = input("Nhap chuoi so bat ki: ")
#         numbers = [int(x) for x in numStr.split()]
#     else:
#         print("Chuoi mac dinh la: [12, 45, 33, 55, 10, 22, 67, 50, 100] ")
#         numbers = [12, 45, 33, 55, 10, 22, 67, 50, 100]

#     max_divisible_by5 = None
#     for number in numbers:
#         if number % 5 == 0:
#             if max_divisible_by5 is None or number > max_divisible_by5:
#                 max_divisible_by5 = number

#     if max_divisible_by5 is not None:
#         print(f"So lon nhat chia het cho 5: {max_divisible_by5}")
#     else:
#         print("Khong tim thay so chia het cho 5")


# if __name__ == "__main__":
#     main()
