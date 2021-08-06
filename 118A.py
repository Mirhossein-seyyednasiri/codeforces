vowels = ["a" , "e" , "i" ,"o" , "u" , "y"]

string = input()
string = string.lower()
result = "."
for i in string:
    if i in vowels :
        pass
    else:
        result += i+"."
print(result[:-1])