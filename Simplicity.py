s = input()
d = {}
for ch in s:
    d[ch] = d.get(ch, 0) + 1

sl = sorted(d.keys())
if not d:
    print(0)
    exit()
del d[sl[0]]
if not d:
    print(0)
    exit()
del d[sl[1]]
print(sum(d.values()))
