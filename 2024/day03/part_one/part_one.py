input_file_path = 'C:\\Users\\slavomir.furman\\source\\repos\\AdventOfCode\\2024\\day03\\part_one\\input.txt'
output_file_path = 'C:\\Users\\slavomir.furman\\source\\repos\\AdventOfCode\\2024\\day03\\part_one\\output.txt'

pos = 0
state = 0

sum = 0

foundMul = ''

firstOp = 0
firstOp_str = ''
secondOp = 0
secondOp_str = ''

with open(input_file_path, 'r') as file:
    while True:
        char = file.read(1)

        if not char:
            break

        if state == 0 and foundMul != '':
            foundMul = ''
            firstOp_str = ''
            secondOp_str = ''
            firstOp = 0
            secondOp = 0
            state = 0

        pos = pos + 1
        foundMul += char            
                             
        if state == 0 and char == 'm':
            state = 1
            continue
                
        if state == 1: 
            if char == 'u':
                state = 2
                continue
            else:
                state = 0
                continue

        if state == 2: 
            if char == 'l':
                state = 3
                continue
            else:
                state = 0
                continue

        if state == 3: 
            if char == '(':
                state = 4
                continue
            else:   
                state = 0
                continue

        if state == 4: 
            if char.isdigit():
                state = 5
                firstOp_str += char
                continue
            else:
                state = 0
                continue

        if state == 5: 
            if char.isdigit():    
                firstOp_str += char
                continue
            elif char == ',':
                state = 6
                firstOp = int(firstOp_str)
                continue
            else:
                state = 0
                continue

        if state == 6: 
            if char.isdigit():    
                secondOp_str += char
                continue
            elif char == ')':
                state = 7
                secondOp = int(secondOp_str)
                sum += firstOp * secondOp            
                print("Found multiplication: [", foundMul + '] at position: ', pos)   
                print(f'{firstOp} * {secondOp} = {firstOp * secondOp}')
                print("Current sum: ", sum)
                state = 0
                continue
            else:
                state = 0                

with open(output_file_path, 'w') as file:
    file.write(str(sum))

        
        


        
        
        


