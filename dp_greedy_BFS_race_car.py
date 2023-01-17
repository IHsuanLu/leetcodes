# FAV
from collections import deque

# BFS + Pruning the trees
class Solution:
    def racecar(self, target: int) -> int:
        """
        AAARA
        pos 0 -> 1 -> 3 -> 7 -> 7 -> 6
        speed 1 -> 2 -> 4 -> 8 -> -1 -> -2
        
        intuition: get shortest sequence of instructions
            -> BFS # (pos, speed, steps)
        """
        queue = deque([(0, 1, 0)])
        while queue:
            for _ in range(len(queue)):
                prev_pos, prev_speed, prev_steps = queue.popleft()

                if prev_pos == target:
                    return prev_steps

                # case 1 -> A
                queue.append((prev_pos + prev_speed, prev_speed * 2, prev_steps + 1))

                # case 2 -> R (TLE)
                # queue.append((prev_pos, -1 if prev_speed >= 0 else 1, prev_steps + 1))

                # enhancement can be made here
                # there are two reasons when we want to reverse the car, having `R`
                # case 2.1 -> R
                #   if the car passed the target and its speed is still positive
                if prev_pos + prev_speed > target and prev_speed > 0:
                    queue.append((prev_pos, -1, prev_steps + 1))

                # case 2.1 -> R
                #   if the car has not reached the target and its speed is negative
                if prev_pos + prev_speed < target and prev_speed < 0:
                    queue.append((prev_pos, 1, prev_steps + 1))

        return -1
        

# TLE
class Solution:
    def racecar(self, target: int) -> int:
        """
        AAARA
        pos 0 -> 1 -> 3 -> 7 -> 7 -> 6
        speed 1 -> 2 -> 4 -> 8 -> -1 -> -2
        
        intuition: get shortest sequence of instructions
            -> BFS # (pos, speed, steps)
        """
        queue = deque([(0, 1, 0)])
        while queue:
            for _ in range(len(queue)):
                prev_pos, prev_speed, prev_steps = queue.popleft()

                if prev_pos == target:
                    return prev_steps

                # case 1 -> A
                queue.append((prev_pos + prev_speed, prev_speed * 2, prev_steps + 1))

                # case 2 -> R
                queue.append((prev_pos, -1 if prev_speed >= 0 else 1, prev_steps + 1))

        return -1
        