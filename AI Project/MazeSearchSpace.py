from pyamaze import maze,COLOR,agent
def DFS(m):
        start=(m.rows,m.cols)
        explored=[start]
        frontier=[start]
        dfspath={}
        dSearch=[]
        while len(frontier)>0:
                CurrCell=frontier.pop()
                dSearch.append(CurrCell)
                if CurrCell==m._goal:
                    break
                poss=0
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
                        poss+=1
                        explored.append(childCell)
                        frontier.append(childCell)
                        dfspath[childCell]=CurrCell
                    if poss>1:
                         m.markCells.append(CurrCell)
        fwdPath={}
        cell=m._goal
        while cell!=start:
            fwdPath[dfspath[cell]]=cell
            cell=dfspath[cell]
        return dSearch,fwdPath


m=maze(5,5)
m.CreateMaze(theme=COLOR.dark)
dSearch,path=DFS(m)
a=agent(m,footprints=True,shape='Square',color='green') 
b=agent(m,footprints=True,color='yellow')
m.tracePath({a:dSearch},showMarked=True)
m.tracePath({b:path})


m.run()