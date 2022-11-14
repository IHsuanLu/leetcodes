# Top down
class Solution:
    def numTrees(self, n: int) -> int:
        def dfs(min, max, memo):
            if min >= max:
                return 1
            
            if (min, max) in memo:
                return memo[(min, max)]
            
            count = 0
            for i in range(min, max + 1): # from min to max, the nodes take turn being a root
                left_count = dfs(min, i - 1, memo)
                right_count = dfs(i + 1, max, memo)
                
                count += left_count * right_count
                
            memo[(min, max)] = count
            
            return count
        
        return dfs(1,n,{})

# Bottom up (dp)
# numTree[4] = numTree[0] + numTree[3]
#             + numTree[1] + numTree[2]
#             + numTree[2] + numTree[1]
#             + numTree[3] + numTree[0]
class Solution:
    def numTrees(self, n: int) -> int:
        numTree = [0] * (n + 1) # numOfTree -> count of unique trees
        numTree[0] = numTree[1] = 1

        # numTree[0] = numTree[1] = 1
        for numOfNodes in range(2, n + 1): # starting from two, build up the result list
            total = 0
            # under `numOfNodes` condition, every node takes turn being a root
            for root in range(1, numOfNodes + 1):
                left = root - 1
                right = numOfNodes - root
                total += numTree[left] * numTree[right]

            numTree[numOfNodes] = total 

        return numTree[n]