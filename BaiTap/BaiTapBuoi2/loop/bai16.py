# import math


# def countDivisor(n):
#     cnt = 0
#     for i in range(1, math.isqrt(n)+1):
#         if n % i == 0:
#             if i != n // i:
#                 cnt += 2
#             else:
#                 cnt += 1

#     return cnt


# def main():
#     N = int(input("Nhap so nguyen N: "))
#     result = countDivisor(N)
#     print(f"Co {result} uoc so {N}")


# if __name__ == "__main__":
#     main()
