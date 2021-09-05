class Solution:
    def solve(self, n):
        v = []
        for i in range(n):
            i = i + 1
            s = str(i)
            if i % 3 == 0 or "3" in s or "6" in s or "9" in s:
                v.append("clap")
                continue
            v.append(s)
        return v
