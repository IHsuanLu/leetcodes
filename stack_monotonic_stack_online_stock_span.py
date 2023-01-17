class StockSpanner:
    """
    [100, 1], [80, 1], [60, 1]
    [100, 1], [80, 1], [70, 2], [60, 1]
    [100, 1], [80, 1], [75, 3]
    """
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        pop_count = 1
        while self.stack and self.stack[-1][0] <= price:
            _, count = self.stack.pop()
            pop_count += count

        self.stack.append((price, pop_count))
        return pop_count