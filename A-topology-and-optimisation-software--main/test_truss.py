from Design import design
from view import design_view
from main import optimizer
import time
from boundary import BC
#from loads import load
def run(nelx,nely,lod,bound):
    s=design(nelx,nely)
    c=s.solid(.4)
    #time.sleep(5)
    design_view(c,nelx,nely)
    #load1=load.load1(nelx,nely)
    s=BC.fixed(nelx,nely)
    p=optimizer(1e-9,1.0,.4,nelx,nely,c,lod,bound)
