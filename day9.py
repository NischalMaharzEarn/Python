f = open('b.txt','w') #Creates a file 
f.write('I am shawn') #Writes int that file and also overwrites the original  content
f = open('b.txt','a')
f.write('Hello hello hello') # Adds this line to the existing file
f = open('b.txt','w')
f.writelines('Hello hello hello') # Adds this line to the existing file
f.close() # closes the file and saves the resources
print(f.close()) # prints the result is closed or not

with open('abc.txt','w') as f: #Easy way to handle a single file multiple times
    f.close()
    
data1 = open('qwe.txt','w') # Lendy way to handle a single file
data2 = open('qwe.txt','w')
data3 = open('qwe.txt','w')
data4 = open('qwe.txt','w')



