n = int(input())

l = [int(input()) for _ in range(n)]
l.sort()

listLength = len(l)
minPairing = pow(10,6)
for i in range(listLength//2):
    minPairing = min(minPairing, l[i] + l[listLength-1-i])
print(minPairing)
