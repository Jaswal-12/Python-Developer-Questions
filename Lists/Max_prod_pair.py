a = [1, 10, 2, 6, 5, 3]

mx = 0
pair = ()

for i in range(len(a)):
    for j in range(len(a)):
        if i == j:
            continue
        x = a[i] * a[j]
        if x > mx:
            mx = x
            pair = (a[i], a[j])

print(pair)
