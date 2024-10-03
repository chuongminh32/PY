# def main():
#     choose = input("Bạn có muốn tự nhập mảng chuỗi số (Y/N) : ")
#     if choose == "Y":
#         numStr = input("Nhap chuoi so bat ki: ")
#         numbers = [int(x) for x in numStr.split()]
#     else:
#         print(
#             "Chuoi mac dinh la: [12, 33, 43, 55, 65, 72, 87, 90, 106, 178, 290, 300] ")
#         numbers = [12, 33.4, 43, 55, 65, 72.5, 87, 90, 106, 178.9, 290, 300]

#     B = float(input("Nhap so B bat ki: "))

#     for i in range(len(numbers)):
#         if numbers[i] > B:
#             numbers.insert(i, B)
#             break
#     # Neu khong co vi tri thoa man -> chen B vao cuoi mang
#     else:
#         numbers.append(B)

#     print(f"Mang sau khi them phan tu B : {numbers}")


# if __name__ == "__main__":
#     main()
