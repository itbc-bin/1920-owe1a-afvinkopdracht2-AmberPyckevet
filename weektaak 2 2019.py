# je moet zelf de bestandsnaam inclusief mappen invullen
file = 'insert\\full\\file\\he_re'
# dit stuk leest je file
f = open(file, "r")
lines = f.readlines()
# de skipline contraptie zorgt er voor dat de eerste lijn niet meegenomen wordt, maar de rest wel
skipline = True
for line in lines:
    if skipline == False:
        # dit leest het aantal A, T, C, G en de totale lengte af
        aantal_a = line.count("A")
        aantal_t = line.count("T")
        aantal_c = line.count("C")
        aantal_g = line.count("G")
        lengte = len(line)
        #dit berekent de cg%, maar zet er zelf geen % achter
        cg=((aantal_c+aantal_g)/lengte*100)
        #dit print het cg% en zet er een % achter
        print(str(cg)+"%")
    skipline = False
