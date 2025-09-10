def add(x,y):
    print("add:",x+y)

f1=lambda x,y :print("add:",x+y)  

f1(22,8)
print("name of the fn=",f1.__name__)
print("type of f1",type(f1))


f2=lambda x,y :print("sub:",x-y)
f3=lambda x,y :print("multi",x*y)

def calc(a,b ,op):
    op(a,b)
calc(20,4,f1)
calc(20,4,f2)
calc(20,4,f3)
calc(20,4,lambda x,y : print("div=",x/y))    