from ast import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hset = set()
        
        for email in emails:
            splitedEmails = email.split("@")
            local, domain = splitedEmails[0], splitedEmails[1]
            dotFreeLocal = local.replace(".", "")
            for i in range(len(dotFreeLocal)):
                if dotFreeLocal[i] == "+":
                    dotFreeLocal = dotFreeLocal[:i]
                    break
                    
            hset.add(dotFreeLocal + "@" + domain)
        
        return len(hset)