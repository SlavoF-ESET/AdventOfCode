input_file_path = 'C:\\Users\\slavomir.furman\\source\\repos\\AdventOfCode\\2024\\day05\\part_two\\input.txt'
output_file_path = 'C:\\Users\\slavomir.furman\\source\\repos\\AdventOfCode\\2024\\day05\\part_two\\output.txt'

sum = 0

arrRules = []
arrCurentPrint = []

areRulesRead = False

with open(input_file_path, 'r') as file:
    for line in file:
        if areRulesRead == False:
            if line.strip():
                pair = tuple(map(int, line.strip().split('|')))
                arrRules.append(pair)
            else:
                areRulesRead = True
                continue
        else:
            # print("Rules:   ")
            # for i in range(len(arrRules)):
            #     print(arrRules[i][0], " | " , arrRules[i][1])

            if line.strip():
                arrCurentPrint.clear()
                arrCurentPrint = list(map(int, line.strip().split(',')))
                numInPrint = len(arrCurentPrint)
                print("Current print:   ")
                print(arrCurentPrint)

                isPrintCorrent = False
                numberOfTries = 0

                while isPrintCorrent == False:

                    if numberOfTries != 0:
                        print("Trying to fix the print...# ", numberOfTries)
                        print("Fixed print:   ")
                        print(arrCurentPrint)

                    pos = 0
                    isPrintCorrent = True

                    for pos in range(numInPrint):
                        for j in range(numInPrint):
                            if j > pos:
                                for q in range(len(arrRules)):
                                    if arrCurentPrint[j] == arrRules[q][0] and arrCurentPrint[pos] == arrRules[q][1]:
                                        isPrintCorrent = False
                                        print("Print is broken!")
                                        print("Sequence: ", arrCurentPrint[j], " | ", arrCurentPrint[pos], "breaks the rule: ", arrRules[q][0], " | ", arrRules[q][1])  

                                        print("Trying to fix the print...") 

                                        clip = arrCurentPrint[j]
                                        arrCurentPrint[j] = arrCurentPrint[pos]
                                        arrCurentPrint[pos] = clip

                                        numberOfTries = numberOfTries + 1

                                        break
                            if isPrintCorrent == False:
                                break
                        if isPrintCorrent == False:
                            break    

                    if isPrintCorrent == True:
                        print("Print is correct!")   

                        if (numberOfTries > 0):                         
                            middleIndex = len(arrCurentPrint) // 2
                            sum += arrCurentPrint[middleIndex]

        continue


# print(arr)
# print(arr[0][2])
# print(arr[1][1])

# for j in range(y):
#     for i in range(x):
#         print("arr[", j, "][",i,"] = ", arr[j][i])


print(sum)

with open(output_file_path, 'w') as file:
    file.write(str(sum))

        
        


        
        
        


