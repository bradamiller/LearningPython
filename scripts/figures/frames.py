import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import OUTDIR, ROBOT_SRC, REPO
import sys
from playwright.sync_api import sync_playwright
from PIL import Image
f=sys.argv[1]; ts=[float(x) for x in sys.argv[2:]]
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':680,'height':380})
    pg.goto('file://'+f); ims=[]
    for t in ts:
        pg.evaluate(f"(()=>{{const s=document.querySelector('svg'); s.pauseAnimations(); s.setCurrentTime({t});}})()")
        pg.wait_for_timeout(150); pg.screenshot(path=OUTDIR+'fr.png'); ims.append(Image.open(OUTDIR+'fr.png').resize((340,190)))
    W=680; rows=(len(ims)+1)//2; out=Image.new('RGB',(W,190*rows),'white')
    for i,im in enumerate(ims): out.paste(im,((i%2)*340,(i//2)*190))
    out.save(OUTDIR+'frames.png')
