def add(x,y):
    print("add :",x+y)

def sub(x,y):
    print("sub:",x-y)

def mult(x,y):
    print("multiplication",x*y)

def calculate(a,b,op):
    print("inside the calculate")
    op(a,b)    

calculate(22,8,add)
calculate(22,8,mult)
calculate(22,8,sub)    
