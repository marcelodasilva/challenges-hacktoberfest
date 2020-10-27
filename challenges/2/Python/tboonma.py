import statistics

number_list = []
for i in range(5): 
    number_list.append(int(input("number {0}: ".format(i+1))))

print("\nMean : {0}\n".format(statistics.mean(number_list)))