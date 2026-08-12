class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        hashmap=defaultdict(int)
        max_len=0
        l=0
        for i,num in enumerate(nums):
            hashmap[num]+=1
            while hashmap[num]>k:
                hashmap[nums[l]]-=1
                l+=1
            max_len=max(max_len,i-l+1)
        return max_len