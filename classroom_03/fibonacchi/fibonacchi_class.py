class Fibonacci:
    def __init__(self):
        self.memoization = {}

    def calculate(self, n):
        if n in self.memoization:
            return self.memoization[n]
        if n <= 1:
            return n
        else:
            result = self.calculate(n-1) + self.calculate(n-2)
            self.memoization[n] = result
            return result
