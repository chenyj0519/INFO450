# print out all numbers between 0 and 99 (inclusive)
# that are evenly divisible by 3, then squared.


x = 0
count = 0
sz = []
y = 0
 
while x < 100:
    x += 1
    if x%3 == 0:
        sz.append(x)
        count += 1
        print("The number can be devided by 3 are:",x)
 
for x in sz:
    y =x*x
    print("The squared of the number can be devided by 3 are%",(count,y))
