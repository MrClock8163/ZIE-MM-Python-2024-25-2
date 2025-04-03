def game(steps):
    trap = [0]
    ladders = 0

    for s in steps:
        newstep = trap[-1] + s
        if newstep % 10 == 0:
            newstep = newstep - 3
            ladders += 1
        
        trap.append(newstep)

    print("2. feladat")
    result = ""
    for s in trap[1:]:
        result += str(s) + " "

    print(result)
    print(str(trap[1:])[1:-1].replace(",", ""))
    print(" ".join(map(lambda n: str(n), trap[1:])))

    print("3. feladat")
    print("A jatek soran " + str(ladders) + " alkalommal lepett letrara.")
    print("A jatek soran", str(ladders), "alkalommal lepett letrara.")
    print(f"A jatek soran {ladders} alkalommal lepett letrara.")
    print("A jatek soran {0} alkalommal lepett letrara.".format(ladders))
    print("A jatek soran %d alkalommal lepett letrara." % ladders)

    print("4. feladat")
    if trap[-1] >= 45:
        print("A jatekot befejezte.")
    else:
        print("A jatekot abbahagyta.")


def read_steps(filepath):
    with open(filepath, encoding="utf8") as file:
        data = file.read().strip().replace(" ", "").split(",")
    
    steps = list(map(int, data))
    steps = [int(x) for x in data]

    steps = []
    for x in data:
        steps.append(int(x))

    return steps


steps = read_steps("...") # valami fajl elresei ut
game(steps)
