import sys
input=sys.stdin.readline
from collections import defaultdict

for _ in range(int(input())):
    n=int(input())
    x=4*n
    for i in range(n):
        print(x,end=" ")
        x-=2
    print()



