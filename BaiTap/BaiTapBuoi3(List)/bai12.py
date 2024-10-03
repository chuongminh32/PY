# def main():
#     n = int(input("Nhap so luong phan tu: "))
#     numbers = []

#     for i in range(n):
#         numbers.append(float(input(f"Nhap phan tu thu {i+1}: ")))

#     for i in range(n):
#         for j in range(i+1, n):
#             if numbers[i] % 2 == 0 and numbers[j] % 2 == 0 and numbers[i] > numbers[j]:
#                 numbers[i], numbers[j] = numbers[j], numbers[i]
#             if numbers[i] % 2 != 0 and numbers[j] % 2 != 0 and numbers[i] < numbers[j]:
#                 numbers[i], numbers[j] = numbers[j], numbers[i]

#     for num in numbers:
#         print(num, end=" ")


# if __name__ == "__main__":
#     main()

# cach 2
# def main():
#     n = int(input())
#     a = []
#     e = []
#     o = []
#     for i in range(n):
#         val = float(input())
#         a.append(val)
#         if val % 2 == 0:
#             e.append(val)
#         else:
#             o.append(val)

#     e.sort()
#     o.sort(reverse=True)

#     for i in range(n):
#         if a[i] % 2 == 0:
#             a[i] = e[0]
#             e.remove(e[0])
#         else:
#             a[i] = o[0]
#             o.remove(o[0])

#     for i in range(n):
#         print(a[i], end=" ")


# if __name__ == "__main__":
#     main()
