import random as r
import data as d

c = 0
score = 0
x = input("Name: ")
ar = []

while True:
    temp = input("Bowler (number, Quit): ")

    if temp.lower() == "quit":
        break
    else:
        bow = int(temp)

    #6 turns to collect Data will converge to 10.. make sure to use a bigger number
    if c <= 6:
        bat = r.randint(1,10)
        if bat == bow:
            print(score)
            print("Out")
            #break
        else:
            score += bat
        print(bat,c)
        ar.append(bow)
        c += 1
    else:
        prob = []
        for n in range(1, 11):
            p = ar.count(n) / len(ar)
            prob.append((1 - p) * n)

        bat = prob.index(max(prob)) + 1

        if bat == bow:
            print("OUT")
            print(score)
            break
        else:
            score += bat
        ar.append(bow)
        print(bat)
