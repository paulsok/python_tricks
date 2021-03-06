# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4]
# Explanation: Your function should return length = 5, 
# with the first five elements of nums 
# being modified to 0, 1, 2, 3, and 4 respectively. 
# It doesn't matter what values are set beyond the 
# returned length.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)
