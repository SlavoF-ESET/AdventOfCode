input_file_path = 'C:\\Users\\slavomir.furman\\source\\repos\\AdventOfCode\\2024\\day05\\part_one\\input.txt'
output_file_path = 'C:\\Users\\slavomir.furman\\source\\repos\\AdventOfCode\\2024\\day05\\part_one\\output.txt'

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
                print("Current print:   ")
                print(arrCurentPrint)

                pos = 0
                isPrintCorrent = True

                for pos in range(len(arrCurentPrint)):
                    for j in range(len(arrCurentPrint)):
                        if j > pos:
                            for q in range(len(arrRules)):
                                if arrCurentPrint[j] == arrRules[q][0] and arrCurentPrint[pos] == arrRules[q][1]:
                                    isPrintCorrent = False
                                    print("Print is broken!")
                                    print("Sequence: ", arrCurentPrint[j], " | ", arrCurentPrint[pos], "breaks the rule: ", arrRules[q][0], " | ", arrRules[q][1])  
                                    break
                        if isPrintCorrent == False:
                            break
                    if isPrintCorrent == False:
                        break    

                if isPrintCorrent == True:
                    print("Print is correct!")                            
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

        
        


        
        
        


