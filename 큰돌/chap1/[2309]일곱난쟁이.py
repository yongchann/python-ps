# https://www.acmicpc.net/problem/2309

from itertools import combinations

data = []
for _ in range(9):
    data.append(int(input()))
    
answer = []
for i in list(combinations(data, 7)):
    if sum(i) == 100:
        answer = list(i)
        break
        
answer.sort()
for i in answer:
    print(i)