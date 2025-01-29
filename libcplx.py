import math

def print_hi(name):
    print(f'Hi, {name}')

def divicplx(a,b):
    num1 = a[0] * b[0] - a[1] * b[1]
    num2 = a[1] * b[0] - a[1] * b[1]
    dem = b[0] ** 2 - b[1]
    return num1 / dem, num2 / dem

def multicplx(c1,c2):
    p1 = c1[0] * c2[0] - c1[1] * c2[1]
    p2 = c2[0] * c1[1] + c2[1] * c1[0]
    return(p1,p2)

def sumacplx(c1,c2):
    parteR = c1[0] + c2[0]
    parteI = c1[1] + c2[1]
    return parteR,parteI

def restacplx(c1,c2):
    parteR = c1[0] - c2[0]
    parteI = c1[1] - c2[1]
    return parteR,parteI

def modulocplx(c1):
    modu1 = ((c1[0] ** 2 + c1[1] ** 2) ** 0.5)
    return modu1

def conjugacplx(c1,c2):
    con1 = - c1[1]
    con2 = - c2[1]
    return (c1[0],con1),(c2[0],con2)

def polarcplx(c1):
    r1 = modulocplx(c1)
    a = c1[0]
    b = c1[1]
    if a > 0 and b > 0:
        a1 = math.atan(b/a)
    elif a < 0 and b < 0:
        a1 = math.atan(b/a) + 180
    elif b > 0 and a < 0:
        a0 = math.atan(b/a) 
        a1 = 180 - a0
    elif b < 0 and a > 0:
        a0 = math.atan(b/a)
        a1 = 360 -a0
    return (r1,a1)

def cartesicplx(c1):
    r,g = polarcplx(c1)
    x = r * math.cos(g)
    y = r * math.sin(g)
    return(x,y)

def fasecplx(c1):
    parteR = c1[0]
    parteI = c1[1]
    fase = math.atan2(parteI,parteR)
    return fase

if __name__ == '__main__':
    print_hi('Pycharm')
    print(sumacplx((3,2),(-5,5.2)))
    print(restacplx((3,2),(-5,5.2)))
    print(multicplx((3,2),(-5,5.2)))
    print(divicplx((3,2),(-5,5.2)))
    print(modulocplx((3,2)))
    print(conjugacplx((3,2),(-5,5.2)))
    print(polarcplx((3,2)))
    print(cartesicplx((3,2)))
    print(fasecplx((3,2)))
