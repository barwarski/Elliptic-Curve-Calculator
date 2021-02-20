# 1.Funktion, die aufgerufen wird
def start(a,b,p,x1,y1,x2,y2):
    if bedingung_test(a,b,p):
        return ("Def. 9.1 nicht erfüllt. Ungeeignet")
    elif x1 == x2 and y1 == y2:
        return (verdoppelung(a,p,x1,y2,x2))
    elif x1 == y1 == 0: #wenn Punkt im Unendlichen als Punkt gegeben wird
        return ("Ergebnis: (" + str(x2) + "," + str(y2) + ")")
    elif y2 == x2 == 0:
        return ("Ergebnis: (" + str(x1) + "," + str(y1) + ")")
    #elif x1 != x2 and y1 != y2:
    #    print(addition(p,x1,y1,x2,y2))
    elif x1 != x2 or y1 != y2:
        return (addition(p, x1, y1, x2, y2))
    else:
        return ("Error")
#Punktverdoppelung
def verdoppelung(a,p,x1,y1,x2):
    ggT = eea(2*y1,p)
    s = ((3*x1**2+a)*ggT)%p ########
    x3 = (s**2-x1-x2)%p
    y3 = (s*(x1-x3)-y1)%p
    return "Ergebnis: (" + str(x3) + "," + str(y3) + ")"
#Punktaddition
def addition(p,x1,y1,x2,y2):
    ggT = eea((x2-x1),p) ## hier wird die multiplikative inverse zuerst berechnet um ohne probleme zügig weiterrechen zukönnen
    s = ((y2-y1)*ggT)%p
    x3 = (s ** 2 - x1 - x2) % p
    y3 = (s * (x1 - x3) - y1) % p
    return "Ergebnis: (" + str(x3) + "," + str(y3) + ")"
# gibt true aus, wenn 4.a^3+27b^2=0 gilt, oder p prim ist
def bedingung_test(a,b,p):
    bedingung = not((4*a**3+27*b**2)%p == 0)
    #primzahltest
    primTest = prim_test(p)
    if bedingung == False or primTest == False:
        return True
    else:
        return False
# berechnet erweitereten euklidischen Algorithmus bzw. die multiplikative Inverse
def eea(a,b):
    u, v, s, t = 1, 0, 0, 1
    while b != 0:
        q = a // b
        a, b = b, a - q * b
        u, s = s, u - q * s
        v, t = t, v - q * t
    return u
# wenn p keine Primuahl ist dann wird False zurückgegeben
def prim_test(p):
    prim = True
    for counter in range(2,p-1):
        if (p%counter) == 0:
            prim = False
            break
    return prim

# -------------------------------------- #

#start(a,b,p,x1,y1,x2,y2)
#start(2,2,17,5,1,5,1)
