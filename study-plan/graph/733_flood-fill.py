# https://leetcode.com/problems/flood-fill/

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        stack_loc = [(sr,sc)]
        oldColor = image[sr][sc]
        visited = {}
        m = len(image)
        n = len(image[0])
        while(len(stack_loc) > 0):
            (sr, sc) = stack_loc.pop()
            if (image[sr][sc] == oldColor and not(sr + sc*n in visited)):
                visited[sr + sc*n] = 1
                image[sr][sc] = newColor
                if (sr - 1 >= 0) and (image[sr-1][sc] == oldColor):
                    stack_loc.append((sr-1, sc))
                if (sc - 1 >= 0) and (image[sr][sc-1] == oldColor):
                    stack_loc.append((sr, sc-1))
                if (sr + 1 < m) and (image[sr+1][sc] == oldColor):
                    stack_loc.append((sr+1, sc))
                if (sc + 1 < n) and (image[sr][sc+1] == oldColor):
                    stack_loc.append((sr, sc+1))
        return image

s = Solution()
print(s.floodFill(image = [[0,0,0],[0,1,1]], sr = 1, sc = 1, newColor = 1))