integers = []
sum = 0

with open('input.txt', 'r') as file:
    for line in file:
        integers = list(map(int, line.split()))
        
        #print(integers)
        
        numOfIntegers = len(integers)        
        isIncreasing = False
        isDecreasing = False

        if (integers[0] < integers[1]):
            isIncreasing = True
            isDecreasing = False

        if (integers[0] > integers[1]):
            isDecreasing = True
            isIncreasing = False

        for i in range(numOfIntegers - 1):
            if (isIncreasing):
                if (integers[i] >= integers[i+1]):
                    isIncreasing = False
                    break
            if (isDecreasing):
                if (integers[i] <= integers[i+1]):
                    isDecreasing = False
                    break
            if (isIncreasing):
                if (integers[i+1] - integers[i] > 3):
                    isIncreasing = False
                    break
            if (isDecreasing):
                if (integers[i] - integers[i+1] > 3):
                    isDecreasing = False
                    break

        if (isIncreasing or isDecreasing):
            sum += 1
            #print(" - safe")
        #else:
            #print(" - unsafe")

        integers.clear()

with open('output.txt', 'w') as file:
    file.write(str(sum))

print(sum)
