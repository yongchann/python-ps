# https://www.acmicpc.net/problem/2979

price =[0] + list(map(int, input().split()))
time = [0] * 101

for _ in range(3):
    start, end = map(int, input().split())
    for i in range(start, end):
        time[i] += 1
    
answer = 0    
for i in time:
    answer += (price[i] * i)

print(answer)