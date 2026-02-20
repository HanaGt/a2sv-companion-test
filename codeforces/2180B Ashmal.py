import sys

def solve():
    n = int(sys.stdin.readline())
    if n == 2:
        print(2)
    elif n == 3:
        print(3)
    else:
        print(n % 2)

t = int(sys.stdin.readline())
for _ in range(t):
    solve()