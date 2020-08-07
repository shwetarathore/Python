# a = True
# b = False

# if a and b:
#     print("True")
# else:
#     print("False")   

# name = input('name pls! - ')
# # name_len = len(name)

# if len(name) < 3:
#     print("name length should be more than 3")
# elif len(name) > 8:
#     print("name length should be less than 8")
# else:
#     print("name looks fine!")    

weight = int(input("Weight: "))
unit = input("(L)bs or (k)g:")

if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kg")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")