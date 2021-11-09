class car:
    def __init__(self,name,age):
        self.names = name
        self.ages = age


while True:
    names = input('your name')
    ages = input('your age')
    car1 = car(names,ages)
    print(f'your name is {car1.names}')
