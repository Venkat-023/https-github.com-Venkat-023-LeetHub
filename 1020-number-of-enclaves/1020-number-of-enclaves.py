class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        r,c=len(grid),len(grid[0])
        def dfs(i,j):
            if i<0 or j<0 or i>=r or j>=c or grid[i][j]==0:
                return 
            grid[i][j]=0
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)
        for i in range(r):
            dfs(i,0)
            dfs(i,c-1)
        for i in range(c):
            dfs(0,i)
            dfs(r-1,i)
        res=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    res+=1
        return res
        