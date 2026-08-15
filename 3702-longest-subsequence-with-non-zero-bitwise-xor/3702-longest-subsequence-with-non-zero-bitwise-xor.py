class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total=0
        non_zero=False
        for x in nums:
            if x!=0:
                non_zero=True
            total^=x
        if total!=0:
            return len(nums)
        if non_zero:
            return len(nums)-1
        return 0