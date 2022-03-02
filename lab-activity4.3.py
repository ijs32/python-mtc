# Write a function that receives a number of arguments; using a continue statement, skip integers and
# print out all other values.

# Write your code here
def skip_integers(*args):
    for arg in args:
        if type(arg) == int:
            continue
        else:
            print(arg)


# Test you code here
skip_integers(3, 5.2, "value", 6.0)
