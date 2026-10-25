import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
def build_graph(rows, cols, blocked):
    g={}
    for r in range(rows):
        for c in range(cols):
            if (r,c) in blocked: continue
            nb=[]
            if r>0 and (r-1,c) not in blocked: nb.append((r-1,c))
            if r<rows-1 and (r+1,c) not in blocked: nb.append((r+1,c))
            if c>0 and (r,c-1) not in blocked: nb.append((r,c-1))
            if c<cols-1 and (r,c+1) not in blocked: nb.append((r,c+1))
            g[(r,c)]=nb
    return g
def bfs(pos,dest,blocked,rows=4,cols=4,dfs=False,trace=False):
    g=build_graph(rows,cols,blocked)
    if pos not in g or dest not in g: return []
    prev={pos:None}; tv=[pos]; log=[]
    while tv:
        cur=tv.pop() if dfs else tv.pop(0)
        if cur==dest: break
        new=[]
        for n in g[cur]:
            if n not in prev:
                prev[n]=cur; tv.append(n); new.append(n)
        log.append((cur,new,list(tv)))
    if dest not in prev: return []
    path=[]; c=dest
    while c!=pos: path.append(c); c=prev[c]
    path.reverse()
    return (path,log,prev) if trace else path
if __name__=='__main__':
    print('bfs open 0,0->3,3',bfs((0,0),(3,3),[]))
    print('dfs open',bfs((0,0),(3,3),[],dfs=True))
    p,log,prev=bfs((0,0),(2,2),[(1,1)],3,3,trace=True); print(p); [print(x) for x in log]
    # run1
    sim=[(2,0),(2,2)]; B=[]; pos=(0,0); dest=(3,3); driven=[(0,0)]; reroutes=[]
    path=bfs(pos,dest,B); print('plan',path)
    while True:
        rer=False
        for nxt in path:
            if nxt in sim:
                B.append(nxt); reroutes.append((pos,nxt)); path=bfs(pos,dest,B); print('replan at',pos,'blocked',nxt,path); rer=True; break
            pos=nxt; driven.append(pos)
        if not rer: break
    print('run1 driven',driven,len(driven)-1,'reroutes',len(reroutes))
    print('run2',bfs((0,0),(3,3),sim))
