def find_max(list):
    max = list[0]
    for number in list:
        if (number > max):
            max = number
    return max

list = [1,2,3,4,5]
max = find_max(list)
print('Max:',max)