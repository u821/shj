x = 0

# try:
#     print("start code")
#     print(10 / x)
#     print("No errors")
#
# except (NameError, ZeroDivisionError) as ex:
#     print(f"we have an error: {ex}")
#
# print("code after")

try:
    print("start code")
    # print(10 / x)
    print("No errors")

except (NameError, ZeroDivisionError) as ex:
    print(f"we have an error: {ex}")

else:
    print("I am ELSE!")

finally:
    print("finally code")

def checker(value):
    if not isinstance(value,str):
        raise TypeError(f"Sorry we cannot work with {type(value)}."
                        f"We need only str"
        )
    else:
        return "Niiiicee" + value

#
# checker(100)


class BuildingError(Exception):
    def __init__(self, amount, limit):
        self.amount = amount
        self.limit = limit
    def __str__(self):
        return "Not enough materials to build!"

def check_materials(amount, limit):
    if amount > limit:
        print("Yes we can build the house!")
    else:
        raise BuildingError(amount, limit)


# check_materials(100, 250)


import warnings

# warnings.simplefilter("always", ImportWarning)
# warnings.simplefilter("always", SyntaxWarning)
# warnings.simplefilter("ignore", SyntaxWarning)
#
# warnings.warn("warning, no code here", SyntaxWarning)
# warnings.warn("warning, wrong import", ImportWarning)
#
# print("hello world")

warnings.simplefilter("error", ImportWarning)
try:
    warnings.warn("warning, wrong import", ImportWarning)
except:
    print("warning processed")