pi=0
i=0
h=[]
def setup():
    size(600,400)
    background(0)
    
def S(n):
    pi=0
    for i in range(n):
        k=2*i+1
        pi+= 4*(pow(-1,i)/k)
    return pi
        
def draw(): 
    background(0)
    global pi, i, h
    
    k=2*i+1
    pi+= 4*(pow(-1,i)/k)
    
    h.extend([pi])

    piY=map(PI,2,4,0, height)
    line(0,piY,width, piY)
    stroke(255)
    noFill()
    beginShape()
    spaceing=width/len(h)
    for j in range(len(h)):
        x=j*spaceing
        y=map(h[j],2,4,0,height)
        vertex(x,y)
    endShape()
    i+=1
       
    
