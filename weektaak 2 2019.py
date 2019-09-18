# naamgeving bestand
file = 'insert\\full\\file\\he_re'
f = open(file, "r")
lines = f.readlines()
skipline = True
for line in lines:
    if skipline == False:
        aantal_a = line.count("A")
        aantal_t = line.count("T")
        aantal_c = line.count("C")
        aantal_g = line.count("G")
        lengte = len(line)
        cg=((aantal_c+aantal_g)/lengte*100)
        print(str(cg)+"%")
    skipline = False
