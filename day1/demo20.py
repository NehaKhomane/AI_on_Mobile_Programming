# input a month (number) from user.
#   if user input 1, then print "jan has 31 days"
#   if user input 2, then print "feb has 28 or 29 days"
#   if user input 3, then print "mar has 31 days"
#   if user input 4 or 6 or 9 or 11, then print "month has 30 days"
#   if user inputs any other number in range 1-12, then print "month has 31 days"
#   if user inputs any other number, then "invalid month"


m=int(input("Enter the month"))

match m:
    case 1:
        print("jan has 31 days")
    case 2:
        print("feb has 28 or 29 days")
    case 3:
        print("march has 31 days")
    case 4 |6 |9 |11 :
        print(" month has 30 days")  
    case x if 1 <= x <=12:
        print("month has 31 days")   
    case _:
        print("invalid month")               


        # if m == 1:
#     print("jan has 31 days")
# elif m == 2:
#     print("feb has 28 or 29 days")
# elif m == 3:
#     print("mar has 31 days")
# elif m == 4 or m == 6 or m == 9 or m == 11:
#     print("month has 30 days")
# elif 1 <= m <= 12:
#     print("month has 31 days")
# else:
#     print("invalid month")