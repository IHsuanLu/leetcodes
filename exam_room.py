
# simulation
"""
seat O(nlogn)
leave O(nlogn)
"""
class ExamRoom:
    def __init__(self, n: int):
        self.size = n
        self.people = []

    def seat(self) -> int:
        self.size, self.people
        if not self.people:
            self.people.append(0)
            return 0

        max_val, max_idx = self.people[0], 0
        
        # middle cases
        for i in range(1, len(self.people)):
            if (self.people[i] - self.people[i - 1]) // 2 > max_val:
                max_val, max_idx = (self.people[i] - self.people[i - 1]) // 2, (self.people[i] + self.people[i - 1]) // 2

        if self.people[-1] != self.size - 1:
            if self.size - 1 - self.people[-1] > max_val:
                max_val, max_idx = self.size - 1 - self.people[-1], self.size - 1

        self.people.insert(self.people, max_idx)
        return max_idx

    def leave(self, p: int) -> None:
        self.people.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)