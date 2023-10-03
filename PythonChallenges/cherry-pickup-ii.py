# https://leetcode.com/problems/cherry-pickup-ii

class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = len(grid)
        c = len(grid[0])
        state = [[-1] * c for i in range(c)]
        state[0][c - 1] = grid[0][0] + grid[0][c - 1]
        for row in range(1, r):
            new_state = [[-1] * c for i in range(c)]
            for bot1 in range(c):
                for bot2 in range(bot1, c):
                    if state[bot1][bot2] == -1:
                        continue
                    for dbot1 in range(-1, 2):
                        for dbot2 in range(-1, 2):
                            new_bot1 = bot1 + dbot1
                            new_bot2 = bot2 + dbot2
                            if new_bot1 >= 0 and new_bot2 >= 0 and new_bot1 < c and new_bot2 < c:
                                if new_bot1 == new_bot2:
                                    new_state[new_bot1][new_bot2] = max(state[bot1][bot2] + grid[row][new_bot1], new_state[new_bot1][new_bot2])
                                else:
                                    new_state[new_bot1][new_bot2] = max(state[bot1][bot2] + grid[row][new_bot1] + grid[row][new_bot2], new_state[new_bot1][new_bot2])
            state = new_state
        return max([max(arr) for arr in state])






                    
        