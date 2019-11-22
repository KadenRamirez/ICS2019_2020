import cv2
import numpy as np

wireColor=(128,128,128)
notWireColor=(0,0,0)
electronColor=(0,255,255)
tailColor=(0,128,255)

wire=1
notWire=0
electron=3
tail=2


def show(img, title="image", wait=30):
    d=np.max(img.shape)
    h,w=img.shape[:2]
    unitSize=1200//d
    resized = cv2.resize(np.uint8(img), (unitSize*w,unitSize*h), interpolation = cv2.INTER_AREA)
    cv2.imshow(title, resized)
    cv2.waitKey(wait) # 0 means wait for key input. postive value waits for that many milliseconds
    
def showCA(ca, wait=0):
    h,w = ca.shape[:2]
    out = np.zeros((h,w,3))

    out[ca==wire]=wireColor
    out[ca==notWire]=notWireColor
    out[ca==electron]=electronColor
    out[ca==tail]=tailColor
    show(out, wait=wait)
    
def load(filename):
    img=cv2.imread(filename)
    h,w = img.shape[:2]
    out = np.zeros((h,w))
    out[img[:,:,1]<100]=notWire
    out[img[:,:,1]>150]=electron
    out[np.logical_and(img[:,:,1]<150,img[:,:,2]>150)]=tail
    out[np.logical_and(img[:,:,1]<150,img[:,:,0]>100)]=wire
    return out
    
    

def iterate(world):
    newWorld=world*1
    kernel=np.int16([[1,1,1],
                     [1,0,1],
                     [1,1,1]])
    whereTheElectronsAre=np.int16(world==electron)
    neighborCount=cv2.filter2D(whereTheElectronsAre,-1,kernel,borderType=cv2.BORDER_CONSTANT)
    newWorld[world==notWire]=notWire
    newWorld[world==electron]=tail
    newWorld[world==tail]=wire
    newWorld[world==wire]=wire
    newWorld[np.logical_and(np.logical_and(world==wire,1<=neighborCount),neighborCount<=2)]=electron
    return newWorld



world=np.array([[0,0,0,0,0],
                [0,0,0,0,0],
                [1,1,1,3,0],
                [0,0,0,0,1],
                [0,0,0,0,1]])

world=load("WireWorldWorld.bmp")
fps=1000
while True:
    showCA(world,1000//fps)
    world=iterate(world)
    #print(i)


# ~ public class Rectange
# ~ {
    # ~ //INSTANCE VARIABLES(S): THINGS TO REMEMBER
    # ~ private int w;
    # ~ int h;
    
    # ~ //CONSTRUCTOR(S):FILL IN INSTANCE VARIABLES
    # ~ public Rectangel(double w, double h)
    # ~ {
        # ~ this.w=w;
        # ~ this.h=h;
    # ~ }
    # ~ //METHOD(S)/FUNCTIONS(S): THINGS YOU CAN DO
    # ~ public int area(double factor)
    # ~ {
        # ~ w*=factor;
        # ~ h*=factor;
    # ~ }
    
# ~ }

# ~ class Rectangle:
    # ~ def__init__(self,w,h):
        # ~ self.w=w
        # ~ self.h=h
    # ~ def area(self):
        # ~ self.w*self.h
    # ~ def scale(self,factor):
        # ~ self.w*=factor
        # ~ self.h*=factor

# ~ reggie = Rectangle(5,6)
# ~ print(reggie.area())
# ~ reggie.scale(5)
    
    
