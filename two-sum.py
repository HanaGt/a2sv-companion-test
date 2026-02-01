1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        arr = []
4        for i in range(len(nums)):
5            for j in range(i + 1 , len(nums)):
6                if nums[i] + nums[j] == target:
7                    arr.append((i , j))
8
9        return arr[0]
10