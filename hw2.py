def average(*args):
    length = len(args)
    sum = add(*args)
    avg = sum / length  
    return avg
def add(*args):
    sum = 0
    for items in args:
        sum = sum + items
    return sum 

mean = average(54,54,12,12,21,12)
if mean> 10000:
        print('I am rich')
else:
        print('I am poor')  

   