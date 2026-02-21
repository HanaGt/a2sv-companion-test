import sys

def solve():
    # Use fast I/O
    input = sys.stdin.read().split()
    if not input:
        return
    
    idx = 0
    t = int(input[idx])
    idx += 1
    
    results = []
    for _ in range(t):
        n = int(input[idx])
        p = input[idx+1 : idx+1+n]
        a = input[idx+1+n : idx+1+2*n]
        idx += 1 + 2*n
        
        # 1. Create the sequence S of consecutive unique elements in a
        s = []
        if n > 0:
            s.append(a[0])
            for i in range(1, n):
                if a[i] != a[i-1]:
                    s.append(a[i])
    
        p_ptr = 0
        s_ptr = 0
        while p_ptr < n and s_ptr < len(s):
            if p[p_ptr] == s[s_ptr]:
                s_ptr += 1
            p_ptr += 1
        
        if s_ptr == len(s):
            results.append("YES")
        else:
            results.append("NO")
            
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()