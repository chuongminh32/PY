# def main():
#     # Nhập số lượng phần tử của danh sách
#     n = int(input("Nhập số lượng phần tử: "))

#     # Tạo danh sách số nguyên
#     numbers = []
#     for i in range(n):
#         numbers.append(int(input(f"Nhập phần tử thứ {i+1}: ")))

#     # Lọc các số âm
#     negativeArray = [num for num in numbers if num < 0]

#     # Sắp xếp các số âm theo thứ tự giảm dần
#     negativeArray.sort(reverse=True)

#     # Thay thế các số âm trong danh sách gốc bằng các số đã sắp xếp
#     index = 0
#     for i in range(len(numbers)):
#         if numbers[i] < 0:
#             numbers[i] = negativeArray[index]
#             index += 1

#     # Hiển thị kết quả
#     print(f"Danh sách sau khi sắp xếp các số âm giảm dần: {numbers}")


# if __name__ == "__main__":
#     main()


# def main():
#     # Nhập số lượng phần tử của danh sách
#     n = int(input("Nhập số lượng phần tử của danh sách (n ≥ 0): "))

#     # Kiểm tra điều kiện n ≥ 0
#     if n < 0:
#         print("Số lượng phần tử không hợp lệ. Vui lòng nhập số nguyên dương.")
#         return

#     # Nhập các số thực vào danh sách
#     numbers = []
#     for _ in range(n):
#         while True:
#             try:
#                 num = float(input("Nhập một số thực: "))
#                 numbers.append(num)
#                 break
#             except ValueError:
#                 print("Giá trị không hợp lệ. Vui lòng nhập một số thực.")

#     # Lọc các số âm và sắp xếp chúng theo thứ tự giảm dần
#     negative_numbers = [num for num in numbers if num < 0]
#     negative_numbers.sort(reverse=True)

#     # Thay thế các số âm trong danh sách gốc bằng các số đã sắp xếp
#     result = []
#     negative_index = 0
#     for num in numbers:
#         if num < 0:
#             result.append(negative_numbers[negative_index])
#             negative_index += 1
#         else:
#             result.append(num)

#     # Hiển thị kết quả
#     print("Danh sách sau khi sắp xếp các số âm giảm dần:")
#     print(result)

# if __name__ == "__main__":
#     main()
