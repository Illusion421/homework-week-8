import math

class MatchBox:

    def __init__(self, dim1, dim2, dim3):

        self.dimesions = sorted([dim1, dim2, dim3])

        self.maxLenght = math.sqrt(math.pow(self.dimesions[0], 2) + math.pow(self.dimesions[1], 2))

    def doesItFit(self, matchLen):

        if matchLen > self.maxLenght:
            print("NO!")
        else:
            print("YES!!")

x = MatchBox(5, 3, 4)

for i in range(10):
    print(i, end = " ")
    x.doesItFit(i)
