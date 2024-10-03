# def main():
#     n = int(input("Nhap so luong phan tu: "))
#     numbers = []

#     for i in range(n):
#         numbers.append(float(input(f"Nhap phan tu thu {i+1}: ")))

#     for i in range(n):
#         for j in range(i+1, n):
#             if numbers[i] < 0 and numbers[j] < 0 and numbers[i] > numbers[j]:
#                 numbers[i], numbers[j] = numbers[j], numbers[i]
#             if numbers[i] > 0 and numbers[j] > 0 and numbers[i] < numbers[j]:
#                 numbers[i], numbers[j] = numbers[j], numbers[i]

#     for num in numbers:
#         print(num, end=" ")


# if __name__ == "__main__":
#     main()
