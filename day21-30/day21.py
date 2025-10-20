# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

def my_function(*kids):
  print("The youngest child is " + kids[3])

my_function("Emil", "Tobias", "Linus","Leo")



def my_function2(fname, lname):
  print(fname + " " + lname)

my_function2("Emil", "Refsnes")

