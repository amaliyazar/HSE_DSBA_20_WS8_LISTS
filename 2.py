a = list(map(int, input().split()))
b = list(map(int, input().split()))
r1, r2 = [], []
res = "YES"
for i in a:
    if i not in r1:
        r1.append(i)
for i in b:
    if i not in r2:
        r2.append(i)
r1, r2 = sorted(r1), sorted(r2)
if r1 == r2:
    print("YES")
else:
    print("NO")
