import sys
INF = 10**20
MOD = 10**9 + 7
I = lambda:list(map(int,input().split()))
from math import gcd
from math import ceil
from collections import defaultdict as dd, Counter
from bisect import bisect_left as bl, bisect_right as br


"""
Facts and Data representation
Constructive? Top bottom up down
"""
def check(s):
  t = 'abacaba'
  ans = 0
  for i in range(len(s)):
    if s[i: i + 7] == t:
      ans += 1
  return ans

def solve():
  n, = I()
  s = input()
  t = 'abacaba'
  cnt = check(s)
  if cnt > 1:
    print('No')
    return
  elif cnt == 1:
    s = list(s)
    for i in range(n):
      if s[i] == '?':
        s[i] = 'z'
    print('Yes')
    print(''.join(s))
  else:
    s = list(s)
    ok = s[::]
    for i in range(n - 6):
      ok = s[::]
      for j in range(7):
        if s[i + j] == t[j]:
          continue
        elif s[i + j] == '?':
          ok[i + j] = t[j]
        else:
          break
      else:
        for i in range(n):
          if ok[i] == '?':
            ok[i] = 'z'
        ok = ''.join(ok)
        if check(ok) != 1:
          continue
        print('Yes')
        print(ok)
        return
    print('No')

t, = I()
while t:
  t -= 1
  solve()
