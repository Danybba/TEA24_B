upper_limit = 500
lower_limit = 200

outliers = False

number = input("Enter a number: ")

if(number == ""):
    error = True
else:
    number = int(number)
    error = False


if (False == error):
    if (number > upper_limit):
        outliers = True
    elif (number < lower_limit):
        outliers = True
    else:
        outliers = False

if (True == outliers) and (False == error):
    print(f"This number {number} is an outlier")
if (True == error):
    print("an error occured")

