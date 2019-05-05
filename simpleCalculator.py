#take two numbers and an operator from a user
n1 = input("Enter first number: ")
n2 = input("Enter second number: ")
op = input("Enter operator: ")

#convert number input to int
n1 = int(n1)
n2 = int(n2)

#write ifs that will add, subt, mult, and divide based on operator specified by user
if op == "+":
    print("{} + {} = {}".format(n1,n2,n1+n2))
elif op=="*":
    print("{} * {} = {}".format(n1,n2,n1*n2))
elif op=="-":
    print("{} - {} = {}".format(n1,n2,n1-n2))
elif op=="/":
    print("{} / {} = {}".format(n1,n2,n1/n2))
else:
    print("incorrect math operator!!! Please Enter *, +, / or -")
