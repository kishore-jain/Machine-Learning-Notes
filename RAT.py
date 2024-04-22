def rat1():
    f = open('Right_Angle_Triangle.txt','w+')
    f.write('RIGHT ANGLE TRIANGLE :')
    f.write('\n')
    f.write('----------------------')
    f.write('\n')
    f.write('\n')
    f.write('1.right angle triangle :')
    f.write('\n--------------------\n')
    for i in range(1,6):
        for j in range(0,i):
            f.write(str(i))
        f.write('\n')
    f.close()

def rat2():
    f = open('Right_Angle_Triangle.txt','a+')
    f.write('\n')
    f.write('2.right angle triangle coulmn printing :')
    f.write('\n------------------------------------\n')
    for i in range(1,7):
        for j in range(1,i):
            f.write(str(j))
        f.write('\n')
    f.close()


def irat1():
    f = open('Right_Angle_Triangle.txt','a+')
    f.write('\n')
    f.write('3.inverse right angle triangle :')
    f.write('\n----------------------------\n')
    for i in range(5,0,-1):
        for j in range(0,i):
            f.write(str(i))
        f.write('\n')
    f.close()

def irat2():
    f = open('Right_Angle_Triangle.txt','a+')
    f.write('\n')
    f.write('4.inverse right angle triangle column printing :')
    f.write('\n-------------------------------------------\n')
    for i in range(6,1,-1):
        for j in range(1,i):
            f.write(str(j))
        f.write('\n')
    f.close()


if __name__=='__main__':
    rat1()
    rat2()
    irat1()
    irat2()
