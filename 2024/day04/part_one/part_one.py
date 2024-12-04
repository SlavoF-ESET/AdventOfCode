input_file_path = 'C:\\Users\\slavomir.furman\\source\\repos\\AdventOfCode\\2024\\day04\\part_one\\input.txt'
output_file_path = 'C:\\Users\\slavomir.furman\\source\\repos\\AdventOfCode\\2024\\day04\\part_one\\output.txt'

xmasCount = 0

x = 0
y = 0

arr = []
arr.append([]) 
y += 1

with open(input_file_path, 'r') as file:
    while True:

        char = file.read(1)
        if char != '\n':
            arr[y-1].append(char)
            if y == 1:
                x += 1

        if not char:
            break

        if char == '\n':
            arr.append([])
            y += 1
            continue

print(x, y)

# print(arr)
# print(arr[0][2])
# print(arr[1][1])

# for j in range(y):
#     for i in range(x):
#         print("arr[", j, "][",i,"] = ", arr[j][i])


for j in range(y):
    for i in range(x):
        if arr[j][i] == 'X':
            print("X found at [", j, "][", i, "]")
            #find XMAS in row forward
            if i + 3 < x:
                if arr[j][i+1] == 'M' and arr[j][i+2] == 'A' and arr[j][i+3] == 'S':
                    xmasCount += 1
                    print("XMAS found in row forward")
            #find XMAS in row backward
            if i - 3 >= 0:
                if arr[j][i-1] == 'M' and arr[j][i-2] == 'A' and arr[j][i-3] == 'S':
                    xmasCount += 1
                    print("XMAS found in row backward")
            #find XMAS in column down
            if j + 3 < y:
                if arr[j+1][i] == 'M' and arr[j+2][i] == 'A' and arr[j+3][i] == 'S':
                    xmasCount += 1
                    print("XMAS found in column down")
            #find XMAS in column up
            if j - 3 >= 0:
                if arr[j-1][i] == 'M' and arr[j-2][i] == 'A' and arr[j-3][i] == 'S':
                    xmasCount += 1
                    print("XMAS found in column up")
            #find XMAS in diagonal down-right
            if i + 3 < x and j + 3 < y:
                if arr[j+1][i+1] == 'M' and arr[j+2][i+2] == 'A' and arr[j+3][i+3] == 'S':
                    xmasCount += 1
                    print("XMAS found in diagonal down-right")
            #find XMAS in diagonal up-right
            if i + 3 < x and j - 3 >= 0:
                if arr[j-1][i+1] == 'M' and arr[j-2][i+2] == 'A' and arr[j-3][i+3] == 'S':
                    xmasCount += 1
                    print("XMAS found in diagonal up-right")
            #find XMAS in diagonal down-left
            if i - 3 >= 0 and j + 3 < y:
                if arr[j+1][i-1] == 'M' and arr[j+2][i-2] == 'A' and arr[j+3][i-3] == 'S':
                    xmasCount += 1
                    print("XMAS found in diagonal down-left")
            #find XMAS in diagonal up-left
            if i - 3 >= 0 and j - 3 >= 0:
                if arr[j-1][i-1] == 'M' and arr[j-2][i-2] == 'A' and arr[j-3][i-3] == 'S':
                    xmasCount += 1
                    print("XMAS found in diagonal up-left")

print(xmasCount)

with open(output_file_path, 'w') as file:
    file.write(str(xmasCount))

        
        


        
        
        


