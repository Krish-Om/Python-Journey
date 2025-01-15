class Sample:
    varia = 1
    
    def __init__(self):
        self.var = 2

    def visible(self):
        pass

    def __hidden(self):
        pass


obj = Sample()

print(Sample.__dict__)