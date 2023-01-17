# FAV

from ast import List

# backtracking and record the sum as traversing
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        """
        use backtracking to brute force the problem
            -> enumerate all the possibilities and store the result to the output array
        
        question:
            - `*` should be calculated first, maybe need to create an helper function
            - remove leading zeros if any
        """
        operators = ["+", "-", "*"]
        res = []
        def backtrack(idx, path, acc, prev):
            if idx == len(num):
                if acc == target:
                    res.append(path)
                return
            
            for i in range(idx, len(num)):
                operand = num[idx: i + 1]

                if operand and operand[0] == "0" and len(operand) > 1:
                    continue
        
                n_operand = int(operand)
                if not path: # first operand
                    backtrack(i + 1, path + operand, n_operand, n_operand)
                else:
                    for operator in operators:
                        if operator == "+":
                            backtrack(i + 1, path + operator + operand, acc + n_operand, acc)
                        elif operator == "-":
                            backtrack(i + 1, path + operator + operand, acc - n_operand, acc * -1)
                        elif operator == "*":
                            print(path + operator + operand, (acc - prev), (n_operand * prev))
                            backtrack(i + 1, path + operator + operand, (acc - prev) + (n_operand * prev), n_operand * prev)

        backtrack(0, "", 0, 0)
        return res



# backtracking with eval function -> TLE, pass 20/23
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        """
        use backtracking to brute force the problem
            -> enumerate all the possibilities and store the result to the output array
        
        question:
            - `*` should be calculated first, maybe need to create an helper function
            - remove leading zeros if any
        """
        operators = ["+", "-", "*"]
        res = []
        def backtrack(idx, path):
            if idx == len(num):
                if eval(path) == target:
                    res.append(path)
                return
            
            for i in range(idx, len(num)):
                operand = num[idx: i + 1]
                if operand and operand[0] == "0" and len(operand) > 1:
                    continue

                if i != len(num) - 1:
                    for operator in operators:
                        backtrack(i + 1, path + operand + operator)
                else:
                    backtrack(i + 1, path + operand)

        backtrack(0, "")
        return res


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        """
        use backtracking to brute force the problem
            -> enumerate all the possibilities and store the result to the output array
        
        question:
            - `*` should be calculated first, maybe need to create an helper function
            - remove leading zeros if any
        """
        operators = ["+", "-", "*"]
        res = []
        def backtrack(idx, path, sum_val, last_operation):
            if idx == len(num) - 1:
                res.append(path)
                return

            for i in range(idx, len(num)):
                operand = num[idx: i + 1]
                if i == 0 and sum_val == 0:
                    sum_val = int(operand)

                if last_operation != [None, None]:
                    if last_operation[1] == "+":
                        sum_val += int(operand)
                    elif last_operation[1] == "-":
                        sum_val -= int(operand)
                    elif last_operation[1] == "*":
                        sum_val *= int(operand)

                if i != len(num) - 1:
                    for operator in operators:
                        backtrack(i + 1, path + operand + operator, sum_val, [int(operand), operator])
                else:
                    backtrack(i + 1, path + operand, sum_val, [int(operand), None])

        backtrack(0, "", 0, [None, None])
        print(res)
        return []
