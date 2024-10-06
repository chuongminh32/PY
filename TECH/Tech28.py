
# =======================PART I: DATA TYPES, LOOPS, OPERATOR FUNCTIONS ===================================
# s = '28 tech'
# if('28' in s) : print('28 la chuoi con 28 tech')

# p/s circle
# R = float(input("Nhap ban kinh R: "))
# pi = 3.14
# chuvi = 2 * pi * R
# dientich = pi * R * R
# print('chu vi la: ','{:.2f}'.format(chuvi))
# print('dien tich la: ','{:.2f}'.format(dientich))

# # tach cac so theo dau cach
# x,y,z = map(int,a) 
# print('danh sach cac so vua nhap: ',a)
# # dung map (data type,list)
# #  -> tach cac so trong xau va ep kieu chung
# print ( 'Tong ba so la: ',x + y + z) 
# # -> tong 3 so


#B 8 : if else elif
# co () -> do uu tien cao nhat 
# and = & , or = || 
# if condition : 
#    code
#    code
# else : 
    # code
    # code
# Ex: 
# n=60
# if n>=50 and n<100 : 
    # print('Python')
    # print('Python2')
# else : print('Python3')

# * toan tu 3 ngoi:
# var = <true_code> if <condition> else <false_code> 
# Ex:
# var = 'True code' if (2>1) else 'false code'
# print(var)

# B 10,11,12,13,14,15,16 : Contest
#1/
# x = int(input('Nhap x: '))
# print(x)
# print("Hello world")

# 2/
# f=float(input())
# print('{:.2f}'.format(f))

# 3/
# s = "Pham Han!Minh Chuong"
# print(s.split('!'))
# ['Pham Han', 'Minh Chuong']
# syntax: map(data_type,list)
# list = nhap tu input -> split theo dau cach 
# x,y,z,t = map(int,input().split())
# print(var,step,end)
# step: k/c giua cac bien 
# end:ki tu ket thuc sau print 

# 4/
# x, y = map(int,input().split())
# print(x**y)
# pow(x,y) => float type 

# 5/
# from math import*
# a,b = map(float,input().split())
# # lay 2 so sau dau phay 
# print('Can ban hai: ','{:.2f}'.format(sqrt(a)))
# # lay 3 so sau dau phay 
# print('Can ban ba: ','{:.3f}'.format(pow(b,1/3)))

# cach2 
# from math import *
# n = int(input())
# res1 = sqrt(n)
# print('%.2f' % res1)
# res2 = pow(n,1/3)
# print('%.3f' % res2)


# 6/
# from math import*
# n = float(input())
# print(floor(n))
# print(round(n))
# print(ceil(n))

# 7/
# from math import*
# n = int(input())
# print(n%10)
# print(n%100)

# 8/
# from math import*
# a,b = map(int,input().split())
# print(a//b)
# print('%.2f' % (a/b))

#9/ tinh gia tri cua bieu thuc
# from math import*
# x = int(input())
# print(int(pow(x,3) + 3*pow(x,2) + x + 1))

# 10/
# from math import*
# r = float(input("Nhap r: "))
# print('P: ','%.2f' % (2*r*3.14))
# print('S: ','%.2f' % (r*r*3.14))

# 11/ distan from two point 
# from math import*
# a,b,c,d = map(int,input().split())
# print('Distance: ','%.2f' % (sqrt(pow(c-a,2) + pow(d-b,2))))

# 12/
# from math import*
# n = int(input())
# if n%3==0 and n%7!=0:
#     print('Yes')
# else:
#     print('No')

# so co > 2 chu so , tan cung la so nguyen to 
# r = n%10
# if n>=10 and n<=99 and ( r = 2 or r = 3 or r = 5 or r = 7):
#     print('Yes')
# else : print('No')

# 13/
# from math import*
# a,b = map(int,input().split())
# # so lon nhat <= a && %b == 0 
# if a//b>0 :
#     print(b*(a//b))
# else : print('No')

# # so nho nhat >= a && % b==0 

# if a//b>0 :
#     if a%b==0 : print(a)
#     else : print(b*(a//b + 1))
# else :
#     print('No')

# # 14/
# from math import*
# a,b,c = map(int,input().split())
# if a<0 or b<0 or c<0 or a+b<c or b+c<a or a+c<b :
#     print ('INVALID')
# else:
#     if a == b and b == c : print (1)
#     elif (a==b and a!=c) or (a==c and a!=b) or (c==b and a!=c) : print(2)
#     elif (pow(a,2) == pow(b,2) + pow(c,2)) or (pow(b,2) == pow(c,2) + pow(a,2)) or (pow(c,2) == pow(b,2) + pow(a,2)) : print(3)
#     else : print(4)

# 15/
# from math import*

# def isLeapyear(year):
#  if (year % 4==0 and year %100!=0 ) or (year %400==0) : 
#     return True
#  else :
#     return False
# x,y = map(int,input().split())
# if x<1 and x>12:print('INVALID')
# else:
#     if(x==1 or x==3 or x==5 or x==7 or x==8 or x==10 or x==12) : print(31)
#     elif(x==2) :
#         if (isLeapyear(y)) : print(29)
#         else : print(28)
#     else :print(30)

# 16/ doi nam sang so nam tuan ngay 
# from math import*
# n = int(input())
# print(n//365)
# n%=((n//365)*365)
# print(n//7)
# print(n%((n//7*7)))

