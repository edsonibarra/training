class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        common_a = []
        common_b = []
        for i in range(1,a+1):
            if a % i == 0:
                common_a.append(i)
        for j in range(1,b+1):
            if b%j==0:
                common_b.append(j)
        print(common_a)
        print(common_b)

        ga = True if len(common_a) >= len(common_b) else False
        gb = True if len(common_b) > len(common_a) else False
        ans = []
        if ga:
            for n in common_a:
                if n in common_b:
                    ans.append(n)
        elif gb:
            for n in common_b:
                if n in common_a:
                    ans.append(n)
        return len(ans)
