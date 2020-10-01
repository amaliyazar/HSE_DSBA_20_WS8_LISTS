
a = list(map(str, input().split()))
x = int(input())
y = len(a)//x+1
#if y % x != 0:
    # y += 1
for i in range(len(a)//x+1):
    print(*a[i:len(a):y])