# mua nuoc 
# from math import*
# n,a,b = map(int,input().split())
# if a<=b/2:
#     print (n*a)
# else:
#   if n%2==0 :
#     print(n//b*2)
#   else:
#     print((n-1)//2*b + a) 

# B15 ,16
# * Ma Asski: ord(var_char)
# Ex: 
# c = 'A' 
# print(ord(c))
# tmp = ord(c) + 1
# print (chr(tmp).lower())
# -> b 

# * Mot so ham char : c.islower(),c.isupper(),c.isdigit()

# 20/
# m,n,a= map(int,input().split())
# x,y=0,0
# if m%a==0:
#     x = m//a
# else:
#     x = m//a+1
# if n%a==0:
#     y = n//a 
# else:
#     y = n//a+1
# print(x*y)

# 21/ Frog
# a,b,k = map(int,input().split())
# if k%2==0:
#     print((k//2)*a - b*(k//2))
# else:
#     print((k//2+1)*a - b*(k//2))

# 23/ m,n : cho m bac thang , bc it nhat bao nhiu de tong so lan bc chia het cho n
# from math import*
# m,n = map(int,input().split())
# max_step = m
# min_step = 0
# if m%2==0:
#     min_step = m//2
# else:
#     min_step = m//2+1
# # tim so dau tien (min_max) ma chia het cho n 
# ans = (min_step + n-1)//n *n
# if ans<=max_step:
#     print(ans)
# else:
#     print(-1)

# 24/ min path 
# from math import*
# d1,d2,d3 = map(int,input().split())
# min_path = min(d1+d2+d3,2*d1+2*d3,2*d1+2*d2,2*d2+2*d3)
# print(min_path)

#25/
# count = 0
# n = int(input())
# count+=n//100
# n%=100
# count+=n//20
# n%=20
# count+=n//10
# n%=10
# count+=n//5
# n%=5
# print(count)

# B17 26 -> 30 
# 27/
# from math import*
# n = float(input())
# if n-0.5 == int(n):
#     print(ceil(n)) 
# else:
#     print(round(n))
# 28/ s(n) = n(u1+un)/2 
# un = u1+(n-1)d 
# CSC
#  29/
# from math import* 
# a,b,c,d = map(int,input().split())
# if b//a == c//b == d//c:
#     print("YES")
# else:
#     print("NO")
# 30/  Cnk = n!/(n-k)!*k!
# from math import*
# n = int(input())
# print(n*(n-1)//2)


# B18 LOOP 
# syn: for var in list/array 
#        code// 
#     else: 
#         code// 
# Ex:
# for (i in [1,2,3]) 
#   print(i)

# * Fun range: range (start,stop,step) == (value dau,value cuoi,step)
# start = 0 (default) 
# Ex:
# a = range(1,10,1)
# for i in a:
    # print(i,end = ' ') 
    # 1 2 3 4 5 6 7 8 9 

# Ex: sum 
# n = int(input())
# s = 0
# for i in range(n):
   
# Ex:Nhap n phan tu mang 
# n =int(input())
# newArray = []
# # i->n-1 
# for i in range(n):
#     newArray.append(input())
# print(newArray)

# # 3
# # 1   
# # 2
# # 3
# # ['1 ', '2', '3']

# Ex:
# # Prompt the user to input the number of elements
# n = int(input("Nhap so luong phan tu: "))

# # Prompt the user to input all the numbers on a single line, separated by spaces
# input_string = input("Nhap cac phan tu (cach nhau bang dau cach): ")

# # Convert the input string into a list of integers
# number_list = list(map(int, input_string.split()))

# # Check if the number of entered elements matches the specified count
# if len(number_list) != n:
#     print(f"Loi: Ban da nhap {len(number_list)} phan tu thay vi {n} phan tu.")
# else:
#     # Print the resulting list
#     print("Mang so da nhap la:", number_list)

# Break & continue 
# Ex: In cac so 1->20 gap so 7 thi dung 
# for i in range(1,21):
#     if i%7==0:
#         break
#     else:
#         print(i,end=' ')
# # Ex: bo qua Minh
# for i in range(1,5):
#     print('Chuong')
#     continue
#     print("Minh")

# B19 
# 0/
# from math import*
# n = int(input())
# for i in range(1,n+1,1):
#     print(i,end=' ',)
# print('\n')
# for i in range(n,-1,-1):
#     print(i,end=' ')
# print('\n')
# for i in range(1,n+1,2):
#     print(i,end=' ')
# print('\n')
# for i in range(0,n+1,2):
#     print(i,end=' ')
# print('\n')
# for i in range(1,n+1,1):
#     if i%4==0:
#         print(i,end=' ')
# print('\n')
# # in n chu cai in thuong dau tien 
# for i in range(ord('a'),ord('a')+n,1):
#     print(chr(i),end=' ')
# print('\n')

# # n chu cai in thuong cuoi 
# for i in range(ord('z')-n+1,ord('z')+1,1):
#     print(chr(i),end=' ')
# # for i in range()2


# 4/
# from math import*
# n = int(input())
# s = 0.0
# for i in range(1,n+1):
#     s+=(1/i)
# print('%.3f' % s)

# B20 
# from math import*
# n = int(input())
# tong = 0
# # isqrt() : can so nguyen 
# for i in range(1,isqrt(n)+1,1):
#     if n%i==0:
#         tong+=i
#         if i!=n//i:
#             tong+=n//i
# print(tong)

# 8/So chinh phuong
# from math import*
# n = int(input())
# for i in range(1,isqrt(n)+1,1):
#     print(i*i,end=' ')

