from functools import reduce

s = input()

i = 0
while len(s) > 1:
    i += 1
    s = str(reduce(lambda x,y: x*y, list(map(int, list(s)))))
    
print(i)
    