def add(x,y):
    print("add",x+y)

def sub(x,y):
    print("sub",x-y)

def mul(x,y):
    print("multi",x*y)

result=[add,sub,mul]

for f in result:
    f(11,4)
