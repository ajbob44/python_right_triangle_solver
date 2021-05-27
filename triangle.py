from math import cos, sin, tan, acos, asin, atan, radians, degrees
import turtle as t
h = input('h:')
a = input('a:')
o = input('o:')
pa = input('angle:')
oa = input('other angle:')
h = int(h)
a = int(a)
o = int(o)
pa = int(pa)
oa = int(oa)
while h ==0 or a ==0 or o ==0 or pa ==0 or oa ==0 :
    if h ==0 :
        if a ==0 :
            if o ==0 :
                print('to little info')
            else:
                if pa !=0 :
                    h = sin(radians(pa))
                    h = o/h
                elif oa !=0 :
                    h = cos(radians(oa))
                    h = o/h
        else:
            if o !=0 :
                h = a**2 + o**2
                h = h**0.5
            elif pa !=0 :
                h = cos(radians(pa))
                h = a/h
            elif oa !=0 :
                h = sin(radians(oa))
                h = a/h
    if a ==0 :
        if h !=0 :
            if o ==0 :
                if pa !=0 :
                    a = cos(radians(pa))
                    a = a * h
                elif oa !=0 :
                    a = sin(radians(oa))
                    a = a * h
            else:
                a = h**2 - o**2
                a = a**0.5
        else:
            if o !=0 :
                if pa !=0 :
                    a = tan(radians(pa))
                    a = o/a
                elif oa !=0 :
                    a = tan(radians(oa))
                    a = a * o
    if o==0 :
        if h ==0 :
            if a !=0 :
                if pa !=0 :
                    o = tan(radians(pa))
                    o = o * a
                elif oa !=0 :
                    o = tan(radians(oa))
                    o = a/o
        else:
            if pa !=0 :
                o = sin(radians(pa))
                o = o * h
            elif oa !=0 :
                o = cos(radians(oa))
                o = o * h
            if a !=0 :
                o = h**2 - a**2
                o = o**0.5
    if pa ==0 :
        if oa !=0 :
            pa = 90 - oa
        else:
            if h ==0 :
                if a !=0 :
                    if o !=0 :
                        pa = degrees(atan(o/a))
            else:
                if a !=0 :
                    pa = degrees(acos(a/h))
                elif o !=0 :
                    pa = degrees(asin(o/h))
    if oa ==0 :
        if pa !=0 :
            oa = 90 - pa
        else:
            if h ==0 :
                if a !=0 :
                    if o !=0 :
                        oa = degrees(atan(a/o))
            else:
                if a !=0 :
                    oa = degrees(asin(a/h))
                elif o !=0 :
                    oa = degrees(acos(o/h))
print('a = ', a, '\no = ', o, '\nh = ', h, '\npa = ', pa, '\noa = ', oa) 


t = t.Turtle()
t.forward(a)
t.left(180 - pa)
t.forward(h)
t.left(180 - oa)
t.forward(o)
input()