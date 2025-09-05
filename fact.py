
''' Factorial of a no.'''

def fact(n):
    if n==0 or n==1:
        return  1
    else:
        result = 1
        for i in range(1,n+1):
            result*=i
        return result
num=int(input("Enter a no: "))
print(f"The factorial of {num} is: {fact(num)}")