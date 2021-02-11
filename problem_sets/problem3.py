lst = []
n = int(input("Element Sayısı: "))
for j in range(0, n):
    lst.append(int(input()))
print(lst)
zeroCount = 0
while 0 in lst:
    zeroCount +=1
    lst.pop(lst.index(0))
for i in range(0, zeroCount):
    lst.insert(0, 0)
print(lst)