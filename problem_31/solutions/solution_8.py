import sys
import heapq as hq

readline = sys.stdin.readline

ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: list(map(int, readline().split()))
nl = lambda: list(map(int, readline().split()))

# eps = 10**-7

def solve():
    s = ns()
    d = dict()
    cnt = 0
    g = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    cur = (0, 0)
    d[cur] = ''
    for x in s:
        for i in range(4):
            if x == 'NEWS'[i]:
                nx = (cur[0] + g[i][0], cur[1] + g[i][1])
                if nx in d and x in d[cur]:
                    cnt += 1
                else:
                    cnt += 5
                    if nx not in d:
                        d[nx] = ''
                    d[nx] += 'NEWS'[3-i]
                    d[cur] += x
                cur = nx
                break
    print(cnt)


# solve()

T = ni()
for _ in range(T):
    solve()