# 10/ kiem tra list co so 2024 ko 
# from math import*
# n = int(input())
# array = []
# array = list(map(int,input().split()))
# for i in range(0,len(array)):
#     if array[i]==2022:
#         print("YES")
#         break

# Tech
# n = int(input())
# a = list(map(int,input().split()))
# if 2024 in a: print("YES")
# else : print("NO")

# B21 
# 11/ 
# from math import*
# s = 0
# n = int(input())
# for i in range(1,n+1,1):
#     if i%2==0:
#         s+=i
#     else:
#         s-=i
# print(s)
# * math.factorial(n) = n! 

# 16/
# n = int(input())
# if n==0:
#     print(1)
    
# else:
# 18/
#     cnt = 0
# while n!=0:
#     cnt+=1
#     n//=10
#  print(cnt)


# B22 
# 19/
# n=int(input())
# ans = n//28
# vo=ans
# while vo>=3:
#     temp = vo//3
#     ans+=temp
#     # cong lai so chai bia temp doi duoc(+temp) va bot di phan da doi (%3): tiep tuc doi
#     vo = vo%3 + temp
# print(ans)

# 20/
# n = int(input())

# if n % 2 == 0:
#     print(n // 2)
#     while n > 0:
#         print(2, end=' ')
#         n -= 2
# else:
#     print(n // 2)
#     while n > 3:
#         print(2, end=' ')
#         n -= 2
#     print(3, end=' ')

# 32/
# k2,k3,k5,k6 = map(int,input().split())
# k256 = min(k2,k5,k6)
# k23 = min(k2-k256,k3)
# print(k256 * 256 + k32*32)

# 33/
# a, b, c, d = map(int, input().split())
# if( a+b+c+d ) % 3 ==0:
#     tmp = (a+b+c+d) //3
#     if tmp>= a and tmp >=b and tmp>=c:
#         print("YES")
#     else:
#         print("NO")
# else:
#     print("NO")

# 34/
# a,b =map(int,input().split())
# print(1440-a*60-b)

# 33/
# a,b,c,d,e = map(int,input().split())
# sum = a+b+c+d+e
# if sum%5==0:
#     x = tong //5
#     if ton!=0:
#         print(tong)
# else:
#     print('NO')

# B24 while loop : while condition:
                    #    code
                    # else:
                        # code 
# B25: 
# 21/
# n = int(input())
# range(n) => i = 0 -> n-1 
# for i in range(n):
#     for j in range(n):
#          print('*',end='')
#         #  endl 
#     print(' ')

# # endl 
# print(' ')

# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print('*',end='')
#         else:print(' ',end='')
#     print(' ')


# print(' ')

# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print('*',end='')
#         else:print('#',end='')
#     print(' ')

# print(' ')

# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print (i+1,end='')
#         else: print(' ',end='')
#     print(' ')

# 5
# *****
# *****
# *****
# *****
# *****

# *****
# *   *
# *   *
# *   *
# *****

# *****
# *###*
# *###*
# *###*
# *****

# 11111
# 2   2
# 3   3
# 4   4
# 55555

   
#22/
# n =  int(input())

# for i in range(n):
#     for j in range(i+1):
#         print('*',end='')
#     print(' ')
         
# print(' ')

# for i in range(n):
#     for j in range(n-i,0,-1):
#         print('*',end='')
#     print(' ')
         
# print(' ')
         
# for i in range(n):
#     for j in range(n):
#         if j>=n-i-1:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print(' ')

# print(' ')

# for i in range(n):
#     for j in range(n):
#         if j>=i :
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print(' ')
    
# print(' ')

# for i in range(n):
#     for j in range(i+1):
#         if j==i or j==0 or i==n-1:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print(' ')

# 23/
# from math import*
# n = int(input())
# cnt=1
# for i in range(n):
#     for j in range(n):
#         print(cnt,end=' ')
#         cnt+=1
#     print(' ')
    
# print(' ')

# for i in range(n):
#     for j in range(n):
#         print(cnt,end=' ')
#         cnt+=1
#     cnt=i+2
#     print(' ')
    
# print(' ')

# for i in range(n):
#     for j in range(n):
#         if j>=n-i-1:
#             print(i+1,end='')
#         else: print('-',end='')
#     print(' ')
    
# print(' ')

# for i in range(1,n+1):
#     ktao = i
#     kc = n-1
#     for j in range(i):
#         print(ktao,end=' ')
#         ktao+=kc
#         kc-=1
#     print(' ')

# 24/ GCD a! , b! = a!
# import math
# a,b=map(int,input().split())
# print(math.factorial(min(a,b)))

# 25/
# import math
# n = int (input())
# sum=0.0
# for i in range(n):
#     sum+=1/(math.factorial(i))

# print('%.4f' % sum)

# 26/
# a,b,n=map(int,input().split())
# check=False
# for i in range(0,n//a+1):
#     temp = n-i*a 
#     if temp % b==0:
#         check = True
#         break

# if check : print('YES')
# else:print('NO')

# 27/
# n=int(input())
# while n//10!=0:
#     sum=0
#     while(n!=0):
#      temp = n%10
#      sum+=temp
#      n//=10
#     n=sum
# print(n)

# 28/
# import math
# n=int(input())
# sum=0
# for i in range(1,n+1):
#     sum+=(math.factorial(i))
# print(sum)

# 29/
# import math
# n=int(input())
# a=list(map(int,input().split()))
# sum=0
# for i in a:
#     if i%2==0:
#         sum+=i
# print(sum)

