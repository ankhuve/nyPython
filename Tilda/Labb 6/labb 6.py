import re
s = ["He\d*", "H\d*", "Li\d*","Be\d*","B\d*","Cl\d*","C\d*","Ne\d*","Na\d*","N\d*","O\d*","F\d*","Mg\d*","Al\d*","Si\d*","P\d*","S\d*","Ar\d*"]
##s = re.compile("He\d+|H\d+|Li|Be|B|Cl|C|Ne|Na|N|O|F|Mg|Al|Si|P|S|Ar")

search_string = "fhoFehiofeHFIOehfEf34892fFh3fQf38f9H#F()QH#F9"
match = re.findall('|'.join(s), search_string)
if match:
    inp = ""
    for i in match:
        inp += "".join(i)
    print("Hittade", inp, "i strängen", search_string)
else:
    print("Hittade inget.")

