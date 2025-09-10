# function with different data as input
# passed input is infrred by function

def function1(v):
    print("Value of v=",v)
    print("type of function",type(v))

    function1(12)
    function1(44.7)
    function1(True)
    function1("Pune")