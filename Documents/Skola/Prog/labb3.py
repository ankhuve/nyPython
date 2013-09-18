###################################
def menyVal():
    nederbord = []
    val = None
    while val != "3":
        print("""
        1 - Mata in nederbörd månadsvis under ett år
        2 - Se statistik för detta år
        3 - Avsluta
        """)
        val = input("Ditt val: ")
        if val == "1":
            nederbord = inmatning()
        elif val == "2":
            statistik(nederbord)
        elif val == "3":
            print("Hejdå!")
        else:
            print("Det var inget giltigt val! Försök igen: ")
##################################
def inmatning():
    nederbord = []
    for i in range(12):
        try:
            nederbördMånad = float(input("Ange för månad " + str(i+1) + ": "))
        except:
            nederbördMånad = input("Du har angett en felaktig siffra, försök igen: ")
        nederbord.append(nederbördMånad)
    return nederbord
#####################################    
def statistik(nederbord):
    if nederbord: 
        nederbord.sort(key=float)
        totalÅr = 0
        for i in nederbord:
            totalÅr += float(i)
        medel = totalÅr/12
        print("Medelvärde under året: ", medel)
        print("Min nederbörd: ", nederbord[0])
        print("Max nederbörd: ", nederbord[-1])
    else:
        print("Det fanns inga värden, mata in dem först!")
#######################################
menyVal()
