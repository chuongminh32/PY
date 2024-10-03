# def main():
#     n = int(input("Nhap so luong phan tu: "))
#     numbers = []
#     for i in range(n):
#         numbers.append(int(input(f"Nhap phan tu thu {i+1}: ")))

#     numbers.sort()


#     print(numbers)


# if __name__ == "__main__":
#     main()

# selection sort
# for i in range(n):
#     index = i
#     for j in range(i+1, n):
#         if numbers[j] < numbers[index]:
#             index = j
#     # temp = numbers[index]
#     # numbers[index] = numbers[i]
#     # numbers[i] = temp
#     numbers[index], numbers[i] = numbers[i], numbers[index]

# buble sort
# for i in range(n):
#     for j in range(0, n-i-1):
#         if numbers[j] > numbers[j+1]:
#             numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

# insert sort
# for i in range(1, n):
#     key = numbers[i]
#     j = i - 1
#     while j >= 0 and numbers[j] > key:
#         numbers[j+1] = numbers[j]
#         j -= 1
#     numbers[j+1] = key

# # merge sort
# def merge_sort(numbers):
#     if len(numbers) > 1:
#         # Tìm điểm giữa để chia danh sách thành hai nửa
#         mid = len(numbers) // 2
#         left_half = numbers[:mid]
#         right_half = numbers[mid:]

#         # Đệ quy sắp xếp hai nửa
#         merge_sort(left_half)
#         merge_sort(right_half)

#         # Các chỉ số ban đầu của hai nửa
#         i = j = k = 0

#         # Gộp hai nửa đã sắp xếp lại
#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 numbers[k] = left_half[i]
#                 i += 1
#             else:
#                 numbers[k] = right_half[j]
#                 j += 1
#             k += 1

#         # Sao chép phần còn lại của left_half nếu còn
#         while i < len(left_half):
#             numbers[k] = left_half[i]
#             i += 1
#             k += 1

#         # Sao chép phần còn lại của right_half nếu còn
#         while j < len(right_half):
#             numbers[k] = right_half[j]
#             j += 1
#             k += 1

#     return numbers

# # Ví dụ sử dụng
# numbers = [38, 27, 43, 3, 9, 82, 10]
# sorted_numbers = merge_sort(numbers)
# print(sorted_numbers)

# quick sort
# def quick_sort(numbers):
#     if len(numbers) <= 1:
#         return numbers
#     else:
#         pivot = numbers[len(numbers) // 2]  # Chọn pivot (phần tử giữa)
#         left = [x for x in numbers if x < pivot]
#         middle = [x for x in numbers if x == pivot]
#         right = [x for x in numbers if x > pivot]
#         # Đệ quy sắp xếp các phần và gộp kết quả
#         return quick_sort(left) + middle + quick_sort(right)

# # Ví dụ sử dụng
# numbers = [38, 27, 43, 3, 9, 82, 10]
# sorted_numbers = quick_sort(numbers)
# print(sorted_numbers)
