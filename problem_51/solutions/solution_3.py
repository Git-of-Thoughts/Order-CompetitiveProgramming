q = int(input())

while q > 0:
    n, k, d1, d2 = list(map(int, input().split()))
    if d1 > d2:
        d1, d2 = d2, d1
    if k - 2 * d1 - d2 >= 0 and (k - 2 * d1 - d2) % 3 == 0 and \
            (n - k) - d1 - 2 * d2 >= 0 and ((n - k) - d1 - 2 * d2) % 3 == 0:
        print('yes')
    elif k - 2 * d2 - d1 >= 0 and (k - 2 * d2 - d1) % 3 == 0 and \
            (n - k) - d2 - 2 * d1 >= 0 and ((n - k) - d2 - 2 * d1) % 3 == 0:
        print('yes')
    elif k - 2 * d2 + d1 >= 0 and (k - 2 * d2 + d1) % 3 == 0 and \
            (n - k) - d2 - d1 >= 0 and ((n - k) - d2 - d1) % 3 == 0:
        print('yes')
    elif k - d1 - d2 >= 0 and (k - d1 - d2) % 3 == 0 and \
            (n - k) - 2 * d2 + d1 >= 0 and ((n - k) - 2 * d2 + d1) % 3 == 0:
        print('yes')
    else:
        print('no')
    q -= 1

