while True:
    F = input("Input temperature as number (q to quit): ")
    if F == 'q' or F == 'Q':
        print("Bye")
        continue
    try:
        F = float(F)
    except:
        print("Please input a number")
        continue
    C = (5 * (F-32) / 9)
    print("Temperature in Celcius :", C)
