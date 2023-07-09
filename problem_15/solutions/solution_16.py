import sys
import math
from collections import defaultdict
from collections import deque
from itertools import combinations
from itertools import permutations
input = lambda : sys.stdin.readline().rstrip()
read = lambda : list(map(int, input().split()))
go = lambda : 1/0
def write(*args, sep="\n"):
  for i in args:
    sys.stdout.write("{}{}".format(i, sep))
INF = float('inf')
MOD = int(1e9 + 7)
YES = "YES"
NO = "NO"

for _ in range(int(input())):
  try:
    a, b, x, y = read()
    up = y * a
    down = (b - y - 1) * a
    left = x * b
    right = (a - x - 1) * b 

    print(max([up, down, left, right]))

  except ZeroDivisionError:
    continue

  except Exception as e:
    print(e)
    continue
