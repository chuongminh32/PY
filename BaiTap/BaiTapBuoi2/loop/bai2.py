# def checkSquareNumber(n) :
#     i = 0
#     while i * i <= n :
#         if i * i == n :
#             return True
#         i+=1
#     else :
#         if (i*i - n ) < (n - (i-1)**2) :
#                 return i * i 
#         else :
#                 return (i-1)**2

# if __name__ == "__main__" :
#     n = int(input())
#     result = checkSquareNumber(n)
#     if (result == True) :
#         print(f"So {n} la so chinh phuong")
#     else :
#         print(f"So {result} la so chinh phuong gan nhat")