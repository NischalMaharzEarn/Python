#write a function that checks if a number is odd or even 
#even values in even list and odd values in odd list
def isevenorodd(*args):
    evenlist = []
    oddlist = []
    for item in args:
        if item % 2 == 0 :
            evenlist.append(item)
        else:
            oddlist.append(item)
    return evenlist, oddlist

i , j= isevenorodd( 1,1,2 ,3,2,5,2,)    
print(i, j)

