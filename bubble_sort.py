# the original array
n = [2,3,5,4]


# This sorts the array in ASCENDING ORDER
# looping through the array
for i in range(len(n)-1, 0, -1):
    for j in range(i):
        # to check wether the current value is
        # bigger than the next value
        if n[j] > n[j + 1]:
            # swaping the variable
            temp = n[j]
            n[j] = n[j + 1]
            n[j + 1] = temp

# showing the new array
print(n)


# This sorts the array in DESENDING ORDER
# looping through the array
for i in range(len(n)-1, 0, -1):
    for j in range(i):
        # to check wether the current value is
        # smaller than the next value
        if n[j] < n[j + 1]:
            # swaping the variable
            temp = n[j]
            n[j] = n[j + 1]
            n[j + 1] = temp

# showing the new array
print(n)
