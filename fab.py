
''' Fabonacci series'''

def fab(n):
    x,y=0,1
    while x<=n:
        print (x,end=" ")
        x, y = y, x + y
        
num=int(input("Enter a no: "))
print(f"The fabonacci from 0 to {num}:")
fab(num)

