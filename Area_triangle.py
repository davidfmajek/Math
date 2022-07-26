a = float(input('side a is:'))
b = float(input('side b is:'))
c = float(input('side c is:'))
s = (a+b+c)/2

area = (s*(s-a)*(s-b)*(s-c))**0.5
print(area)
