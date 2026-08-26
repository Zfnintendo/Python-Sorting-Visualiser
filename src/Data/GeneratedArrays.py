import random

class ArrayGeneration:

    def Randomised(self, ArrLength: int):
        self.OriginalArray = [random.randint(1, ArrLength) for i in range(ArrLength)]


    def Ordered(self, ArrLength: int):
        self.OriginalArray = list(range(1, ArrLength+1))
        random.shuffle(self.OriginalArray)
