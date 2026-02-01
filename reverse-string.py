1class Solution:
2    def reverseString(self, s: List[str] ) -> None:
3        """
4        Do not return anything, modify s in-place instead.
5        """
6
7        def reverse(left, right):
8            if left >= right:
9                return 
10            s[left] , s[right] = s[right] , s[left]
11            reverse(left+1 , right - 1)
12            
13        reverse(0 , len(s)-1)
14        
15
16