# # 30/
# from math import*
# t = int(input())
# for i in range(t):
#     n=int(input())
#     if n%2==0:
#         print('EVAN')
#     else:
#         print('ODD')

# B27 
# syntax: def namefun(arguments):
    #   code 
    #  return value 

# if __name__ == '__main__':    (int main(){})
# code 



# Ex: 
# def tong(a,b):
#     res = a+b
#     return res

# def xinchao(name1,name2,name3):
#     print('Xin chao',name1,name2,name3)

# if __name__ == '__main__':
# xinchao('Teo','Ty','Chuong')
# xinchao(name2='Chuong',name1='Teo',name3='Ty')
# m,n=10,20
# print(tong(m,n))


# Ex: 

# def change(n):
    # n*=2

# if __name__ == '__main__':
    # n = 10
    # change(n)
    # print(n)
    # =10 

# Ex: 
# def gt(n):
#     res=1
#     for i in range(1,n+1):
#         res*=i
#     return res

# def luythua(a,b):
#     res=1
#     for i in range(1,b+1):
#         res*=a
#     return res

# if __name__ == '__main__':
#     print(gt(4))
#     print(luythua(2,4))

# B28 
# Ex: 
# def tongUoc(n):
#     sum=0
#     for i in range(1,n+1):
#         if n%i==0:
#             sum+=i
#     return sum

# def demUoc(n):
#     cnt=0
#     for i in range(1,n+1):
#         if n%i==0:
#             cnt+=1
#     return cnt

# if __name__ == '__main__':

#     print(tongUoc(24))
#     print(demUoc(8))

# => toi uu: duyet toi can(n)
# Ex:
# from math import*
# def tongUoc(n):
#     sum=0
#     for i in range(1,isqrt(n)+1):
#          if n%i==0:
#             sum+=i
#             if i!=n//i:
#                 sum+=n//i
#     return sum

# def demUoc(n):
#     cnt=0
#     for i in range(1,isqrt(n)+1):
#         if n%i==0:
#             cnt+=1
#             if i!=n//i:
#                 cnt+=1
#     return cnt

# if __name__ == '__main__':

#     print(tongUoc(24))
#     print(demUoc(8))

# B29
# *Note: code check true/false -> tim dieu kien sai -> return true trong th ngc lai 
# Ex: prime 
# from math import*
# def prime(n):
#     for i in range(2,isqrt(n)+1):
#         if n%i==0:
#             return False
#     return n>1

# if __name__ == '__main__':
#     for i in range(1,101,1):
#         if(prime(i)):print(i,end=' ')

# B30
# Ex: phan tich thua so nt 
# from math import*
# def tsnt(n):
#     for i in range(2,isqrt(n)+1):
#         while n%i==0:
#             print(i,end=' ')
#             n//=i
#     if n>1:
#         print(n)


# if __name__ == '__main__':
#     print(tsnt(60))

# B31 
# Ex: So chinh phuong & so lap phuong
# from math import*
# def check(n):
#     x = isqrt(n)
#     return pow(x,2) == n

# def check2(n):
#     x = (int)(pow(n,1/3))
#     return pow(x,3) == n
# if __name__ == '__main__':
#     for i in range(1,101,1):
#         if check(i):
#             print(i,end=' ')
#     print(' ')
#     for i in range(1,101,1):
#         if check2(i):
#             print(i,end=' ')

# B32 Gcd,lcm 
# def gcd(a,b):
#     if(b==0):
#         return a
#     return gcd(b,a%b)

# def lcm(a,b):
#     return a*b//gcd(a,b)

# if __name__ == '__main__':
#     print(gcd(15,7))

# B33: C n k ,  C n 2 = (n*(n-1))/2 
# import math
# def tohop(n,k):
#     return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))

# if __name__ == '__main__':
#     print(tohop(5,3))

# B34 : so Fibo 
# import math
# # Ex: in n fibo dau tien 
# def fibo(n):
#     if n==1:
#        print('0','\n')
#     elif n==2:
#        print('0 1')
#     else:
#        print('0 \n1')
#        f2,f1 = 1,0
#        for i in range(2,n+1):
#         fn = f1 + f2
#         print(fn,end='\n')
#         f2,f1 = fn,f2

# # Ex: check fibo 
# def checkFibo(n):
#    if n==0 or n==1:
#       return True
#    f1,f2 = 0,1
#    for i in range(2,100):
#       fn = f1 + f2
#       if fn==n:return True
#       f2,f1 = fn,f2
#    return False
# # Ex: Print fibo 
# def printFibo(n):
#    if n==0 or n==1:
#       return n
#    f1,f2 = 0,1
#    for i in range(2,n+1):
#       fn = f1 + f2
#       f2,f1 = f1,fn 
#    return fn
# if __name__ == '__main__':
#     print(fibo(143))
#     # for i in range(1,200):
#     #    if checkFibo(i):
#     #       print(i,end=' ')

# B35: so thuan nghich 
# import math
# def tn(n):
#     tmp = n
#     s=0
#     while(n!=0):
#         s=s*10 + n%10
#         n//=10
#     return tmp==s
# if __name__ == '__main__':
#     print(tn(int(123321)))
#     print(tn(1221))

# B36: so hoan hao : tong uoc(ko tinh chinh no) = chinh no
# from math import* 
# def shh(n):
#     sum=0
#     for i in range(1,isqrt(n)+1):
#         if n%i==0:
#             if i!=n//i: sum+=(i+n//i)
#             else: sum+=i
#     return sum-n == n

