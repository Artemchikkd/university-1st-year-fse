x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

sum1 = x1 + y1
sum2 = x2 + y2

if sum1 % 2 == sum2 % 2:
    print("YES")
    
    
    if sum1 % 2 == 0:
        print("White")
    else:
        print("Black")
else:
    print("NO")
