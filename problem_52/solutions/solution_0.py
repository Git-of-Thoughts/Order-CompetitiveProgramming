n=int(input())
a=sorted(int(input()) for _ in range(n))
print(sum(a[i]*a[-i-1] for i in range(n))%10007)
