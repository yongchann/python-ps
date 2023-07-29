# https://www.acmicpc.net/problem/11655

# import codecs

# print(codecs.encode(input(), 'rot13'))

answer = ""

for i in input():
    n = ord(i)
    if 65 <= n <= 90:
        t = n+13 if n+13 <= 90 else 64+(n+13)%90
        answer += chr(t)
    elif 97 <= n <= 122:
        t = n+13 if n+13 <= 122 else 96+(n+13)%122
        answer += chr(t)
    else:
        answer += i
        
print(answer)
        