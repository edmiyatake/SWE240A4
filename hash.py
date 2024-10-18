arr1 = []
f = open("fifteen.txt","r")
for line in f:
    arr1.append(line)
f.close()

def strToASCII(str):
    sum = 0
    # problem was that the first char was not taking precedence
    # as i increases terms in sum should get smaller if divided by i
    for i in range(0,1):
        newSTR = str[slice(8,33)]
        sum += ord(newSTR[i]) + (ord(newSTR[i+1]) * 0.1) + (ord(newSTR[i+2]) * 0.01)
    return sum

for element in arr1:
    print(f"The name is {element[slice(8,33)]} and the corresponding value is: {strToASCII(element)}")
