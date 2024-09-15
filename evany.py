#This program will put your initals and your significant other's initial in a heart

a1 = "   0   "
a2 = "  0 0  "
a3 = " 0   0 "
a4 = " 00000 "
a5 = " 0   0 "
#-------
b1 = " 0000  "
b2 = " 0   0 "
b3 = " 0000  "
b4 = " 0   0 "
b5 = " 0000  "
#-------
c1 = " +000  "
c2 = " 0   0 "
c3 = " 0     "
c4 = " 0   0 "
c5 = "  000  "
#-------
d1 = " 0000  "
d2 = " 0   0 "
d3 = " 0   0 "
d4 = " 0   0 "
d5 = " 0000  "
#-------
e1 = " 00000 "
e2 = " 0     "
e3 = " 0000  "
e4 = " 0     "
e5 = " 00000 "
#-------
f1 = " 00000 "
f2 = " 0     "
f3 = " 0000  "
f4 = " 0     "
f5 = " 0     "
#-------
g1 = "  0000 "
g2 = " 0     "
g3 = " 0  00 "
g4 = " 0    0"
g5 = "  0000 "
#-------
h1 = " 0   0 "
h2 = " 0   0 "
h3 = " 00000 "
h4 = " 0   0 "
h5 = " 0   0 "
#-------
i1 = " 00000 "
i2 = "   0   "
i3 = "   0   "
i4 = "   0   "
i5 = " 00000 "
#-------
j1 = "  00000"
j2 = "    0  "
j3 = "    0  "
j4 = " 0  0  "
j5 = " 000   "
#-------
k1 = " 0   0 "
k2 = " 0   0 "
k3 = " 0000  "
k4 = " 0   0 "
k5 = " 0   0 "
#-------
l1 = " 0     "
l2 = " 0     "
l3 = " 0     "
l4 = " 0     "
l5 = " 00000 "
#-------
m1 = " 0   0 "
m2 = " 00 00 "
m3 = " 0 0 0 "
m4 = " 0   0 "
m5 = " 0   0 "
#-------
n1 = " 0   0 "
n2 = " 00  0 "
n3 = " 0 0 0 "
n4 = " 0  00 "
n5 = " 0   0 "
#-------
o1 = "  000  "
o2 = " 0   0 "
o3 = " 0   0 "
o4 = " 0   0 "
o5 = "  000  "
#-------
p1 = " 0000  "
p2 = " 0   0 "
p3 = " 0000  "
p4 = " 0     "
p5 = " 0     "
#-------
q1 = " 000   "
q2 = "0   0  "
q3 = "0 0 0  "
q4 = "0  00  "
q5 = " 00000 "
#-------
r1 = " 0000  "
r2 = " 0   0 "
r3 = " 0000  "
r4 = " 0  0  "
r5 = " 0   0 "
#-------
s1 = "  0000 "
s2 = " 0     "
s3 = "  000  "
s4 = "     0 "
s5 = " 0000  "
#-------
t1 = " 00000 "
t2 = "   0   "
t3 = "   0   "
t4 = "   0   "
t5 = "   0   "
#-------
u1 = " 0   0 "
u2 = " 0   0 "
u3 = " 0   0 "
u4 = " 0   0 "
u5 = "  000  "
#-------
v1 = " 0   0 "
v2 = " 0   0 "
v3 = " 0   0 "
v4 = "  0 0  "
v5 = "   0   "
#-------
w1 = "0     0"
w2 = "0     0"
w3 = "0  0  0"
w4 = "0 0 0 0"
w5 = " 0   0 "
#-------
x1 = " 0   0 "
x2 = "  0 0  "
x3 = "   0   "
x4 = "  0 0  "
x5 = " 0   0 "
#-------
y1 = " 0   0 "
y2 = "  0 0  "
y3 = "   0   "
y4 = "   0   "
y5 = "   0   "
#-------
z1 = " 00000 "
z2 = "    0  "
z3 = "   0   "
z4 = "  0    "
z5 = " 00000 "

init1 = input("What is your first initial? ")
if init1 == "can you give me a blowjob?" or init1 == "Can you give me a blowjob?":
    print("Yes! Hawk tuah!")
while len(init1) != 1 or not init1.isalpha():
    print("That is not an initial. Please try again.")
    init1 = input("What is your first initial? ")
if init1 == "A" or init1 == "a":
    row11 = a1
    row12 = a2
    row13 = a3
    row14 = a4
    row15 = a5
