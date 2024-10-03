# # def sieve(n):
# #     # danh dau true cho tat ca phan tu tu 1 -> n
# #     primes = [True] * (n+1)

# #     # so nguyen to dau tien
# #     p = 2

# #     # duyet tat ca uoc cua n
# #     while p * p < n:
# #         # loai bo uoc so
# #         if primes[p]:
# #             for i in range(p * p, n + 1, p):
# #                 primes[i] = False
# #         p += 1

# #     # them cac so nguyen to hop le vao mang moi
# #     arrayPrimes = [p for p in range(2, n+1) if primes[p] == True]
# #     return arrayPrimes


# # if __name__ == "__main__":
# #     N = int(input("Nhap N: "))
# #     arrayPrimes = sieve(N)
# #     print(f"Cac so nguyen to nho hon {N} : {arrayPrimes} ")

# import math


# def checkPrime(n):
#     for i in range(2, math.isqrt(n)+1):
#         if n % i == 0:
#             return False

#     return n > 1


# if __name__ == "__main__":
#     N = int(input("Nhap N: "))
#     cnt = 0
#     i = 2
#     while 1:
#         if cnt == N:
#             break

#         if checkPrime(i):
#             print(i, end=" ")
#             cnt += 1

#         i += 1