# if __name__ == '__main__':
#     for i in range(1,1001):
#         if(shh(i)):print(i,end=' ')

# B37: ly thuyet dong du : 
# (A+B)%C = ((A%C) + (B%C)) % C
# (A-B)%C = ((A%C) - (B%C) + C)%C
# (A*B)%C = ((A%C) * (B%C)) % C
# (A/B)%C = ((A%C) + (B^-1%C)) % C
# => bai taon yeu cau chia cho mot so nao do -> tinh den dau chia den do 
# import math
# if __name__ == '__main__':
#     mod = (math.pow(10,9)+7)
#     n = int(input())
#     res = 1
#     for i in range(1,n+1):
#         res*=i
#         res%=mod
#     print(res%mod)


    # a,b,c = map(int,input().split())
    # # print((a**b)%c)
    # res=1
    # for i in range(b):
    #     res*a
    #     res%=c
    # print(res)


# B38 
# from math import*
# def b1_check_prime(n):
#     for i in range(2,isqrt(n)+1):
#         if n%i==0: return 0
#     return n>1

# def b2_sum(n):
#     sum=0
#     while(n):
#         sum+=(n%10)
#         n//=10
#     return sum

# def b3_sum_evan(n):
#     sum=0
#     while(n):
#         if((n%10)%2==0):
#          sum+=(n%10)
#         n//=10
#     return sum

# def b4_sum_prime(n):
#     sum=0
#     while(n):
#         if(b1_check_prime(n%10)):
#          sum+=(n%10)
#         n//=10
#     return sum

# def b5_reverse_num(n):
#    sum=0
#    while(n):
#       sum=sum*10 + n%10
#       n//=10
#    return(sum)

# def b6_count_prime(n):
#    cnt=0
#    for i in range(2,isqrt(n)+1):
#       while (n%i==0 and b1_check_prime(i)):
#          cnt+=1
#          n//=i
#    if(b1_check_prime(n)) : cnt+=1
#    return cnt

# def b7_max_prime(n):
#    res = 0
#    for i in range(2,isqrt(n)+1):
#       while (n%i==0 and b1_check_prime(i)):
#          res = max(res,i)
#          n//=i
#    if(b1_check_prime(n)) : res = max(res,n)
#    return res

# def b8_check_6(n):
#     while(n):
#         if (n%10)==6: return 1
#         n//=10
#     return 0

# def b9_check_sum(n):
#     sum=0
#     while(n):
#         sum+=(n%10)
#         n//=10
#     if sum%8==0:return 1
#     else: return 0

# def b10_sum_gt(n):
#     sum=0
#     while(n):
#         sum+=factorial(n%10)
#         n//=10
#     return sum

# def check_11(n):
#    tmp=n%10
#    while(n):
#       if(n%10!=tmp) : return 0
#       n//=10
#    return 1

# def check_12(n):
#    tmp=n
#    res=0
#    while(n):
#       res = max(res,n%10)
#       n//=10
#    if(res==tmp%10): return 1
#    else: return 0

# def check_13(n):
#    tmp=n
#    count_num=0
#    while(tmp):
#       count_num+=1
#       tmp//=10
#    sum=0
#    while(n):
#       sum+=(pow(n%10,count_num))
#       n//=10
#    return sum
# if __name__ == '__main__':
#     print(check_13(123))

# B39 
# 15/ so sphenic 
# Ex: 30 = 2x5x3 (so sphenic) , 60=2x2x3x5(ko phai so sphenic)
# from math import*
# def sphenic(n):
#     cnt=0
#     for i in range(2,isqrt(n)+1):
#         if n%i==0:
#             mu=0
#             while(n%i==0):
#              mu+=1
#              n//=i
#             if mu>=2 : return False
#             cnt+=1
#     if n>1 : cnt+=1
#     return cnt==3

# if __name__ == '__main__':
#     # for i in range(1,101):
#         # if(sphenic(i)): print(i,end=' ')
#     print(sphenic(30))

# 16/ in tsnt: 2^2 * 3^1 * 5^1
# from math import*
# def tsnt(n):
#     for i in range(2,isqrt(n)+1):
#         if n%i==0:
#           mu=0
#           while n%i==0:
#                 mu+=1
#                 n//=i
#           print(i,mu,sep='^',end='')
#           if n!=1 :
#               print(' * ',end='')
#     if n>1 : print (n,1,sep='^')

# if __name__ == '__main__':
#     tsnt(60)

# 17/ uoc max la so nt 
# from math import*
# def solve(n):
#     res=0
#     for i in range(2,isqrt(n)+1):
#         if n%i==0:
#             mu=0
#             while(n%i==0):
#                 mu+=1
#                 n//=i
#             res=i
#     if n>1 : res = n
#     return res

# if __name__ == '__main__':
#     print(solve(17))
        
# 18/ so smith 
# from math import*
# def check_prime(n):
#     for i in range(2,isqrt(n)+1):
#         if n%i==0: return False
#     return n>1

# def sum_num(n):
#     sum=0
#     while(n):
#         sum+=(n%10)
#         n//=10
#     return sum
# def solve(n):
#     sum1=sum_num(n)
#     sum2=0
#     tmp=n
#     for i in range(2,isqrt(n)+1):
#         if n%i==0:
#             while(n%i==0): 
#                 sum2+=sum_num(i)
#                 n//=i
#     # n la so nt 
#     if tmp==n: return False
#     if n>1:sum2+=sum_num(n)
#     return sum1==sum2

