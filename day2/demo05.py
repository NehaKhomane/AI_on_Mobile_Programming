# function with 4 params -- can be positional or can be keyword


def print_info1(name, age , addr, mobile):
    print("name =",name," age =",age," address =",addr," mobile =",mobile)

# print_info1("Ravi", 15 , "Pune", "9876767654")  #positional arguments

# print_info1(name="Ravi",age=15,addr="Pune",mobile="987667676") #named/keyword parameters
# print_info1(addr="Pune",name="Ravi",mobile="987667676",age=15)


def print_info2(name, age , addr, mobile,/):
    print("name =",name," age =",age," address =",addr," mobile =",mobile)

# print_info2("Ravi", 15 , "Pune", "9876767654")  #positional arguments
# print_info2(name="Ravi",age=15,addr="Pune",mobile="987667676") error
# print_info2("Ravi", 15 , addr="Pune", mobile="987667676") error

def print_info3(*,name, age , addr, mobile):
    print("name =",name," age =",age," address =",addr," mobile =",mobile)

# print_info3(name="Ravi",age=15,addr="Pune",mobile="987667676")
# print_info3("Ravi", 15 , addr="Pune", mobile="987667676") error
# print_info3("Ravi", 15 , "Pune", "9876767654") error

def print_info4(name, age ,/, addr, mobile):
    print("name =",name," age =",age," address =",addr," mobile =",mobile)

# print_info4("Ravi", 15 , addr="Pune", mobile="987667676")  # ok
# print_info4("Ravi", 15 , "Pune", "9876767654") # ok
# print_info4(name="Ravi",age=15,addr="Pune",mobile="987667676") error

def print_info5(name, age ,/,*, addr, mobile):
    print("name =",name," age =",age," address =",addr," mobile =",mobile)

# print_info5("Ravi", 15 , addr="Pune", mobile="987667676")  # ok
# print_info5("Ravi", 15 , "Pune", "9876767654") # error
# print_info5(name="Ravi",age=15,addr="Pune",mobile="987667676") # error

# def print_info6(name, age ,*,/, addr, mobile):
#     print("name =",name," age =",age," address =",addr," mobile =",mobile)
