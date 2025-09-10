def function1():
    print("Inside the function1:")
function1()
print("type of the function",type(function1))
print("name of the function1",function1.__name__)
print("Address of the function",id(function1))    

func2=function1
func2()
print("type of func2:",type(func2))
print("name of func2: ",func2.__name__)
print("address of func2: ",id(func2))