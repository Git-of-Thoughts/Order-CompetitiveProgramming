def solve():
    n, k1, k2 = list(map(int, input().split()))
    m1 = max(list(map(int, input().split())))
    m2 = max(list(map(int, input().split())))
    if m1 > m2:
        print('YES')
    else:
        print('NO')


def main():
    t = int(input())
    # t = 1
    for _ in range(t):
        solve()


main()
