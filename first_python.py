# # variable = "text"

# # city = "Berlin"
# # job = "Engineer"


# # car_1 = "Benz"
# # car_2 = "Audi"

# # name = "Daniel"
# # LastName = "Schäftner"

# # print('Mein Name ist: ' + name)

# # text = "5 * 5" 
# # number = 100 
# # komma = 0.5

# # powered_on = not True

# # entered_pin = 5445
# # expected_pin = 5445

# # # print(entered_pin != expected_pin)

# # print(f"{entered_pin - 6} this is the {name} pin")
# num = 2

# eingabe = input()

# print(int(eingabe) + 2)

# text = "hello"
# number = 50 * 0.1
# komma = 4.5
# boolsch = True

# print(type(text))
# print(type(number))
# print(type(komma))
# print(type(boolsch))

# help(print)


# age = int(input("Enter your age: "))

# if age >= 18:
#     print("Old enough")


# can_drive = True
# has_license = True
# has_insurance = True
# alcohol = 0.5

# age = int(input("Enter your age: "))

# if (18 <= age) and ((True == has_license) or (True == has_insurance)) and (alcohol < 0.3):
#     can_drive = True
# else:
#     can_drive = False 

# if can_drive:
#     print("Can drive")
# else:
#     print("Can't drive")


# hour = int(input("Enter the hour: "))

# if hour < 12:
#     print("Good morning")
# elif hour < 18:
#     print("Good afternoon")
# elif hour < 22:
#     print("Good evening")
# else:
#     print("Good night")

text = input("Enter a text: ")

if "word" in text.lower():
    print("The word is in the text")