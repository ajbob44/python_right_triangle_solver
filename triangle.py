from math import cos, sin, tan, acos, asin, atan, radians, degrees
import turtle as t
t = t.Turtle()
while True:
    h = input('h:')
    a = input('a:')
    o = input('o:')
    pa = input('angle:')
    if h !='':
        h=float(h)
    if a !='':
        a=float(a)
    if o !='':
        o=float(o)
    if pa !='':
        float(pa)
    oa = 0
    while h =='' or a =='' or o =='' or pa =='':
        if h =='' :
            if a =='' :
                if o =='' :
                    print('to little info')
                else:
                    if pa !='' :
                        h = sin(radians(pa))
                        h = o/h
                        a = tan(radians(pa))
                        a = o/a
                    else:
                        print('to little info')
            else:
                if o !='' :
                    h = a**2 + o**2
                    h = h**0.5
                    pa = degrees(atan(o/a))
                elif pa !='' :
                    h = cos(radians(pa))
                    h = a/h
                    o = tan(radians(pa))
                    o = o * a
                else:
                    print('to little info')
        elif a !='':
            o = h**2 - a**2
            o = o**0.5
            pa = degrees(acos(a/h))
        elif o !='':
            a = h**2 - o**2
            a = a**0.5
            pa = degrees(asin(o/h))
    oa = 90 - pa
    print('a = ', a, '\no = ', o, '\nh = ', h, '\npa = ', pa, '\noa = ', oa) 
    c = 300/h
    t.forward(a*c)
    t.left(180 - pa)
    t.forward(300)
    t.left(180 - oa)
    t.forward(o*c)
    t.left(90)
