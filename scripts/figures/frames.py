import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys
from playwright.sync_api import sync_playwright
from PIL import Image
f=sys.argv[1]; ts=[float(x) for x in sys.argv[2:]]
with sync_playwright() as p:
    import re
    m=re.search(r'viewBox="0 0 (\d+) (\d+)"',open(f).read()); W0,H0=int(m.group(1)),int(m.group(2))
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':W0,'height':H0})
    pg.goto('file://'+os.path.abspath(f)); ims=[]
    for t in ts:
        pg.evaluate(f"(()=>{{const s=document.querySelector('svg'); s.pauseAnimations(); s.setCurrentTime({t});}})()")
        pg.wait_for_timeout(150); pg.screenshot(path=OUTDIR+'fr.png'); ims.append(Image.open(OUTDIR+'fr.png').resize((W0//2,H0//2)))
    w,h=W0//2,H0//2; rows=(len(ims)+1)//2; out=Image.new('RGB',(2*w,h*rows),'white')
    for i,im in enumerate(ims): out.paste(im,((i%2)*w,(i//2)*h))
    out.save(OUTDIR+'frames.png')