# if __name__ == '__main__':
#     print(solve(22))

# B40 
# 1/ in so cp [a,b]

# from math import*
# if __name__ == '__main__':
#     a,b, = map(int,input().split())
#     can1 ,can2 = isqrt(a),isqrt(b)
#     # vd a=10 -> 3 sai 
#     if can1*can1!=a : can1+=1
#     # b la so cp -> 9999,999
#     if (can2+1)*(can2+1) == b:
#           can2+=1
#     # for i in range(can1,can2+1):
#             # print(i*i,end=' ')
#     print(can2-can1+1)


# 2 so co so luong uoc le = so chinh phuong

# B41 
# 6/ so thuan nguyen to
# import math
# def check_prime(n):
#     for i in range(2,math.isqrt(n)+1):
#         if n%i==0 : return False
#     return n>1

# def check_sum_prime(n):
#     sum = 0 
#     while(n):
#         sum+=(n%10)
#         n//=10
#     return check_prime(sum)

# def check_num_prime(n):
#     while(n):
#         if (check_prime(n%10)==False) : return False
#         n//=10
#     return True

# def solve(n):
#     return check_prime(n) and check_num_prime(n) and check_sum_prime(n)
# if __name__ =='__main__':
#   cnt=0
#   a,b = map(int,input().split())
#   for i in range(a,b+1):
#       if(solve(i)) : cnt+=1
#   print(cnt,end='\n')

# 27/  so co 3 uoc so nguyen to khac nhau
# import math
# # so tn 
# def check_tn(n):
#     tmp = n
#     sum = 0
#     while(n):
#         sum = sum*10 + n%10 
#         n//=10
#     return sum == tmp

# def solve(n):
#     cnt=0
#     for i in range(2,math.isqrt(n)+1):
#         if n%i==0:
#             cnt+=1
#             while(n%i==0):
#                 n//=i
#     if n!=1:cnt+=1
#     return cnt>=3
# if __name__ == '__main__':

#     a,b = map(int,input().split())
#     for i in range(a,b+1):
#         if(solve(i) and check_tn(i)) : print(i,end=' ')

#  29/ so tn && sum co chu so cuoi =8 , chua it nhat 1 so 6
# import math
# def solve(n):
#     tmp=n
#     rev=0
#     sum=0
#     ok = False
#     while(n):
#         rev=rev*10 + n%10
#         if n%10==6: ok = True
#         sum+=n%10
#         n//=10
#     return ok and sum%10==8 and rev==tmp
# if __name__ == '__main__':
#     a,b=map(int,input().split())
#     cnt=0
#     for i in range(a,b+1):
#         if(solve(i)):print(i,end='')

# 30 
# from math import*
# def check_prime(n):
#     for i in range(2,isqrt(n)+1):
#         if n%i==0: return False
#     return n>1

# def solve(n):
#     tmp = n
#     max_num = 0
#     while(n):
#         max_num = max(max_num,n%10)
#         n//=10
#     return max_num == tmp%10 and check_prime(tmp)  

# if __name__ == '__main__':
#     n = int(input())
#     cnt=0
#     for i in range(1,n+1):
#         if(solve(i)):
#             print(i,end=' ')
#             cnt+=1
#     print(cnt)

# B42 
# 41/ so thuan nghich upgrade 
# import math
# def check(n):
#     tmp=n
#     cnt=0
#     while(tmp):
#         cnt+=1
#         tmp//=10
#     n1 = int(n//(math.pow(10,cnt-1)))
#     n2 = n %10
#     # lay so o giua so dau va cuoi 
#     tn_num =int((n-n1*math.pow(10,cnt-1))//10)
#     temp = tn_num 
#     sum=0
#     while(temp):
#         sum = sum*10 + temp%10
#         temp//=10
#     return (sum==tn_num) and (n1==2*n2 or n2==2*n1)

# def tn(n):
#     rev=0
#     tmp=n
#     while(n):
#         rev = rev*10 + n%10
#         n//=10
#     return rev==tmp

# def check_2(n):
#     last = n%10
#     m=0
#     n//=10
#     while n>=10:
#         m=m*10+n%10
#         n//=10
#     return (n==2*last or last==2*n) and (tn(m))

# if __name__ == '__main__':
#     n = int(input())
#     if check_2(n):print("YES")
#     else:print("NO") 

# 45/ 
# def check(n):
#  for i in range(0,n//111+1):
#     if (n-111*i)%11==0: return True
#  return False 
# n = int(input())
# if check(n):print("YES")
# else: print("NO")

# 46/ SO hoan hao  (nt + tong uoc = chinh no)
# import math
# def prime(n):
#     for i in range(2,math.isqrt(n)+1):
#         if n%i==0: return False
#     return n>1

# def check(n):
#     for i in range(2,33):
#         if(prime(i) and prime(2**i-1)):
#             if(2**i-2) * (2**(i-1)) == n:
#                 return True
#     return False

# 32/ in ra so nguyen to thu k 
# import math
# def solve(n,k):
#     cnt=0
#     for i in range(2,math.isqrt(n)+1):
#         if n%i==0:
#             while(n%i==0):
#              cnt+=1
#              if(cnt==k):
#                  return i
#              n//=i
#     if n!=1 : cnt+=1
#     if cnt==k : return n 
#     return -1

# if __name__ =='__main__':
#     print(solve(28,3))

# B43 
# 18/
# import math
# def solve(n):
#     for i in range(2,math.isqrt(n)+1):
#         if n%i==0:
#             mu = 0
#             while(n%i==0):
#                 mu+=1
#                 if mu==2 : return True
#                 n//=i 
#     if n!=1: return False 

