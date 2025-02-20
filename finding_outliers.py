upper_limit = 500
lower_limit = 200


outliers= False


number = int(input("Put Number: "))


if (upper_limit<=number) or (lower_limit>=number):
    outliers = True 
else:
    outliers = False  

if outliers == True:
    print("it is")
else:
    print("it is not")

