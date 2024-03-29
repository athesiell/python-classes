class Bird:
    def __init__(self, name):
        self.name = name

    def walk(self):
        return f"{self.name} bird can walk"
    
    def fly(self):
        return f"{self.name} bird can fly"
    
class FlyingBird(Bird):
    def __init__(self, name, ration="grains"):
        super().__init__(name)
        self.ration = ration

    def walk(self):
        return super().walk()
    
    def fly(self):
        return super().fly()
    
    def eat(self):
        return f"It eats mostly {self.ration}"
    
    def __str__(self) -> str:
        return f"{self.name} bird can walk and fly"
    
class NonFlyingBird(Bird):
    def __init__(self, name, ration="fish"):
        super().__init__(name)
        self.ration = ration

    def swim(self):
        return f"{self.name} bird can swim"
    
    def eat(self):
        return f"It eats mostly {self.ration}"
    
    def fly(self):
        raise AttributeError(f"'{self.name}' object has no attribute 'fly")
    
class SuperBird(NonFlyingBird, FlyingBird):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        return f"It eats mostly {self.ration}"
    
    def fly(self):
        return f"{self.name} bird can fly"
    
    def __str__(self) -> str:
        return f"{self.name} bird can walk, swim and fly"
    
b = Bird("Any")
print(b.walk())

p = NonFlyingBird("Penguin", "fish")
print(p.swim())
try:
    print(p.fly())
except AttributeError as e:
    print(e)
print(p.eat())

c = FlyingBird("Canary")
print(c.walk())
print(c.fly())
print(c.eat())

s = SuperBird("Gull")
print(s.walk())
print(s.swim())
print(s.fly())
print(s.eat())
print(str(s))
print(str(c))