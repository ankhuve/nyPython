text = open("highscores.txt", "r")
info = text.read()
hs_dict = {}
for entry in info.replace("%", "").splitlines():
    entry = entry.split(" | ")
    hs_dict[entry[0]] = entry[1]
sorted_hs = sorted(hs_dict.items(), key=lambda a: float(a[0]), reverse=True)
print(sorted_hs)
##top_ten_pct = []
##[top_ten_pct.append(float(sorted_hs[i][0])) for i in range(10)]
##print(top_ten_pct)

nyfil = open("nyfil.txt", "w+")
for i in sorted_hs:
    nyfil.write(str(float(i[0]))+" | "+i[1]+"\n")
nyfil.close()
