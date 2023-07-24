# https://www.acmicpc.net/problem/10988

# int(True) -> 1
# int(False) -> 0

str = input()
answer = 0
if str == str[::-1]:
    answer = 1
    
print(answer)
