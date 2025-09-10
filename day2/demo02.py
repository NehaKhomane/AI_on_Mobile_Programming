
# when you perfoem addition type of parameter should be same
def addition(n1,n2):
    res=n1+n2
    return res
res1=addition(20,7)
print("res1",res1)

res2=addition(33,addition(22,7))
print("res2",res2)

print("res=",addition(22,7))

res4=addition("sunbeam","Pune")
print("res4",res4)

res5=addition(44,addition(89,65))
print("res5",res5)
# res5 = addition("sunbeam", 44)  TypeError: can only concatenate str (not "int") to str
# print("res5 =", res5)