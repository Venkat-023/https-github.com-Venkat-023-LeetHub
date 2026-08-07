class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        res=0
        lmax=0
        rmax=0
        l,r=0,n-1
        while l<=r:
            if height[l]<lmax:
                res+=(lmax-height[l])
            else:
                lmax=height[l]
            if height[r]<rmax:
                res+=(rmax-height[r])
            else:
                rmax=height[r]
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return res