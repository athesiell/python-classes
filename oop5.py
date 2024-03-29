from typing import List

class Counter:
    def __init__(self, values: List[int]):
        self.values = values

    def __add__(self, b):
        if isinstance(b, str):
            return [f"{value} {b}" for value in self.values]
        else:
            raise TypeError("Error!")

c = Counter([1, 2, 3])
msg = c + "missisipi"
print(msg)