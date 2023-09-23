from copy import copy


def theorem_3(index):
    a = copy(index)
    for i in range(len(a)):
        a[i] = abs(a[i])
    B = max(a)
    an = a[len(a)-1]
    a.pop()
    A = max(a)
    r = 1/(1+B/(abs(a[0])))
    R = 1+(A/abs(an))
    return(r, R)

def theorem_4(index):
    b = copy(index)
    maximum = -1
    pos = 0
    if (b[len(b)-1]>0):
        for i in range(len(b)):
            if b[i] < 0:
                pos = i
                if (maximum <= abs(b[i])):
                    maximum = abs(b[i])
    R = 1+(maximum/b[len(b)-1])**(1/(len(b)-1-pos))
    return R

def theorem_5(index):
    c = copy(index)
    R = theorem_4(index)
    c.reverse()
    if(c[len(c)-1] <0):
        for i in range(len(c)):
            c[i] = -c[i]
    R1 = theorem_4(c)
    c = copy(index)
    for i in range(1, len(c)):
        if(i%2 !=0):
            c[i] = -c[i]
    if (c[len(c) - 1] < 0):
        for i in range(len(c)):
            c[i] = -c[i]
    R2 = theorem_4(c)
    c.reverse()
    if (c[len(c) - 1] < 0):
        for i in range(len(c)):
            c[i] = -c[i]
    R3 = theorem_4(c)
    return R, R1, R2, R3

#example
index = [-3, -7, 8, -5, 2, 1]
r, R = theorem_3(index)
print(r, R)
R = theorem_4(index)
print(R)
R, R1, R2, R3 = theorem_5(index)
print(R, R1, R2, R3)