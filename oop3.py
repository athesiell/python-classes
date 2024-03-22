class Counter:
    def __init__(self,start=0, stop=None):
        self.start = start
        self.stop = stop

    def get(self):
        return self.start
    
    def increment(self):
        if self.stop is None or self.start < self.stop:
            self.start += 1
            if self.stop is not None and self.start == self.stop:
                print('Maximum value is reached.')


c = Counter(start=42, stop=43)
c.increment()
print(c.get())