# A plus B
# Tissan Kugathas
# May 27 2019

N = int(input())

if 1 <= N <= 100000:
    for n in range(N):
        a, b = map(int, input().split())
        print(a + b)
