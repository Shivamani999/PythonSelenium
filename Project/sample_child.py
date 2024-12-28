from Project.sample import Calculator


class sample_child(Calculator):
    num2 = 200

    # def __init__(self, a, b):
    #     self.a = a
    #     self.b = b
    #     Calculator.__init__(self, self.a, self.b)

    def getTotalData(self):
        return self.num2 + self.num + self.sum()


# obj = sample_child()
obj = sample_child(4, 59)
print(obj.getTotalData())
