linesCount = int(input())
x = 0
for i in range(linesCount) :
    data = input()
    if "-" in data :
        x -=  1
    else:
        x+= 1

print(x)