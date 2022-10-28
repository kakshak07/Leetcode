class Solution:
    def minWindow(self, s: str, t: str) -> str:
        Tc = Counter(t)
        Sc = Counter()

        best_i = -sys.maxsize
        best_j = sys.maxsize

        i = 0

        for j, char in enumerate(s):
            Sc[char] += 1

            while Sc & Tc == Tc:
                if j - i < best_j - best_i:
                    best_i, best_j = i, j

                Sc[s[i]] -= 1
                i += 1

        return s[best_i : best_j + 1] if best_j - best_i < len(s) else ""