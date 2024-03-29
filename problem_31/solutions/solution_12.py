import sys

def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
INF = 10 ** 18
MOD = 10 ** 9 + 7

for _ in range(INT()):
    S = input()

    se = set()
    h = w = 0
    ans = 0
    for s in S:
        prev = (h, w)
        if s == 'S':
            h += 1
        elif s == 'N':
            h -= 1
        elif s == 'W':
            w -= 1
        else:
            w += 1
        cur = (h, w)
        key = (min(prev, cur), max(prev, cur))
        if key in se:
            ans += 1
        else:
            ans += 5
            se.add(key)
    print(ans)

