# print(33/0)
# Runtime error

while True:
    a = input('Enter the name')
    try:
        if a % 2 == 0:
            print('It is even')
    except:
            print('wrong number')
    else:
            print('Hello Heloo')
    finally:
            print('Finally')


try:
    #opening the database
    pass
except:
    #code that runs when there is error while opening the database
    print('Database was not connected')
else:
    #close the database
    pass
finally:
    print('Thank you for connecting to us')





