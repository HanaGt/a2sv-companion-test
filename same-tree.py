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
17
18
19
20
21
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional
[TreeNode]) -> bool:
        def dfs(p , q):
            if not p and not q:
                return True
                
            if not p or not q:
                return False
            check_lefts = dfs(p.left , q.left)
            check_rights = dfs(p.right , q.right)
            return  p.val == q.val and check_lefts and 