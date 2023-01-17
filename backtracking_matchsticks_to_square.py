from ast import List

# enhanced brute force w/o memoization -> O(4^n), based on edges
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False
        if sum(matchsticks) % 4:
            return False

        matchsticks.sort(reverse=True)

        n = sum(matchsticks) // 4
        sides = [0] * 4
        def backtrack(idx):
            if idx == len(matchsticks):
                return True
            for edge in range(4):
                if sides[edge] + matchsticks[idx] <= n:
                    sides[edge] += matchsticks[idx]
                    if backtrack(idx + 1):
                        return True
                    sides[edge] -= matchsticks[idx]
            return False

        return backtrack(0)


# brute force w/o memoization -> O(4^n)
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # let's start from the brute force
        # we need to use backtracking to try out every possibility
        # def bactrack(idx, curr, remaining_edge)
        # additional array to keep track of the used `matchstick`

        if len(matchsticks) < 4:
            return False
        if sum(matchsticks) % 4:
            return False
        
        n = sum(matchsticks) // 4
        used = [False] * len(matchsticks)

        def backtrack(idx, curr, remaining_edge):
            if remaining_edge == 0:
                return True
            
            if curr == n:
                return backtrack(0, 0, remaining_edge - 1) 
            
            for i in range(idx, len(matchsticks)):
                if used[i]:
                    continue
                
                # we made a decision of selecting `i` matchstick
                used[i] = True

                if curr + matchsticks[i] <= n:
                    if backtrack(i + 1, curr + matchsticks[i], remaining_edge):
                        return True

                # we reverse the decision of selecting `i` matchstick
                used[i] = False
            
            return False
        
        return backtrack(0, 0, 4)