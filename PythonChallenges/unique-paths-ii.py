class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        result = [[0] * n for _ in range(m)]
        result[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1, m + n - 1): # i is the total index of x and y
            x = i if i < m else m - 1
            y = i - x
            while x > -1 and x < m and y > -1 and y < n:
                if obstacleGrid[x][y] == 0:
                    if x > 0:
                        result[x][y] += result[x - 1][y]
                    if y > 0:
                        result[x][y] += result[x][y - 1]
                x -= 1
                y += 1
        print(result)
        return result[m-1][n-1]
        