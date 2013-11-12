text = open("highscores.txt", "r")
info = text.read()
d = info.split("\n")
d.append("53|Hejee")
d.sort()
d.reverse()
text = open("highscores.txt", "w+")

for i in d:
    print(i)
    text.write(i+"\n")
text.close()
