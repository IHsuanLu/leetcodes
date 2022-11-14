class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        # key is to split the path using "/"
        for portion in path.split("/"):
            if portion == "..":
                if stack:
                    stack.pop()
            elif not portion or portion == ".":
                continue
            else:
                stack.append(portion)
        
        return "/" + "/".join(stack)