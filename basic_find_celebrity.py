class Solution:
    def findCelebrity(self, n: int) -> int:
        # logic:
        #   - if i knows celeb, celeb remains
        #   - if celeb knows i, celeb invalidated and i is new candidate celeb
        #       - in this case:
        #           - i is only person up to this point that may NOT know anyone else
        #   - last pass checks "surviving" candidate
        # 
        # could use a cached version `self.cached_knows` to reduce "API" calls 
        celeb = 0

        # [[1,1,0],
        #  [0,1,0],
        #  [1,1,1]]
        
        # if celeb doesn't know i, then i can't be celebrity, i moves on;
        # if celeb knows i, then celeb can't be celebrity, celeb = i become the next candidate
        for i in range(1, n):
            if knows(celeb, i):
                celeb = i

        for i in range(n):
            if i != celeb:
                # if i does not know candidate, or candidate knows i, return -1;
                if not knows(i, celeb) or knows(celeb, i):
                    return -1
        
        return celeb
        