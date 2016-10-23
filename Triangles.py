tri1 = list(map(int, input().split()))
tri2 = list(map(int, input().split()))

tri1.sort()
tri2.sort()

if tri1 != tri2:
    print(0)
elif tri1[0]**2 + tri1[1]**2 == tri1[2]**2:
    print(1)
else:
    print(0)
