x = int(input("Enter a number: "))

rev = 0

while x != 0:
    l = x % 10
    rev = rev * 10 + l
    x = x // 10

print(rev)
