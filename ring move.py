Web VPython 3.2

def move(obj) : 
    k = keysdown()
    if 'right' in k : 
        obj.pos.x += 0.05
    if 'left' in k:
        obj.pos.x -= 0.05
    if 'down' in k: 
        obj.pos.y -= 0.05
    if 'up' in k:
        obj.pos.y += 0.05
    if 'z' in k : 
        obj.pos.z += 0.05
    if 'x' in k : 
        obj.pos.z -= 0.05


colors = [color.red, color.orange, color.yellow, color.green, color.blue, color.magenta, color.purple]
ball = sphere(color = color.cyan, radius = 0.2, emissive = True)
rings = []
for i in range(7) : 
    rings.append(ring(pos = vec(i,0,0), color = colors[0+i]))

while True :
    rate(100)
    move(ball)
    for i in range(7):
        if mag(ball.pos - rings[i].pos) < 0.5 :
            rings[i].color = ball.color
        else :
            rings[i].color = colors[i]
    
