a = [1,2,3,2,3,2,5]
res = []

for i in a:
    if a.count(i) > 1:
        if i not in res:    # avoid repeating same duplicate
            res.append(i)

print(res)
