#exception handling

def function11():
    try:
        num=int(input("enter the  first number"))
        den=int(input("enter the second number"))
        result=num/den
        print("result",result)
    except:
        print("something went wrong..please correct it..")
    else:
        print("program executed successfully")
    finally:
        print("Bye")   
function11()         
