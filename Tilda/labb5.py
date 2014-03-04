def search(hashtabell, atomlista):
    s = input("Atombeteckning: ")
    name_list = []
    for element in atomlista:
        name, weight = element.split()
        name_list.append(name.lower())
    if s.lower() in name_list:
        print(hashtabell.get(s).weight)
    else:
        print("Okänd atom. Försök igen.")
