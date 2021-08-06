row = 0
colume = 0

for i in range(5):
    line = input().split()
    if "1" in line :
        colume = line.index("1")
        row = i 

print(abs(row -2 ) + abs(colume - 2))