elif init1 == "B" or init1 == "b":
    row11 = b1
    row12 = b2
    row13 = b3
    row14 = b4
    row15 = b5
elif init1 == "C" or init1 == "c":
    row11 = c1
    row12 = c2
    row13 = c3
    row14 = c4
    row15 = c5
elif init1 == "D" or init1 == "d":
    row11 = d1
    row12 = d2
    row13 = d3
    row14 = d4
    row15 = d5
elif init1 == "E" or init1 == "e":
    row11 = e1
    row12 = e2
    row13 = e3
    row14 = e4
    row15 = e5
elif init1 == "F" or init1 == "f":
    row11 = f1
    row12 = f2
    row13 = f3
    row14 = f4
    row15 = f5
elif init1 == "G" or init1 == "g":
    row11 = g1
    row12 = g2
    row13 = g3
    row14 = g4
    row15 = g5
elif init1 == "H" or init1 == "h":
    row11 = h1
    row12 = h2
    row13 = h3
    row14 = h4
    row15 = h5
elif init1 == "I" or init1 == "i":
    row11 = i1
    row12 = i2
    row13 = i3
    row14 = i4
    row15 = i5
elif init1 == "J" or init1 == "j":
    row11 = j1
    row12 = j2
    row13 = j3
    row14 = j4
    row15 = j5
elif init1 == "K" or init1 == "k":
    row11 = k1
    row12 = k2
    row13 = k3
    row14 = k4
    row15 = k5
elif init1 == "L" or init1 == "l":
    row11 = l1
    row12 = l2
    row13 = l3
    row14 = l4
    row15 = l5
elif init1 == "M" or init1 == "m":
    row11 = m1
    row12 = m2
    row13 = m3
    row14 = m4
    row15 = m5
elif init1 == "N" or init1 == "n":
    row11 = n1
    row12 = n2
    row13 = n3
    row14 = n4
    row15 = n5
elif init1 == "O" or init1 == "o":
    row11 = o1
    row12 = o2
    row13 = o3
    row14 = o4
    row15 = o5
elif init1 == "P" or init1 == "p":
    row11 = p1
    row12 = p2
    row13 = p3
    row14 = p4
    row15 = p5
elif init1 == "Q" or init1 == "q":
    row11 = q1
    row12 = q2
    row13 = q3
    row14 = q4
    row15 = q5
elif init1 == "R" or init1 == "r":
    row11 = r1
    row12 = r2
    row13 = r3
    row14 = r4
    row15 = r5
elif init1 == "S" or init1 == "s":
    row11 = s1
    row12 = s2
    row13 = s3
    row14 = s4
    row15 = s5
elif init1 == "T" or init1 == "t":
    row11 = t1
    row12 = t2
    row13 = t3
    row14 = t4
    row15 = t5
elif init1 == "U" or init1 == "u":
    row11 = u1
    row12 = u2
    row13 = u3
    row14 = u4
    row15 = u5
elif init1 == "V" or init1 == "v":
    row11 = v1
    row12 = v2
    row13 = v3
    row14 = v4
    row15 = v5
elif init1 == "W" or init1 == "w":
    row11 = w1
    row12 = w2
    row13 = w3
    row14 = w4
    row15 = w5
elif init1 == "X" or init1 == "x":
    row11 = x1
    row12 = x2
    row13 = x3
    row14 = x4
    row15 = x5
elif init1 == "Y" or init1 == "y":
    row11 = y1
    row12 = y2
    row13 = y3
    row14 = y4
    row15 = y5
elif init1 == "Z" or init1 == "z":
    row11 = z1
    row12 = z2
    row13 = z3
    row14 = z4
    row15 = z5

init2 = input("What is the first initial of a loved one? ")
while len(init2) != 1 or not init2.isalpha():
    print("That is not an initial. Please try again.")
    init2 = input("What is the first initial of a loved one? ")
if init2 == "A" or init2 == "a":
    row21 = a1
    row22 = a2
    row23 = a3
    row24 = a4
    row25 = a5
elif init2 == "B" or init2 == "b":
    row21 = b1
    row22 = b2
    row23 = b3
    row24 = b4
    row25 = b5
elif init2 == "C" or init2 == "c":
    row21 = c1
    row22 = c2
    row23 = c3
    row24 = c4
    row25 = c5
elif init2 == "D" or init2 == "d":
    row21 = d1
    row22 = d2
    row23 = d3
    row24 = d4
    row25 = d5
