from operator import contains


print("Введите ребра графа")
U = input().split(" ")
X = []
for i in U:
    if i[1] not in X:
        X.append(i[1])
    if i[3] not in X:
        X.append(i[3])
X = sorted(X)
print(X)
