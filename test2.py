# global vars



# functions


def sum(num1, num2):
    result = num1 + num2
    print(result)

def division(num1, num2):
    # if the second number is 0,print an error
    # otherwise, divide and print the result
    if num2 == 0:
        print("error")
    else:
        result = num1 / num2
        print(result)


def print_greater(num1, num2):
    # if num1 is greater than num2, print num1
    # otherwise, print num2
    if num1 > num2:
        print(num1)
    else:
        print(num2)
    
def print_numbers():
    nums = [12,3,53,67,12,8,45,87,31,98,30,82,24,16,82,68,34]
    # print numbers lower than 50

    for x in nums:
        if x < 50:
            print(x)

def print_list():
    names = ["jason","Michael"]

    # add elements
    names.append("John")
    names.append("Mary")

    # READ
    print(names[0])
    print(names[2])

    # check if an element exists
    if  "Lauren" not in names:
        names.append("Lauren")

    print(names)


def print_dict():
    me = {
        "name": "Cody",
        "last_name": "Deal",
        "hobbies": ["bodybuilding", "gaming", "coding"]
    }

    print(me)

    # read
    print(me["name"])

    # add
    me["age"] = 30

    # modify
    me["age"] = 31

    print(me)

    me["last_name"] = me["last"]
    del me["last"]


    # check if a key exists befre reading
    if "invalid" in me:
        print(me["invalid"])



# call functions





sum(21, 24)
sum(-3, 9)
sum(12431, 32524)

division(10, 2) #should print 5
division(0, 10) #should print 0
division(10, 0) #should print error

print_greater(10, 2) #should print 10
print_greater(0, 10) #should print 10
print_greater(10, 15) #should print 15

print("--------------------")
print_numbers()
print_list()
print_dict()