class Incrementer(int):
    def __add__(self,other):
        return super().__add__(other+1)
i=Incrementer(5)
result=i+3
print(result)