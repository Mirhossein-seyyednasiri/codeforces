stoneNumber = int(input())

string = input()
count = 0
for i in range(1 , stoneNumber ) :

    if string[i] == string[i-1] :
        count += 1

print(count)