elif init2 == "E" or init2 == "e":
    row21 = e1
    row22 = e2
    row23 = e3
    row24 = e4
    row25 = e5
elif init2 == "F" or init2 == "f":
    row21 = f1
    row22 = f2
    row23 = f3
    row24 = f4
    row25 = f5
elif init2 == "G" or init2 == "g":
    row21 = g1
    row22 = g2
    row23 = g3
    row24 = g4
    row25 = g5
elif init2 == "H" or init2 == "h":
    row21 = h1
    row22 = h2
    row23 = h3
    row24 = h4
    row25 = h5
elif init2 == "I" or init2 == "i":
    row21 = i1
    row22 = i2
    row23 = i3
    row24 = i4
    row25 = i5
elif init2 == "J" or init2 == "j":
    row21 = j1
    row22 = j2
    row23 = j3
    row24 = j4
    row25 = j5
elif init2 == "K" or init2 == "k":
    row21 = k1
    row22 = k2
    row23 = k3
    row24 = k4
    row25 = k5
elif init2 == "L" or init2 == "l":
    row21 = l1
    row22 = l2
    row23 = l3
    row24 = l4
    row25 = l5
elif init2 == "M" or init2 == "m":
    row21 = m1
    row22 = m2
    row23 = m3
    row24 = m4
    row25 = m5
elif init2 == "N" or init2 == "n":
    row21 = n1
    row22 = n2
    row23 = n3
    row24 = n4
    row25 = n5
elif init2 == "O" or init2 == "o":
    row21 = o1
    row22 = o2
    row23 = o3
    row24 = o4
    row25 = o5
elif init2 == "P" or init2 == "p":
    row21 = p1
    row22 = p2
    row23 = p3
    row24 = p4
    row25 = p5
elif init2 == "Q" or init2 == "q":
    row21 = q1
    row22 = q2
    row23 = q3
    row24 = q4
    row25 = q5
elif init2 == "R" or init2 == "r":
    row21 = r1
    row22 = r2
    row23 = r3
    row24 = r4
    row25 = r5
elif init2 == "S" or init2 == "s":
    row21 = s1
    row22 = s2
    row23 = s3
    row24 = s4
    row25 = s5
elif init2 == "T" or init2 == "t":
    row21 = t1
    row22 = t2
    row23 = t3
    row24 = t4
    row25 = t5
elif init2 == "U" or init2 == "u":
    row21 = u1
    row22 = u2
    row23 = u3
    row24 = u4
    row25 = u5
elif init2 == "V" or init2 == "v":
    row21 = v1
    row22 = v2
    row23 = v3
    row24 = v4
    row25 = v5
elif init2 == "W" or init2 == "w":
    row21 = w1
    row22 = w2
    row23 = w3
    row24 = w4
    row25 = w5
elif init2 == "X" or init2 == "x":
    row21 = x1
    row22 = x2
    row23 = x3
    row24 = x4
    row25 = x5
elif init2 == "Y" or init2 == "y":
    row21 = y1
    row22 = y2
    row23 = y3
    row24 = y4
    row25 = y5
elif init2 == "Z" or init2 == "z":
    row21 = z1
    row22 = z2
    row23 = z3
    row24 = z4
    row25 = z5





















print("                                                                ")
print("            000000000                    00000000               ")
print("         00           000           0000          00            ")
print("        0                00       00                0           ")
print("       0                   00   00                   0          ")
print("      0                      000                      0         ")
print("      0                                               0         ")
print("      0                                               0         ")
print(f"      0        {row11}        0        {row21}        0         ")
print(f"      0        {row12}        0        {row22}        0         ")
print(f"       0       {row13}    000000000    {row23}       0          ")
print(f"        00     {row14}        0        {row24}     00           ")
print(f"          00   {row15}        0        {row25}   00             ")
print("            00                                 00               ")
print("              00                             00                 ")
print("                00                         00                   ")
print("                  00                     00                     ")
print("                    00                 00                       ")
print("                      00             00                         ")
print("                        00         00                           ")
print("                          00     00                             ")
print("                            0   0                               ")
print("                             0 0                                ")
print("                              0                                 ")


if init1 == "e" or init1 == "E":
    if init2 == "j" or init2 == "J":
        print("I love you Evany")
elif init1 == "j" or init1 == "J":
    if init2 == "e" or init2 == "E":
        print("I love you Evany")