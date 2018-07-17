import random
colour = ["red", "green", "blue", "yellow"]
make = ["ferrari", "tesla", "bmw", "citroen"]

class foo(object):
    def __init__(self, n):
        self.n = n
        self.num = 0
	
    def __iter__(self):
        return self

    def __next__(self):
        if self.num < self.n:
            self.num += 1
            return random.choice(colour), random.choice(make)
        else:
            raise StopIteration()


for c, m in foo(10):
    print("I have a %s %s" %(c, m))