# a, b, c = map(int,input().split())
# if a > b :
#     if b > c :
#         print(b)
#     else :
#         if a > c :
#             print(c)
#         else :
#             print(a)
# else :
#     if a > c :
#         print(a)
#     else :
#         if b > c :
#             print(c)
#         else :
#             print(b)

# # cach 2

# # def swap(a, b):
# #     return b, a

# # if __name__ == "__main__":
# #     # Input: Enter numbers separated by spaces
# #     n = input("Nhập các số cách nhau bởi dấu cách: ")
# #     a = [int(x) for x in n.split()]

# #     # Bubble Sort to sort the list in ascending order
# #     for i in range(len(a)):
# #         # len(a) - i - 1 : bo di i -1 gia tri cho vong long ke tiep
# #         for j in range(0, len(a) - i - 1):
# #             if a[j] > a[j + 1]:
# #                 a[j], a[j + 1] = swap(a[j], a[j + 1])

# #     # Print the sorted list
# #     for i in a:
# #         print(i, end=" ")

# #     # Input: Enter numbers separated by spaces
# #     n = input("Nhập các số cách nhau bởi dấu cách: ")
# #     a = [int(x) for x in n.split()]

# #     # Bubble Sort to sort the list in ascending order
# #     for i in range(len(a)):
# #         for j in range(0, len(a) - i - 1):
# #             if a[j] > a[j + 1]:
# #                 a[j], a[j + 1] = swap(a[j], a[j + 1])

# #         print(a[1])


# # * selection sort
# # def selection_sort(a):
# #     for i in range(len(a)):
# #         min_idx = i
# #         for  j in range(i+1,len(a)):
# #             if a[j] > a[min_idx] :
# #                 min_idx = j
# #         a[min_idx], a[i] = a[i], a[min_idx]

# # if __name__ == "__main__" :
# #     n = input("Nhap cac so nguyen(3 so) cach nhau dau cach: ")
# #     a = [int(x) for x in n.split()]

# #     selection_sort(a)
# #     print(f"So lon thu hai: {a[1]}")
