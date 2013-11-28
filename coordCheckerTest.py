li = [(2, -1),(5, 7),(10, 6),(10, -1)]
print(li)
for n in li:
    checked_coords = []
    for coord in n:
        if coord>9:
            checked_coords.append(9)
        elif coord<0:
            checked_coords.append(0)
        else:
            checked_coords.append(coord)
    li[li.index(n)] = (checked_coords[0], checked_coords[1])

print(li)
