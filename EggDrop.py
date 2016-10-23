n, floors = list(map(int, input().split()))

d = dict()
d["SAFE"] = 1
for _ in range(n):
    s = input().split()
    floor = int(s[0])
    safety = s[1]
    if safety == "SAFE":
        d["SAFE"] = max(floor, d["SAFE"])
    else:
        d["BROKEN"] = min(floor, d.get("BROKEN", floors))


s = d["SAFE"]

if "BROKEN" not in d:
    print(s+1, s)
else:
    b = d["BROKEN"]
    if s+1 == d:
        print(s, b)
    else:
        print(s+1, b-1)
