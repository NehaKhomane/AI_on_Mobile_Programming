# docstring in python
#   documentation of function or classes.
#   the first statement of the function can be a simple string - description/doc of the func.

print("hello",end=" ")#continue with the same line
print("hello")

def my_function(a,b):
    '''This is my simple function
    parameter 1: a(int)
    parameter 2:b (int)'''
    print("----inside the my_function-------")

    print("name of function=",my_function.__name__)
    print("info of function=",my_function.__doc__)