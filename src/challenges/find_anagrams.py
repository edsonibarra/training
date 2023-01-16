"""Not working yet, time limit exceded error"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        idx = 0
        count = []
        while idx <= len(s) - len(p):
            print(idx)
            sbstr = s[idx: idx + len(p)]
            print(sbstr)
            sorted_sbstr = sorted(sbstr)
            if sorted(p) == sorted_sbstr:
                # idx += len(p)
                count.append(idx)
            idx += 1
        return count
        