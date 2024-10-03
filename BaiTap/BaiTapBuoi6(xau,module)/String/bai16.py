

# xau con ngan nhat chua tat ca ki tu
# len dict = len key(s[i]) 
# def solve(s):
#     char_set = set(s)
#     char_count = {}
#     min_len = float('inf')
#     max_sub = ""
#     left = 0

#     for right in range(len(s)):
#         # get -> get value dict 
#         # neu chua co trong tu dien -> 's[i]' = '0' else ++ 
#         char_count[s[right]] = char_count.get(s[right], 0) + 1
        
#         # da day du cac ki tu -> toi uu tim xau ngan nhat 
#         while (len(char_count) == len(char_set)):

#             current_len = right - left + 1

#             if current_len < min_len:
#                 max_len = current_len
#                 max_sub = s[left:right+1]

#             char_count[s[left]] -= 1

#             if char_count[s[left]] == 0:
#                 del(char_count[s[left]]) 
            
#             left += 1
    
#     return max_len, max_sub

# if __name__ == "__main__":
#     s = input("Nhap s: ")
#     print(solve(s))


        