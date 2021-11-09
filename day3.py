print('nischal '*2) # print 2 times
print(int(5/2))
print(int(4.334)) # converts into int
print(float(True))
print(str(True)) # change into string true
print(bool('True')) #change into boolean true

#List
Fruits = [
'apple','banana','orange',52,52.12
]
print(id(Fruits))
Fruits.append('cherry')
print(id(Fruits))
print(Fruits[:])
students = [] # Creating an empty list
print(len(Fruits))
print(Fruits[:])
Fruits.insert(1, 'lol')
print(Fruits)
Fruits.remove(Fruits[1])
print(Fruits)
Fruits.pop(0)
Fruits.pop(0)

print(Fruits)

Fruits.reverse()
print(Fruits)
Fruits.clear()
del Fruits # Deleting fruits

#not to change list of same 
l1=[1,2,3,4,5]
l2=l1.copy()
l2[0] = 'Hello'
print(l1)

# Tuple
car = ('Sun' , 'Mon' , 'Tue' , 'Wed')

# Sets
a = {1,2,3,4}
b = {5,6,7,8}
print(a.difference(b))
a.add('hekkow')
print(a)

