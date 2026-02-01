1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
class Solution:
    def reverseString(self, s: List[str] ) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(left, right):
            if left >= right:
                return 
            s[left] , s[right] = s[right] , s[left]
            reverse(left+1 , right - 1)

        reverse(0 , len(s)-1)