input_file_path = 'C:\\Users\\slavomir.furman\\source\\repos\\AdventOfCode\\2024\\day04\\part_two\\input.txt'
output_file_path = 'C:\\Users\\slavomir.furman\\source\\repos\\AdventOfCode\\2024\\day04\\part_two\\output.txt'

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
        if arr[j][i] == 'A':
            print("A found at [", j, "][", i, "]")
            #find X-MAS rotated at 0 degrees
            if i + 1 < x and j + 1 < y:
                if arr[j-1][i-1] == 'M' and arr[j-1][i+1] == 'S' and arr[j+1][i+1] == 'S' and arr[j+1][i-1] == 'M':
                    xmasCount += 1
                    print("XMAS found rotated at 0 degrees")
            #find X-MAS rotated at 90 degrees
            if i + 1 < x and j + 1 < y:
                if arr[j-1][i-1] == 'M' and arr[j-1][i+1] == 'M' and arr[j+1][i+1] == 'S' and arr[j+1][i-1] == 'S':
                    xmasCount += 1
                    print("XMAS found rotated at 90 degrees")
            #find X-MAS rotated at 180 degrees
            if i + 1 < x and j + 1 < y:
                if arr[j-1][i-1] == 'S' and arr[j-1][i+1] == 'M' and arr[j+1][i+1] == 'M' and arr[j+1][i-1] == 'S':
                    xmasCount += 1
                    print("XMAS found rotated at 180 degrees")
            #find X-MAS rotated at 270 degrees
            if i + 1 < x and j + 1 < y:
                if arr[j-1][i-1] == 'S' and arr[j-1][i+1] == 'S' and arr[j+1][i+1] == 'M' and arr[j+1][i-1] == 'M':
                    xmasCount += 1
                    print("XMAS found rotated at 270 degrees")


print(xmasCount)

with open(output_file_path, 'w') as file:
    file.write(str(xmasCount))

        
        


        
        
        