# if __name__ == '__main__':
#     a,b = map(int,input().split())
#     for i in range(a,b+1):
#         if solve(i) : print(i,end=' ')

# 19 so chia het cho 1 so nguyen to -> cx phai chia het cho binh phuong so do 
# import math
# def solve(n):
#     for i in range(2,math.isqrt(n)+1):
#         if n%i==0:
#             mu = 0
#             while(n%i==0):
#                 mu+=1
#                 n//=i 
#             if mu==1 : return False
#     if n!=1: return False 
#     return True

# if __name__ == '__main__':
#     a,b = map(int,input().split())
#     for i in range(a,b+1):
#         if solve(i) : print(i,end=' ')
  
# 17
# import math
# def nt(n):
#     for i in range(2,math.isqrt(n)+1):
#         if n%i==0: return False
#     return n>1
# def check(n):
#     for i in range(n,n//2+1,-1):
#         if nt(i) and nt(n-i) :
#             print(n-i,i,sep=' ',end='\n')
  
# if __name__ == '__main__':
#     t=int(input())
#     while(t):
#         n = int(input())
#         check(n)
#         t-=1 

# 18/  so nho nhat co t chu so chia het x,y,z 
# from math import*
# def gcd(a,b):
#     if b==0:return a
#     return gcd(b,a%b)

# def lcm(a,b):
#     return (a*b) / gcd(a,b)

# def check(x,y,z,t):
#     tmp = 10**(t-1)
# so nho nhat chia het cho boi chung 
#     ans = (tmp + lcm -1) // lcm * lcm 
#     if ans < 10**t:
#         return ans
#     return -1

# 19/ liet ke cac cap nguyen to cung nhau 

# from math import*
# def gcd(a,b):
#     if b==0:return a
#     return gcd(b,a%b)

# def lcm(a,b):
#     return (a*b) / gcd(a,b)

# def solve(a,b):
#     for i in range(a,b):
#         for j in range(i+1,b+1):
#             if(gcd(i,j)==1) :
#                 print("(",i,",",j,")",sep='')
        

# if __name__ == '__main__':
#     solve(5,10)

# B44 
# 1/ 
# def fibo(n):
#     f0 = 1
#     f1 = 1
#     if n==1:print(1)
#     elif n==2: print(1,1,sep='\n')
#     else:
#      print(1,1,sep='\n')
#      for i in range(1,n-1):
#          fn = f0 + f1 
#          print(fn)
#          f1,f0 = fn,f1 

# if __name__ == '__main__' :
#     n = int(input())
#     fibo(n)

# 2/ check fibo

# def check(n):
#     if n==0 or  n==1 : return True
#     f0 = 0
#     f1 = 1
#     for i in range(1,93):
#         fn = f0 + f1
#         if n==fn : return True
#         f0,f1 = f1,fn
#     return False
        
# if __name__ == '__main__' :
#     n = int(input())
#     if check(n): print("YES")
#     else: print("NO")


# 3/ 
# def check(n):
#     if n==0 or  n==1 : return True
#     f0 = 0
#     f1 = 1
#     for i in range(1,93):
#         fn = f0 + f1
#         if fn>n : return fn
#         f0,f1 = f1,fn
#     return -1

# if __name__ == '__main__' :
#     n = int(input())
#     print(check(n))

# 4/ 
# import math
# def prime(n):
#     for i in range(2,math.isqrt(n)+1):
#         if n%i==0: return False
#     return n>1

# def fibo(n):
#     if n==0 or  n==1 : return True
#     f0 = 0
#     f1 = 1
#     for i in range(1,93):
#         fn = f0 + f1
#         if n==fn : return True
#         f0,f1 = f1,fn
#     return False

# def solve(n):
#     tmp = n
#     sum=0
#     while(n):
#         sum+=n%10
#         n//=10
#     return prime(tmp) and fibo(sum) 

# if __name__ == '__main__':
#     n = int(input())
#     for i in range(1,n+1):
#         if (solve(i)) : print(i,end=' ')



# B46: Recursion 

# def s(n) :
#     if n==0: return 0
#     else: return n+s(n-1)

# def sum_digit(n):
#     if n<10: return n
#     return n%10 + sum_digit(n//10)

# def C(n,k):
#     if k==0 or k==1:
#         return 1
#     return C(n-1,k-1) + C(n-1,k)

# def decToBin(n):
#     if n<2: 
#         print(n,end='')
#         return
#     decToBin(n//2)
#     print(n % 2,end='')
# if __name__ == '__main__':
#     print(s(4))


# # B47 Contest
# def s(n):
#     if n==0:return 0
#     else:
#         if n%2==0:return n + s(n-1)
#         else: return -n + s(n-1)
# # c2 
# def s2(n):
#     if n==0:return 0
#     else:
#         return (-1)**n * n + s2(n-1)
    
# B48 
# def fibo(n):
#     if n==1: return 0
#     if n==2 : return 1
#     return fibo(n-1) + fibo(n-2)

# *Luy thua nhi phan a^b
# def powMod(a,b):
#     if b==0: return 1
#     x = powMod(a,b//2)
#     if b%2==1: return x*x*a % (10**9 +7)
#     else : return x*x % (10**9 + 7)

# if __name__ == '__main__':
#     a,b = map(int,input().split())
#     print(powMod(a,b))
# Ex: 2,5 -> 2,2 -> 2,1 -> 2,0 -> x = 1 -> x = 2  -> x = 4 -> x = 32 

