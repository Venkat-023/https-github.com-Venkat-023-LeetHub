class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r,c=len(board),len(board[0])
        def dfs(i,j):
            if i<0 or j<0 or i>=r or j>=c or board[i][j]!='O':
                return
            board[i][j]='#'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        for i in range(r):
            dfs(i,0)
            dfs(i,c-1)
        for j in range(c):
            dfs(0,j)
            dfs(r-1,j)
        for i in range(r):
            for j in range(c):
                if board[i][j]=='#':
                    board[i][j]='O'
                else:
                    board[i][j]='X'
