class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = []

    def computeDifference(self):
        for i in range(len(a)):
            for j in range(i+1, len(a)):
                diff = abs(a[i] - a[j])
                self.maximumDifference.append(diff)
        self.maximumDifference = max(self.maximumDifference)


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
