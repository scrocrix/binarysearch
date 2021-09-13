class Solution:
    def solve(self, deadlines, credits, durations):
        n = len(deadlines)
        mat = [(deadlines[i], credits[i], durations[i]) for i in range(n)]
        mat.sort()
        @lru_cache(None)
        def comp(i, current_time):
            if i == n:
                return 0

            ans = 0
            new_time = current_time + mat[i][2]

            # if we take the current task
            if new_time - 1 <= mat[i][0]:
                ans = max(ans, mat[i][1] + comp(i + 1, new_time))

            # if we do not take the current task
            ans = max(ans, comp(i + 1, current_time))
            return ans

        return comp(0, 0)
