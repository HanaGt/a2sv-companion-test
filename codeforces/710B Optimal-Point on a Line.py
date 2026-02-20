import sys

def solve():
    # Reading input efficiently
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    # Convert the rest of the strings to integers and sort them
    x = sorted(map(int, input_data[1:]))
    
    # The leftmost median is always at index (n-1) // 2
    print(x[(n - 1) // 2])

if __name__ == "__main__":
    solve()