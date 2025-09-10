PI=3.14
final_name=""

def set_name(name):
    if len(name)==0:
        raise ValueError("name is blank")
    global final_name
    final_name=name

try:
    set_name("sunbeam")
    print("final name is",final_name)
except ValueError as e:
    print("name length is xero ".e)    