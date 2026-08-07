class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        def dfs(i,j,t,seen):
            if i<0 or j<0 or i>=n or j>=n or (i,j) in seen or grid[i][j]>t:
                return False
            if i==n-1 and j==n-1:
                return True
            seen.add((i,j))
            return dfs(i+1,j,t,seen) or dfs(i,j+1,t,seen) or dfs(i-1,j,t,seen) or dfs(i,j-1,t,seen)
        left=0
        right=n**2
        while left<right:
            mid=(left+right)//2
            seen=set()
            if dfs(0,0,mid,seen):
                right=mid
            else:
                left=mid+1
        return left
