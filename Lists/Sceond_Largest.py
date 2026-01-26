l = [9, 2, 3, 4, 5, 1, 6]

fm = -1
sm = -1

for i in l:
    if i > fm:
        sm = fm
        fm = i
    elif i > sm and i != fm:
        sm = i

print("Second max:", sm)
