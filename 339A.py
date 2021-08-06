data = input().split("+")
data.sort()

string = ""
for i in data:
    string += i + "+"
print(string[:-1])