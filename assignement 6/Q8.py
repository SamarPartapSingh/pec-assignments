class SumThreeZero:
    def __init__(self, numbers):
        self.numbers = numbers

    def three_sum_zero(self):
        result = []
        for i in range(len(self.numbers)-2):
            for j in range(i+1, len(self.numbers)-1):
                for k in range(j+1, len(self.numbers)):
                    if self.numbers[i] + self.numbers[j] + self.numbers[k] == 0:
                        result.append([self.numbers[i], self.numbers[j], self.numbers[k]])
        return result

numbers = [-25, -10, -7, -3, 2, 4, 8, 10]
test = SumThreeZero(numbers)
print(test.three_sum_zero())
