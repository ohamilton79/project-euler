#Oliver Hamilton
#Special Pythagorean triplet
#20/12/2020

#If a, b and c add to 1000, they are either all even
for b in range(1, 999, 2):
    for c in range(b+2, 999, 2):
        a = 1000 - b - c
        if (a ** 2) + (b ** 2) == (c ** 2):
            print(a*b*c)