# * S(n) = 1/1 + 1/2 + 1/3 + .. + 1/n 
# def s(n):
#     if n==1:return 1
#     return 1/n + s(n-1)

# if __name__ == '__main__':
#     print(s(4))

# B49 
# def decToBin(n):
#     if n!=0:
#         decToBin(n//2)
#         print(n%2,end='')
    
# if __name__ == '__main__':
#     decToBin(13)

# *chuyen he 16 ( phan du <10 -> num else  A->F)
# from math import*
# def DectoHex(n):
#     if n!=0:
#         DectoHex(n//16)
#         r = n%16
#         if r<10:
#             print(r,end='')
#         else:
#             print(chr(r+55),end='')
    
# if __name__ == '__main__':
#     n = int(input())
#     if n==0:print(0)
#     else:
#      DectoHex(n)
#     #  995 -> 3E3 

# B50 
# 16/ tim max/min digit of n
# def M(n):
#     if n<10 : return n
#     return max(n%10,M(n//10))

# def m(n):
#     if n<10 : return n
#     return min(n%10,m(n//10))

# if __name__ == '__main__':
#     print(M(23454321323),m(1234567654321))

# 17/ in so 

# import math 
# def In(n):
#     if n<10: 
#         print(n,end='')
#         # return
#     else:
#      print(n%10,end=' ')
#      return In(n//10)

# def In2(n):
#    if n<10: print(n,end=' ')
#    else :
#       In2(n//10)
#       print(n%10,end=' ')

# # 1234 -> 123 -> 12-> 1 : print (1) , print(12%10) ,...
# if __name__ == '__main__':
#     In2(12345)
   

# 18 / sum digit odd even 
# giong bai sum_digit: them dk so chan 
# def sum(n):
#     if n<10 and n%2==0: return n
#     if n%2==0:
#      return (n%10 + sum(n//10))
#     else: return sum(n//10)

# if __name__ == '__main__':
#     print(sum(1124678923))

# 19/ check all digit is even ? 
# def sum(n):
#     if n<10 and n%2==0: return True
#     if n%2==0:
#      return sum(n//10)
#     else: return False

# if __name__ == '__main__':
#     print(sum(222222468))

# 20 Dem so thao tac
# def count(n):
#     if(n==1) : return 0
#     if n%3 == 0:
#         return (1 + count(n//3))
#     elif n%2 == 0:
#         return (1 + count(n//2))
#     else: return (1 + count(n-1))

# def count_c2(n):
#     if n==1:
#         return 0
#     tt1,tt2,tt3 = 10**9,10**9,10**9
#     if n%2==0:
#         tt1 = 1 + count_c2(n//2)
#     if n%3==0:
#         tt2 = 1 + count_c2(n//3)
#     if n>1 :
#         tt3 = 1 + count_c2(n-1)
#     return min(tt1,tt2,tt3)
# if __name__ == '__main__':
#     print(count(100),end='\n')
#     print(count_c2(100))

# B51 
# 1/ check mang doi xung 
# def check(a,l,r):
#     if l>=r : return True
#     if a[l]!=a[r]: return False
#     else : return check(a,l+1,r-1)

# if __name__ == '__main__':
#     n = int(input())
#     a = list(map(int,input().split()))
#     if(check(a,0,n-1)) : print('YES')
#     else: print('NO')

# 2/ in mang bang de quy 
# def In_Rev(a,n):
#     if n>=1:
#         print(a[n-1],end=' ')
#         In_Rev(a,n-1)

# def In(a,n):
#     if n>=1 :
#         In(a,n-1)
#         print(a[n-1],end=' ')

# if __name__ == '__main__':
#     n = int(input())
#     a = list(map(int,input().split()))
#     In(a,n)
#     In_Rev(a,n)

# 3/ kiem tra mang toan chan 
# def check(a,n):
#     if n>=1:
#         if a[n-1]%2==1: return False
#         else: return check(a,n-1)
#     return True

# 4/ kiem tra mang tang dan 
# def check(a,n):
#     if n==1: return True
#     else :
#         if a[n-1]<=a[n-2]: return False
#         else: return check(a,n-1)
#     return True     

# 5/ binary search
# from math import*
# def binary_search (a,l,r,x):
#     if l>r : return False
#     m = (l+r)//2
#     if a[m] == x : return True
#     elif a[m]>x: return binary_search(a,m+1,r,x)
#     else: return binary_search(a,l,m-1,x)

# if __name__ == '__main__':
#     n = int(input())
#     a = list(map(int,input().split()))
#     a.sort()
#     x = int(input())
#     if binary_search(a,0,n-1,x): print(1)
#     else: print(0)


# B53 range of variable 
# * n global 
# n = 500
# def local_scope():
#     # cu phap sd bien toan cuc 
#     global n
#     n=100
#     print(n)

# # * enclosing scope : var khai bao sau ->
# def outer():
#     x = 2804
#     def outer2():
#         nonlocal x
#         x = 1010
#         print(x)
#     outer2()
#     print(x)
# outer()

# if __name__ == '__main__':
#     outer()

# B59 Dang toan co ban tren list 

# Ex: tim cap nguyen to cung nhau 
# from math import *
# n = int(input())
# a = list(map(int, input().split()))
# dem = 0
# for i in range(n):
#     for j in range(i+1,n):
#         if(gcd(a[i],a[j]) == 1):
#             dem+=1
# print(dem)



