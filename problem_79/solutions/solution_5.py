import sys
input=lambda:sys.stdin.readline().rstrip()

def gcd(a, b):
  while b: a, b = b, a % b
  return a
def isPrimeMR(n):
  d = n - 1
  d = d // (d & -d)
  L = [2, 3, 61]
  for a in L:
    t = d
    y = pow(a, t, n)
    if y == 1: continue
    while y != n - 1:
      y = (y * y) % n
      if y == 1 or t == n - 1: return 0
      t <<= 1
  return 1
def findFactorRho(n):
  m = 1 << n.bit_length() // 8
  for c in range(1, 99):
    f = lambda x: (x * x + c) % n
    y, r, q, g = 2, 1, 1, 1
    while g == 1:
      x = y
      for i in range(r):
        y = f(y)
      k = 0
      while k < r and g == 1:
        ys = y
        for i in range(min(m, r - k)):
          y = f(y)
          q = q * abs(x - y) % n
        g = gcd(q, n)
        k += m
      r <<= 1
    if g == n:
      g = 1
      while g == 1:
        ys = f(ys)
        g = gcd(abs(x - ys), n)
    if g < n:
      if isPrimeMR(g): return g
      elif isPrimeMR(n // g): return n // g
      return findFactorRho(g)
def primeFactor(n):
  i = 2
  ret = {}
  rhoFlg = 0
  while i*i <= n:
    k = 0
    while n % i == 0:
      n //= i
      k += 1
    if k: ret[i] = k
    i += 1 + i % 2
    if i == 101 and n >= 2 ** 20:
      while n > 1:
        if isPrimeMR(n):
          ret[n], n = 1, 1
        else:
          rhoFlg = 1
          j = findFactorRho(n)
          k = 0
          while n % j == 0:
            n //= j
            k += 1
          ret[j] = k

  if n > 1: ret[n] = 1
  if rhoFlg: ret = {x: ret[x] for x in sorted(ret)}
  return ret

for _ in range(int(input())):
  n=int(input())
  ret=primeFactor(n)
  m=len(ret)
  s=1
  a=[]
  for i in ret:
    a.append(i)
    s*=ret[i]+1
  ans=[]
  for i in range(m):
    s//=ret[a[i]]+1
    for j in range(1,ret[a[i]]+1):
      for k in range(s):
        x=a[i]**j
        for l in range(i+1,m):
          k,t=divmod(k,ret[a[l]]+1)
          x*=a[l]**t
        ans.append(x)
  if gcd(ans[0],ans[-1])==1:
    del ans[ans.index(ans[0]*ans[-1])]
    ans.append(ans[0]*ans[-1])
  anss=0
  for i in range(len(ans)-1):
    if gcd(ans[i],ans[i+1])==1:anss+=1
  print(*ans)
  print(anss)
