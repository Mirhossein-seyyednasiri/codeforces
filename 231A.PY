problemCount = int(input())


count = 0 

for i in range(problemCount) :
    data = input()
    if data.count("1") >= 2 :
        count += 1
    else:
        pass


print(count)