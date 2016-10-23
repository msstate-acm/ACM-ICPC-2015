
n = int(input())
d = []
for _ in range(n):
    d.append(input()[::-1])
d.sort()
for s in d:
    print(s)
