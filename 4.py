fin = open("input_6_3_1.csv", "r", encoding= 'utf8')
fout = open("rezultat.txt", "w", encoding="utf8")
x = fin.read()
Companys = {}

for line in x.split('\n'):
    if len(line.split(';')) == 2:
        Company, value = line.split(';')
        value = int(value)
        if Company in Companys:
            Companys[Company] += [value]
        else:
            Companys[Company] = [value]
for k, v in Companys.items():
    Companys[k] = sum(v) / len(v)
for i in sorted(Companys.items(), key = lambda x: [x[1], x[0]]):
    print(*i[0], sep="")

fout.close()
fin.close()
