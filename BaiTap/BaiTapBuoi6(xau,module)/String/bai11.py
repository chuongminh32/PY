# gap ki tu trung -> xoa het tat ca ki tu truoc do -> tao chuoi con moi 
# * sliding windown 
# def longest_sub_str(origin_s):
#     set_s = set()  #set: ko thu tu ko trung
#     left = 0
#     max_len = 0
#     max_sub = ""

#     for right in range(len(origin_s)):
#         # Neu gap ki tu trung thi xoa ki tu ben trai cho toi khi het trung 
#         while origin_s[right] in set_s:
#             set_s.remove(origin_s[left])
#             left += 1
        
#         # neu chua co ki tu trung -> them vao set 
#         set_s.add(origin_s[right])

#         # cap nhat ki luc : len & sub_s
#         if len(set_s) > max_len:
#             max_len = len(set_s)
#             max_sub = origin_s[left:right + 1]

#     return max_len, max_sub

# if __name__ == "__main__":
#     s = input("Nhap s: ")
#     len, sub = longest_sub_str(s)
#     print(len, sub, end=" ")



# abcabcbb -> 3 abc 
# * dynamic 
# dp[i] = a -> do dai xau con khong lap ki tu = a tinh toi vi tri i trong xau 
# char_index[s[i]] = j -> luu vi tri index ki tu s[i]: luu vet lan xh cuoi cung cua ki tu s[i]
# def solve(s):
#     char_index = {}
#     start_index = 0
#     max_len = 0
#     dp = [0] * len(s)

#     for i in range(len(s)):
#         if s[i] in char_index:
#             # dp[i] = dp[i-1] + 1: neu s[i] ko gay ra su trung lap voi phan truoc do xau con 
#             # dp[i] = i - char_index[s[i]] do dai xau con se gioi han voi lan xh s[i] truoc do 
#             dp[i] = min(dp[i-1] + 1, i - char_index[s[i]])
#         else:
#             # neu chua xh trong tu dien -> ++1 
#             dp[i] = dp[i-1] + 1 if i > 0 else 1
        
#         # mark s[i] - index of s[i]
#         char_index[s[i]] = i

#         # update max len 
#         if dp[i] > max_len:
#             max_len = dp[i]
#             start_index = i - max_len + 1
        
#     return s[start_index:start_index + max_len], max_len 

# if __name__ == "__main__":
#     s = input("s: ")
#     print(solve(s))

