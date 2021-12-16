import statistics
import math

class Stat:

    def __init__(self, nums_list):
        self.nums_list = nums_list

    def addNumber(self, x):
        self.nums_list.append(x)

    def mean(self):
        size_of_list = len(self.nums_list)
        sum = 0
        for number in self.nums_list:
            sum += number
        mean = sum / size_of_list
        return mean

    def median(self):
        median = statistics.median(self.nums_list)
        return median

    def stdDev(self):
        sum = 0
        for num in self.nums_list:
            deviation = num - self.mean()
            deviation *= deviation
            sum += deviation
        size_of_list = len(self.nums_list)
        result = sum / (size_of_list - 1)
        sd = math.sqrt(result)
        return sd

    def count(self):
        size_of_list = len(self.nums_list)
        return size_of_list

    def min(self):
        self.nums_list.sort()
        return self.nums_list[:1]

    def max(self):
        return max(self.nums_list)

    def __str__(self):
        for num in range(len(self.nums_list)):
            stats_str = "Here are your stats. Mean: " + str(self.mean()) + " Median: " + str(self.median()) \
                    + " List of numbers: " \
                    + str(self.nums_list[num]) + " Count of numbers: " + str(self.count()) \
                    + " Min value: " + str(min(self.nums_list)) + " Max value: " + str(max(self.nums_list))
        return stats_str

    def __add__(self, other):
        new_list = other + self.nums_list
        return new_list

    def __mul__(self, num):
        multiplied_array = [element * num for element in self.nums_list]
        return multiplied_array


def main():
    numList = [1, 2, 3, 4, 5]
    other = [1, 2, 3, 4, 5]
    stat = Stat(numList)
    print(str(stat.addNumber(2)))
    print("Mean: " + str(stat.mean()))
    print("Median: " + str(stat.median()))
    print("Standard Deviation: " + str(stat.stdDev()))
    print("Count: " + str(stat.count()))
    print("Min: " + str(stat.min()))
    print("Max: " + str(stat.max()))
    print("List of stats: " + str(stat.__str__()))
    print("Combine two lists: " + str(stat.__add__(other)))
    print("Multiply a list: " + str(stat.__mul__(2)))

main()






        

    
        
        
