class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        r,c=len(land),len(land[0])
        seen=set()
        top_left=(r,c)
        bottom_right=(0,0)
        def dfs(i,j):
            nonlocal top_left,bottom_right
            if i<0 or j<0 or i>=r or j>=c or land[i][j]==0 or (i,j) in seen:
                return 
            top_left=min(top_left,(i,j))
            bottom_right=max(bottom_right,(i,j))
            seen.add((i,j))
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        res=[]
        for i in range(r):
            for j in range(c):
                if land[i][j]==1 and (i,j) not in seen:
                    top_left=(r,c)
                    bottom_right=(-1,-1)
                    dfs(i,j)
                    if top_left!=(r,c) and bottom_right!=(-1,-1):
                        res.append(top_left+bottom_right)
        return res