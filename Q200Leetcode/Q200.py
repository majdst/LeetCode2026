class Solution:
    def numIslands(self, grid:list)->int:
        def helper(z, xDir, yDir, rw, col):
            if xDir < 0 or yDir < 0 or xDir >= (rw) or yDir >= (col) or z[xDir][yDir] == "0":
                return

            z[xDir][yDir] = "0"
            helper(z, xDir + 1, yDir, rw, col)
            helper(z, xDir - 1, yDir, rw, col)
            helper(z, xDir, yDir - 1, rw, col)
            helper(z, xDir, yDir + 1, rw, col)

        row = len(grid)
        colmn = len(grid[0])
        count = 0
        for r in range(row):
            for c in range(colmn):
                if grid[r][c] == "1":
                    count +=1

                    helper(grid, r, c, row, colmn)
        
        return count
    
x = Solution()
y = x.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]])
print(y)