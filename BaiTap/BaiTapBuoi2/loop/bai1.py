# def countDigit(n):
#     cnt_even = 0
#     cnt_odd = 0
#     while n != 0 :
#         if (n % 10) % 2 == 0 :
#             cnt_even += 1 
#         else :
#             cnt_odd += 1
#         n//=10
#     return cnt_even, cnt_odd

# if __name__ == "__main__" :
#     N = int(input("Nhap so N trong khoang [10000, 99999]: "))
#     if N >= 10000 and N <= 99999:
#         count_e,count_o = countDigit(N)
#         print(f"so {N} co {count_e} so chan va {count_o} so le")
#     else :
#         print("Nhap lai")
        