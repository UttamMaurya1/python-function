# def f_to_c(f):
#     return 5*(f-32)/9

# f = int(input("Enter temp: "))
# print(f"{f_to_c(f)} ")

def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter temp: "))
c = f_to_c(f)
print(f"{round(c, 2)} ")