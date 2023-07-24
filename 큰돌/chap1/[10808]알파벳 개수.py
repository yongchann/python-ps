# https://www.acmicpc.net/problem/10808

# alpha_map = {}
# src = "abcdefghijklmnopqrstuvwxyz"

# for alpha in src:
#     alpha_map[alpha] = 0
    
# str = input()
# for s in str:
#     alpha_map[s] += 1
    
# print(*alpha_map.values())

ans = [0] * 26
for s in input():
    ans[ord(s) - 97] += 1
    
print(*ans)