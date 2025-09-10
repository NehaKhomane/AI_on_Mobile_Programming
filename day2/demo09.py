# python -- scope of var/fn -- where that var/fn is accessible?
#   global var -- accessible in whole program (after its definition)

# global keyword
#   1. modify global var inside a fn
#   2. make a var assigned in fn as global - to access it outside later

num=100

#def func1():
  #  print("func1:num1=" ,num)#100

#def func2():
#    global num
#    num=200
#    print("func2():num1",num)
    ##200

#func1()
#func2()

def function1():
    global name
    name="sunbeam"
    print("name=",name)

function1()
print("name",name)


def function2():
    print("name",name)
function2()    