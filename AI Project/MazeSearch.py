from pyamaze import maze,COLOR,agent,textLabel
from queue import PriorityQueue
def DFS(m):
        start=(m.rows,m.cols)
        explored=[start]
        Uncharted=[start]
        dfspath={}
        while len(Uncharted)>0:
                CurrCell=Uncharted.pop()
                if CurrCell==(1,1):
                    break
                for d in 'ESNW':
                    if m.maze_map[CurrCell][d]==True:
                        if d=='E':
                            childCell=(CurrCell[0],CurrCell[1]+1)
                        elif d=='W':
                            childCell=(CurrCell[0],CurrCell[1]-1) 
                        elif d=='S':
                            childCell=(CurrCell[0]+1,CurrCell[1])
                        elif d=='N':
                            childCell=(CurrCell[0]-1,CurrCell[1])
                        if childCell in explored:
                             continue
                        explored.append(childCell)
                        Uncharted.append(childCell)
                        dfspath[childCell]=CurrCell
        fwdPath={}
        cell=(1,1)
        while cell!=start:
            fwdPath[dfspath[cell]]=cell
            cell=dfspath[cell]
        return fwdPath
def h(cell1,cell2):
    x1,y1=cell1
    x2,y2=cell2

    return abs(x1-x2) + abs(y1-y2)

def aStar(m):
    start=(m.rows,m.cols)
    g_score={cell:float('inf') for cell in m.grid}
    g_score[start]=0
    f_score={cell:float('inf') for cell in m.grid}
    f_score[start]=h(start,(1,1))

    open=PriorityQueue()
    open.put((h(start,(1,1)),h(start,(1,1)),start))
    aPath={}
    while not open.empty():
        currCell=open.get()[2]
        if currCell==(1,1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                if d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                if d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if d=='S':
                    childCell=(currCell[0]+1,currCell[1])

                temp_g_score=g_score[currCell]+1
                temp_f_score=temp_g_score+h(childCell,(1,1))

                if temp_f_score < f_score[childCell]:
                    g_score[childCell]= temp_g_score
                    f_score[childCell]= temp_f_score
                    open.put((temp_f_score,h(childCell,(1,1)),childCell))
                    aPath[childCell]=currCell
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[aPath[cell]]=cell
        cell=aPath[cell]
    return fwdPath
def BFS(m):
    start=(m.rows,m.cols)
    Uncharted=[start]
    explored=[start]
    bfsPath={}
    while len(Uncharted)>0:
        currCell=Uncharted.pop(0)
        if currCell==(1,1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                if childCell in explored:
                    continue
                Uncharted.append(childCell)
                explored.append(childCell)
                bfsPath[childCell]=currCell
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    return fwdPath
               
                             

if __name__=='__main__':
    m=maze(15,15)
    m.CreateMaze(theme=COLOR.red,loopPercent=100,loadMaze='maze--2023-10-29--16-26-55.csv')
    #REMOVE/ADD HASHTAGs ACCORDINGLY TO USE THE SPECIFIED SEARCH METHOD 
    path=DFS(m)
    #path=aStar(m)
    #path=BFS(m)   
    a=agent(m,footprints=True) 
    m.tracePath({a:path})
    l=textLabel(m,'Shortest Length to Goal',len(path)+1)

    m.run()