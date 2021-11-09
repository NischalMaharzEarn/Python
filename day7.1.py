a = 10
def aa():
    a = 100
aa()
print(a)

# using global variable
salary = 1000
def salaryconfirm():
    global salary
    salary = salary + 5
salaryconfirm()