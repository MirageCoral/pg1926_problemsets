lst = []
n = int(input("Element Sayısı: "))
for j in range(0, n):
    lst.append(int(input()))
maxEl = max(lst)
while maxEl % 2 == 0:
    lst.pop(lst.index(maxEl))
    maxEl = max(lst)
print(maxEl)