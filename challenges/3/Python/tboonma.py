def fibonacci(seq):
    first_seq = 0
    second_seq = 1
    fibo = []
    if seq == 1:
        return [first_seq]
    elif seq == 2:
        return [first_seq, second_seq]
    fibo.append(first_seq)
    fibo.append(second_seq)
    for i in range(seq-2):
        temp = second_seq
        second_seq += first_seq
        first_seq = temp
        fibo.append(second_seq)
    return fibo

while True:
    seq = input("Enter the element number (enter q to quit): ")
    if seq == 'q' or seq == 'Q':
        print("Bye")
        break
    try:
        seq = int(seq)
    except:
        print("Please input an integer")
        continue
    if seq <= 0:
        print("Please input an integer")
        continue
    print("Fibonacci {0} sequence(s) is {1}".format(seq, fibonacci(seq)))