import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
  n = int(input())
  a = list(map(int,input().split()))
  a.sort()
  ans = 0
  sepa = -1
  for i in range(n):
    if i-sepa >= a[i]:
      sepa = i
      ans += 1
  print(ans)
