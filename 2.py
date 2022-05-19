def parse(s):
    strana = s[:s.find(" ")]
    gorodd = s[s.find(" ")+1:]
    gorod = gorodd.split(" ")
    for i in range (len(gorod)):
        gorod[i] = gorod[i].strip()
    return ( strana, gorod)
N = int(input())
goristran = {}
goristran2 = {}
for i in range (N):
    s = input()
    strana, gorod = parse (s)
    for gorods in gorod:
        if gorods is not goristran:
            goristran[gorods] = []
        goristran[gorods].append(strana)
M = int(input())
for k in range (M):
    print(*goristran[input()],sep="\n")
