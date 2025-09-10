def function5():
    try:
        num=int(input("Enter the number"))
        num2=int(input("Enter the number"))
        result=num/num2
        print("result",result)
    except ValueError:
        print("you are not entered any number..please enter the number")
    except ZeroDivisionError:
        print("den never divide by zero")  
    except:
        print("Something went wrong")  

function5()        