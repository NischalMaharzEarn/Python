fir = 8
lll = 8
print(id(fir))
print(id(lll))
if 8 == 8 :
    print("We are same")
elif 6 < 8 :
    print("This is less")      
else :
    print("We are not the same")     #Runs the first true statement


if 8 == 8 :
    print("We are same")
if 6 < 8 :
    print("This is less")      
else :
    print("We are not the same")    # Runs all the thue statement    

a = 6 if 6 > 5 else 9
print(a)  

if 6 > 4:
    pass
else:
    print("It hasnt been passed")  # pass if you have not declared to print anything



# and both needs to be true
# or if any one is true then true 

print(True and True)
print(True and False)
print(False and False and False) # And Case


print(True or False)
print(True or True)
print(False or False)
print(False or False or True)  #Or case

if 8 > 3 or (4 % 3 + 3 - 344):
    print("see first statement is true or not . if true it executes")
else:
    print("Hello it is false")    



a = input("Enter the first number")
b = input("Enter the second number")

if int(a) % 2 == 0:
    print("it is even number")
else:
    print("it is a odd number")    



student_num = {
    'nischal' : 50,
    'sujan' : 10,
    'raj' : 5
}
name = input('Enter the student')

if student_num[name] >= 40 and student_num[name] <= 100:
    print('Student is passed')
else:
    print('Student is failed')    

i = 0
while i < 10:
    print('I am growing')
    i = i + 12

    
