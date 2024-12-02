leftnum = []
rightnum = []

with open('input.txt', 'r') as file:
    for line in file:
        a, b = map(int, line.split())
        # print(f"First integer: {a}, Second integer: {b}\n")
        leftnum.append(a)
        rightnum.append(b)

leftnum.sort()
rightnum.sort()

print(leftnum)
print(rightnum)

sum = 0

for i in range(len(leftnum)):
    sum += abs(leftnum[i] - rightnum[i])

with open('output.txt', 'w') as file:
    file.write(str(sum))

print(sum)