import math
def zy1(h,w):
    t1=w/h**2
    print('%.1f'%t1)

zy1(1.76,74)


def zy2(w,t1):
    h=math.sqrt(w/t1)*100
    print('张燕燕的身高是%.1fcm'%h)

zy2(43.3,18.6)


def zy3(h,t1):
    w=h**2*t1
    print('张燕燕体重%.1fkg合适'%w)

zy3(1.76,21.25)

