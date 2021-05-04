import sys

def add(a,b):
    return(a+b)
def sub(a,b):
    return(int(a) - int(b))
def multiply(a,b):
    return(int(a)*int(b))
def divide(a,b):
    return(int(a)/int(b))

'''
a=int(input("enter 1st no:"))
b=int(input("enter 2nd no:"))
print(add(a,b))
print("thus addition is performed")
print(sub(a,b))
print("thus subtraction is performed")
print(multiply(a,b))
print("thus multiplication is performed")
print(divide(a,b))
print("thus division is performed")
'''


if __name__ == "__main__":
    a = sys.argv[1];
    b = sys.argv[2];
    add_value=add(a,b)
    print(add_value)
    sub_value=sub(a,b)
    print(sub_value)
    multi_value=multiply(a,b)
    print(multi_value)
    div_value=divide(a,b)
    print(div_value)

