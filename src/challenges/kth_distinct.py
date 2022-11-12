class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        d1 = self.get_chars(words1)
        d2 = self.get_chars(words2)
        d1len = False
        d2len = False
        if len(d1.values()) >= len(d2.values()):
            d1len = True
        else:
            d2len = True
        totalcount = 0
        if d1len:
            for k, v in d1.items():
                if k in d2:
                    if v == 1 and v == d2[k]:
                        totalcount += 1
            return totalcount
        else:
            for k, v in d2.items():
                if k in d1:
                    if v == 1 and v == d1[k]:
                        totalcount += 1
            return totalcount

    def get_chars(self, arr):
        d1 = {}
        for c in arr:
            d1[c] = d1.get(c, 0) + 1
        return d1
