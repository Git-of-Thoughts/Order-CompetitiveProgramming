#list(map(int,input().split()))
t=int(input())
for _ in range(t):
    n=int(input())
    aa=list(map(int,input().split()))
    bb=list(map(int,input().split()))
    aa.sort()
    bb.sort()
    print(*aa)
    print(*bb)

