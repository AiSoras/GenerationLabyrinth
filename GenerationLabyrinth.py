from turtle import *
import random
#from tkinter import *
def getNeighbours(mh,mw,cell,m):
    res=[]
    x=cell[0]
    y=cell[1]
    if (y+2)<mw and m[x][y+2][-1]!=1: #right
        res.append(m[x][y+2])
    if (x+2)<mh and m[x+2][y][-1]!=1: #down
        res.append(m[x+2][y])
    if (y-2)>0 and m[x][y-2][-1]!=1: #left
        res.append(m[x][y-2])
    if (x-2)>0 and m[x-2][y][-1]!=1: #up
        res.append(m[x-2][y])
    return res
def removeWall(cf,cs,m):
    x=(cf[0]-cs[0])//2
    y=(cf[1]-cs[1])//2
    m[cs[0]+x][cs[1]+y]=0
def drawturtle(m,mh,mw,d,a):
    hideturtle()
    pensize(5)
    speed(0)
    for i in range(mh):     
        if(not i%2):
            penup()
            setposition(0-a,-d*i+a)
            seth(0)
            pendown()
            for k in range(len(m[i][:-1])):
                if(m[i][k] and m[i][k+1]):
                    forward(d)
                else:
                    penup()
                    forward(d)
                    pendown()
        else:
            for t in range(0,mw,2):
                if(m[i][t]):
                    penup()
                    setposition(d*t-a,-d*(i-1)+a)
                    pendown()
                    seth(270)
                    forward(2*d)
def drawconsole(m,mh):
    for i in range(mh):
        if(i%2==0):
            t=['■■' if x  else '  ' for x in m[i]]
            print(''.join(x for x in t))
        else:
            t=['■■  ' if x else '    ' for x in m[i][::2]]
            print(''.join(x for x in t))
#def drawtk(m,mh):
#    root = Tk()
w0,h0=map(int, input("Vvedite razmernost labirinta: w,h\n>>>").strip().split(" "))
w=2*w0+1
h=2*h0+1
maze=[]
stackcurr=[] #Цепочка посещенных клеток
unvisitedcells=w0*h0 #Количество непосещенных клеток
for i in range(h):
    maze.append([])
    if (i%2==0):
        maze[i].extend([int(x) for x in '1'*w])
    else:
        for j in range(w):
            if(j%2==0):
                maze[i].append(1) #Стена
            else:
                maze[i].append([i,j,0]) #Непосещенная клетка
startcell=random.randrange(1,h,2)
currentcell=maze[startcell][1]
maze[startcell][0]=0
currentcell[-1]=1
unvisitedcells-=1
stackcurr.append(currentcell)
while (unvisitedcells):
    neigh=getNeighbours(h,w,currentcell,maze)
    if (neigh):
        randnum=random.randint(0,len(neigh)-1)
        neighbourcell=neigh[randnum]
        neighbourcell[-1]=1
        unvisitedcells-=1
        removeWall(neighbourcell,currentcell,maze)
        currentcell=neighbourcell
        stackcurr.append(neighbourcell)
    elif (stackcurr):
        stackcurr.pop()
        currentcell=stackcurr[-1] 
endcell=random.randrange(1,h,2)
maze[endcell][-1]=0
drawconsole(maze,h)
drawturtle(maze,h,w,15,400)