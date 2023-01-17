# simulation
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        currX, currY = 0, 0
        direction = 0
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        attempt = 4
        while attempt:
            for ins in instructions:
                if ins == "L":
                    direction -= 1
                elif ins == "R":
                    direction += 1
                else:
                    direction %= 4
                    currX += directions[direction][0]
                    currY += directions[direction][1]
            
            if currX == 0 and currY == 0:
                return True

            attempt -= 1
        
        return False


# not working => cannot pass the test case "GLGLGGLGL"
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # L, R -> (number of degree * 4) % 360 == 0 -> cycle
        degree = 0
        for ins in instructions:
            if ins == "L":
                degree -= 90
            elif ins == "R":
                degree += 90

        degree = abs(degree)
        return degree != 0 and (degree * 4) % 360 == 0