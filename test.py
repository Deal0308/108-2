# this is a comment


last_name = "Smith"
first_name = "John"
age = 20
price = 19.99
found = False

print(last_name)
print(first_name)

print(first_name + " " + last_name)

print(age / 2)
print (price / 2)

print(first_name + str(age))

# if / else

if(age < 100):
    print("dont worry, you are still young")
    print("inside the if")

    if True:
        print("another level")
print("outside the if")


if age < 100:
    print("dont worry, you are still young")


elif age == 100:
    print("you are at the century mark")


else:
    print("you are getting old")

print("outside the if")

# functions

def say_hello():
    print("hello there")

def greet(name):
    print("hello " + name)

# call fns
say_hello()
say_hello()
say_hello()
say_hello()
