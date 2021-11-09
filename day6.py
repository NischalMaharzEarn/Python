# Format
a = 5
b = 6
c = 8

print(f'Welcome {a} {b} {c}')


# Function
def add():
    print(10 + 15)
add()

#arguements Parameters 
def minus(a,b,c):
    print(a + b + c )

minus(5, 65, 45) 

#Variable length arguement
def add(*args):
    print(args)

add(1,2,2,1,2,1,2,2)


# Write a function named average that accepts variable length salary
# the function calculates the average of the salary
# if avg is greater than 10k, print I am rich
# if avg is less than 10k, print I am poor