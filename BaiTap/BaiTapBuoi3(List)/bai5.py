def main():
    n = int(input("Nhap so luong phan tu: "))
    numbers = []

    for i in range(n):
        numbers.append(float(input(f"Nhap phan tu thu {i+1}: ")))

    even = []
    odd = []

    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    print("Even List:")
    for e in even:
        print(e, end=" ")

    print()
    print("Odd List:")
    for o in odd:
        print(o, end=" ")


if __name__ == "__main__":
    main()
