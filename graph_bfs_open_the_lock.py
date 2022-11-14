from ast import List
from collections import deque


class Solution:
    def openLock(self, trapped_combos: List[str], target_combo: str) -> int:
        trapped_combo_set = set(trapped_combos)
        visited = set()
        queue = deque([('0000', 0)])

        while len(queue) > 0:
            n = len(queue)
            for _ in range(n):
                (target, steps) = queue.popleft()
                if target == target_combo:
                    return steps
                if target in trapped_combo_set:
                    continue
                for i in range(4):
                    digit = int(target[i])
                    for move in [-1, 1]:
                        new_digit = (digit + move) % 10
                        new_string = target[:i] + str(new_digit) + target[i+1:]

                        if new_string not in visited:
                            visited.add(new_string)
                            queue.append((new_string, steps+1))
        return -1