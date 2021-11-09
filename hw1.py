#input salaries
def average():
    salarieslen = input('Enter salary length')
    salaries = []
    i = int(salarieslen)
    j = int(len(salaries))
    print(j)
    #create empty salaries list
    while j < i:
        salary = input('Enter a salary')
        salaries.insert(j, salary)
        j = j + 1
    print(salaries)
    totalsalary = 0
    for item in range(0,len(salaries)):
        totalsalary = totalsalary + int(salaries[item])
    averagesalary = totalsalary / i
    print(averagesalary)
    if averagesalary > 10000:
        print('I am rich')
    else:
        print('I am poor')    
average()    








        



  
