#def fn_outer():
 #   def fun_inner():
  #      print("Inside the inner function")
  #  fn_inner()
  #  print("inside the fun outer")   


def fun_outer():
    global fun_inner
    def fun_inner():
        print("Inside the inner function") 
    print("inside the outer function")
fun_outer()
fun_inner()            