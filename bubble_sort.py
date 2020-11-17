n = [2,3,5,4]

for i in range(len(n)-1, 0, -1):
    for j in range(i):
        if n[j] > n[j + 1]:
            temp = n[j]
            n[j] = n[j + 1]
            n[j + 1] = temp

print(n)
