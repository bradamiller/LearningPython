import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import math
CX,CY,R=215,210,128; S=0.42; SENS=60*S; TW=10; SPOT=5
def reading(sx,sy):
    d=math.hypot(sx-CX,sy-CY)-R      # signed, + outside
    lo,hi=d-SPOT,d+SPOT
    ov=max(0,min(hi,TW/2)-max(lo,-TW/2))/(2*SPOT)
    return 0.2+0.6*ov
def sim(Kp,T=12.0,dt=0.01,K=6.0,V=60.0,tau=0.22,delay=0.08,start_ang=90):
    # start at bottom of circle, outside edge, heading clockwise (screen): at bottom moving left
    a=math.radians(start_ang)
    sxp,syp=CX+(R+TW/2)*math.cos(a), CY+(R+TW/2)*math.sin(a)   # sensor point on outer edge
    h=math.degrees(math.atan2(-math.sin(a),-math.cos(a)))       # placeholder
    # tangent for clockwise screen motion at angle a: direction (-sin a, cos a)?? check: screen cw at bottom (a=90) moves left: (-1,0)
    tx,ty=-math.sin(a)*-1, math.cos(a)*1
    tx,ty=-1*math.sin(a+0)*1, 0
    tx,ty=-math.sin(a)*1, math.cos(a)*-1   # a=90 -> (-1,0)
    th=math.atan2(ty,tx)                    # heading angle in math screen coords
    x,y=sxp-SENS*tx, syp-SENS*ty
    om=0.0; buf=[0.0]*int(delay/dt+1); out=[]; t=0
    while t<T:
        sx,sy=x+SENS*math.cos(th), y+SENS*math.sin(th)
        r=reading(sx,sy); e=0.5-r; c=Kp*e
        buf.append(c); cd=buf.pop(0)
        om+= (K*cd-om)*dt/tau            # positive c -> turn right = clockwise on screen = +theta (y down)
        th+=om*dt; x+=V*math.cos(th)*dt; y+=V*math.sin(th)*dt
        out.append((t,x,y,math.degrees(th)+90,r,e,c)); t+=dt
    return out
if __name__=='__main__':
    import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
    fig,ax=plt.subplots(1,3,figsize=(15,5))
    for i,kp in enumerate([0.2,0.5,1.0]):
        o=sim(kp); ax[i].plot([p[1] for p in o],[p[2] for p in o]); 
        c=plt.Circle((CX,CY),R,fill=False,lw=4,color='k'); ax[i].add_patch(c); ax[i].set_aspect('equal'); ax[i].invert_yaxis(); ax[i].set_title(str(kp)); ax[i].set_xlim(0,430); ax[i].set_ylim(420,0)
    plt.savefig(OUTDIR+'kp.png',dpi=60)
