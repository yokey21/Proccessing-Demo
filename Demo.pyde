width = 480
height = 480

def setup():
    size(width, height)
    background(1,100,3)

def draw():
    if  mousePressed:
        fill(255,0,0)
        
    else:
        fill(255)
        noStroke()
        background(1,100,3)
    ellipse(width/2, height/2, 50, 50)

    
