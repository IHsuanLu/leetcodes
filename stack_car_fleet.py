from ast import List


# instead of simulating condition of every round, we can simple determine if there will be a car fleet by comparing the arrival time
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tuples = []
        for i in range(len(position)):
            tuples.append([position[i], speed[i]])

        tuples.sort(reverse=True)
        
        # monotonic increasing stack
        stack = []
        for pos, spe in tuples:
            stack.append((target - pos) / spe) # arrive time

            # pop the one behind if it happens to arrive sooner than or at the same time as the car in the front 
            if len(stack) > 1 and stack[-1] <= stack[-2]: 
                stack.pop()
        
        return len(stack)


# wrong solution -> only runs one round
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tuples = []
        for i in range(len(position)):
            tuples.append([position[i], speed[i]])
        
        tuples.sort(reverse=True)
        
        # monotonic decreasing stack
        stack = []
        for i in range(len(tuples)):
            new_pos = tuples[i][0] + tuples[i][1]

            while stack and stack[-1][0] < new_pos:
                stack.pop()

            if stack and stack[-1][0] == new_pos:
                _, last_speed = stack.pop()
                stack.append([new_pos, min(last_speed, tuples[i][1])])
            else:
                stack.append([new_pos, tuples[i][1]])


        return len(stack)