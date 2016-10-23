n = int(input())


class Person:
    length = 0
    def __init__(self, inputString):
        s = inputString.split()
        self.name = s[0][:-1]
        s = s[1:-1]
        self.s = s[::-1]
        Person.length = max(len(self.s), Person.length)
        
    def getClassNum(self):
        num = ''.join(map(self.filterFunction, self.s))
        pad = '1'*(Person.length - len(num))
        return num + pad
        
    def filterFunction(self, classString):
        if classString == "upper":
            return '2'
        elif classString == "middle":
            return '1'
        else:
            return '0'      


people = []
for _ in range(n):
    people.append(Person(input()))

people.sort(key=lambda p: p.name)
people.sort(key=lambda p: p.getClassNum(), reverse=True)
for p in people:
    print(p.name)
    
