# https://www.acmicpc.net/problem/1159
# Counter
# defualtdict
# list comprehension

# from collections import defaultdict

# m = defaultdict(int)
# for _ in range(int(input())):
#     m[input()[0]] += 1

# ans = ""
# for k in m:
#     if m[k] >= 5:
#         ans += k
        
# if not ans:
#     print("PREDAJA")
# else:
#     print("".join(sorted(ans)))


from collections import Counter

m = Counter(input()[0] for _ in range(int(input())))
ans = "".join(k for k, v in m.items() if v >= 5)

if not ans:
    print("PREDAJA")
else:
    print("".join(sorted(ans)))
