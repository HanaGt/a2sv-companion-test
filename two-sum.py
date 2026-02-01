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
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for i in range(len(nums)):
            for j in range(i + 1 , len(nums)):
                if nums[i] + nums[j] == target:
                    arr.append((i , j))
        return arr[0]