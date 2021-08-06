numberOfPlayer , kplace = map(int , input().split())

listofscore = input().split(" ")
for i in range(numberOfPlayer):
    listofscore[i] = int(listofscore[i])

passer = 0
for i in listofscore :
    if i >= listofscore[kplace - 1] and i > 0 :
        passer += 1
    else:
        break


print(passer)


