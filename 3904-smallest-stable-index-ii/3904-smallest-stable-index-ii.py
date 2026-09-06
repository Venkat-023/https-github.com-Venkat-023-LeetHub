class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        min_num=float('inf')
        max_num=float('-inf')
        small=[min_num]*n
        large=[max_num]*n
        for i in range(n):
            max_num=max(max_num,nums[i])
            large[i]=max_num
        for i in range(n-1,-1,-1):
            min_num=min(min_num,nums[i])
            small[i]=min_num
        for i in range(n):
            cur=large[i]-small[i]
            if cur<=k:
                return i
        return -1
