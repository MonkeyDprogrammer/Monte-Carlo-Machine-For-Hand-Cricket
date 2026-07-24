import random as r

#pure random:
"""
def bat(batting):
    score = 0
    while True:
        bowler = r.randint(1,10)
        if bowler == batting:
            break
        else:
            score += batting
    return score
"""

#bowler has 60% chance to repeat the same number
"""
def bat(batting):
    score = 0
    prev = None
    while True:
        if prev == None:
            bowler = r.randint(1,10)
            prev = bowler
        else:
            chance = r.randint(1,10)
            if chance <= 4:
                bowler = r.randint(1,10)
                prev = bowler
            else:
                bowler = prev
        if bowler == batting:
            break
        else:
            score += batting
    return score
"""

#Adaptive Batsman to 60% repeating bowler
def bat():
    score = 0
    prev = None
    batting = 0
    ch = [1,2,3,4,5,6,7,8,9,10]

    while True:
        choices = ch.copy()
        if prev != None:
            temp = ch.index(prev) + 1
            choices.remove(prev)
            differences = []
            for i in choices:
                if i < prev:
                    choices.remove(i)
            for i in choices:
                differences.append(i-prev)
            batting = max(differences) + temp

        else:
            batting = r.choice(choices)

        if prev == None:
            bowler = r.randint(1,10)
            prev = bowler

        else:
            chance = r.randint(1,10)

            if chance <= 4:
                bowler = r.randint(1,10)
                prev = bowler

            else:
                bowler = prev

        if bowler == batting:
            break

        else:
            score += batting

    return score

#Batsman With HardCoded Number
"""
def simulate(n):
    avg = []
    s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = s9 = s10 = 0

    for _ in range(n):
        s1 += bat(1)
    else:
        s1 = s1/n
        avg.append(s1)

    for _ in range(n):
        s2 += bat(2)
    else:
        s2 = s2/n
        avg.append(s2)

    for _ in range(n):
        s3 += bat(3)
    else:
        s3 = s3/n
        avg.append(s3)

    for _ in range(n):
        s4 += bat(4)
    else:
        s4 = s4/n
        avg.append(s4)

    for _ in range(n):
        s5 += bat(5)
    else:
        s5 = s5/n
        avg.append(s5)

    for _ in range(n):
        s6 += bat(6)
    else:
        s6 = s6/n
        avg.append(s6)

    for _ in range(n):
        s7 += bat(7)
    else:
        s7 = s7/n
        avg.append(s7)

    for _ in range(n):
        s8 += bat(8)
    else:
        s8 = s8/n
        avg.append(s8)

    for _ in range(n):
        s9 += bat(9)
    else:
        s9 = s9/n
        avg.append(s9)

    for _ in range(n):
        s10 += bat(10)
    else:
        s10 = s10/n
        avg.append(s10)

    maximum = max(avg)
    max_num = avg.index(maximum) + 1
    return max_num, maximum
"""

def simulate(n):
    avg = []
    s1 = 0

    for _ in range(n):
        s1 += bat()
    else:
        s1 = s1/n
        avg.append(s1)

    return s1

m = simulate(10000)

print(m)