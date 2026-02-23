def solve(l, r):
    if r - l == 1:
        return 0
    mid = (l + r) // 2
    mal = max(p[l:mid])
    mar = max(p[mid:r])
    ans = 0
    if mal > mar:
        ans += 1
        p[l:mid], p[mid:r] = p[mid:r], p[l:mid]
    return solve(l, mid) + solve(mid, r) + ans

for _ in range(t):
    m = int(input())
    p = list(map(int, input().split()))
    operations = solve(0, m)
    if p == sorted(p):
        res.append(operations)
    else:
        res.append(-1)

for r in res:
    print(r)