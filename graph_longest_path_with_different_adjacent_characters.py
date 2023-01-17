from ast import List
import collections


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        adjacents = collections.defaultdict(list)
        for i in range(len(parent)):
            if parent[i] != -1:
                adjacents[parent[i]].append(i)
        
        """
        max_so_far: the maximum length of path so far from the leaf to the current node
            -> we consider at most two children
        max_acc: the maximum accumulate number that we can pass to the parent
            -> we consider only the max-length child
        """
        def dfs(node):
            max_acc = max_so_far = 1
            
            child_accs = []
            for neighbor in adjacents[node]:
                child_acc, child_max_so_far, last_char = dfs(neighbor)
                max_so_far = max(max_so_far, child_max_so_far)

                # store the valid accumulated path returned from children
                if last_char != s[node]:
                    child_accs.append(child_acc)

            # max_acc -> we can only use the max-length child in the parent rounds
            if child_accs:
                max_acc = max(max_acc, max(child_accs) + 1)
        
            # max_so_far -> we can use at most two children to achieve the longest path
            curr_max_so_far = 1
            child_accs.sort(reverse=True)
            for i in range(min(2, len(child_accs))):
                curr_max_so_far += child_accs[i]

            return max_acc, max(max_so_far, curr_max_so_far), s[node]

        acc, max_so_far, _ = dfs(0)
        return max(acc, max_so_far)


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        adjacents = collections.defaultdict(list)
        for i in range(len(parent)):
            if parent[i] != -1:
                adjacents[parent[i]].append(i)
        
        def dfs(node):
            max_acc = max_so_far = 1
            
            # replace array with two variables
            max1 = max2 = 0
            for neighbor in adjacents[node]:
                child_acc, child_max_so_far, last_char = dfs(neighbor)
                max_so_far = max(max_so_far, child_max_so_far)

                if last_char != s[node]:
                    if not max1:
                        max1 = child_acc
                    elif not max2:
                        max2 = child_acc
                    elif child_acc > min(max1, max2):
                        if max1 > max2:
                            max2 = child_acc
                        else:
                            max1 = child_acc

            if max1 or max2:
                max_acc = max(max_acc, max(max1, max2) + 1)
        
            curr_max_so_far = 1
            for m in [max1, max2]:
                curr_max_so_far += m

            return max_acc, max(max_so_far, curr_max_so_far), s[node]

        acc, max_so_far, _ = dfs(0)
        return max(acc, max_so_far)