while True:
    x = input("Input 1st number : ")
    try:
        x = float(x)
        break
    except:
        print("Please input a number")
while True:
    y = input("Input 2nd number : ")
    try:
        y = float(y)
        break
    except:
        print("Please input a number")
if x > y:
    print("The Biggest Number is", x)
elif x < y:
    print("The Biggest Number is", y)
else:
    print("Two Numbers are equal")