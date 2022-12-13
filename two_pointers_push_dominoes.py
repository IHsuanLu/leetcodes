class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        l = r = 0
        while r < len(dominoes):
            if dominoes[r] == ".":
                r += 1
                continue
            
            if dominoes[r] == "L":
                i, j = l, r
                if dominoes[i] == "." or dominoes[i] == "L":
                    while i <= j:
                        dominoes[j] = "L"
                        j -= 1
                # dominoes[i] == "R"
                else:
                    while i < j:
                        dominoes[j] = "L"
                        dominoes[i] = "R"
                        i += 1
                        j -= 1
                l = r
            # dominoes[r] == "R"
            else: 
                if dominoes[l] == "R":
                    while l < r:
                        dominoes[l] = "R"
                        l += 1
                # dominoes[l] == "." or dominoes[l] == "L"        
                else: 
                    l = r

            r += 1

        # if there are trailing "." and `l` pointer is pushed to the right
        if dominoes[l] == "R":
            while l < r:
                dominoes[l] = "R"
                l += 1

        return "".join(dominoes)