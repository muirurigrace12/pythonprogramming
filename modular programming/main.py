import operators
#x =operators.add(20,30)
#y = operators.subtract(40, 30)
#print(x)
#print(y)

#from operators import add
#x = add(2, 3)
#print(x)

#from operators import subtract
#y = subtract(7,6)
#print(y)

import others
import tri
#x = others.cube(3)
#print(x)

operator = input("enter operator:")

if operator == "cube":
    num = eval(input("enter a number:"))
    p =others.cube(num)
    print(p)

elif operator =="sin":
    angle = eval(input("enter an angle:"))
    sin_of_angle = tri.sin(angle)
    print(sin_of_angle)

elif operator =="tan":
    angle = eval(input("enter angle iin degress:"))
    print(tri.tan(angle))

elif operator =="cos":
    angle = eval(input("enter angle in degress:"))
    print(tri.cos(angle))

else:
    num1 = eval(input("enter the first number:"))
    num2 = eval(input("enter the second number:"))

    
    if operator =="+":
        x = operators.add(num1, num2)
        print(x)
    elif operator =="-":
        y = operators.subtract(num1, num2)
        print(y)
    elif operator =="*"or"x"or"X":
        z =operators.multiply(num1, num2)
        print(z)
    elif operator == "/":
        r =operators.divide(num1, num2)
        print(r)








