a, b, c = map(int,input().split())
if b > a:
    a = b
if a > c:
    print(a)
else:
    print(c)