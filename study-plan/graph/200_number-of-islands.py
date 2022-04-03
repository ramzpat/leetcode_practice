# https://leetcode.com/problems/number-of-islands/

class Solution(object):
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def fill_visited(grid, visited, i, j, n, m):
            # fill visited
            stack_loc = [(i,j)]
            while(len(stack_loc) > 0):
                (i,j) = stack_loc.pop()
                if (i >= 0 and j >= 0 and i < n and j < m and not((i + j * n) in visited) and grid[i][j] == "1"):
                    visited[ i + j * n] = 1
                    stack_loc += [(i+x, j+y) for (x,y) in [(-1,0), (0, -1), (1, 0), (0, 1)] if (i+x >= 0 and j+y >= 0 and i+x < n and j+y < m and grid[i+x][j+y] == "1")]
                    
            return visited
                

        visited = {}
        count = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(0, n):
            for j in range(0, m):
                if not (i + j * n in visited) and grid[i][j] == "1":
                    fill_visited(grid, visited, i, j, n, m)
                    count = count + 1
        
        return count 

s = Solution()
print(s.numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
