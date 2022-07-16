Web VPython 3.2

import random
c=1
box(color = color.green, size = vec(100,1,20))
ball = sphere(color = color.red, pos = vec(0,10,0))
ball.v = vec(0,0,0)
t = 0
b_list = []
a_list = []
o=0
for i in range(10) :
    x = random.randint(-40, 40)
    y = random.randint(1, 9)
    b_list.append(sphere(pos = vec(x,y,0)))
for i in range(5) :
    x = random.randint(-40, 40)
    y = random.randint(1, 9)
    a_list.append(sphere(color = vec(1,1,0), pos = vec(x,y,0)))
for i in range(1) :
    x = random.randint(-40, 40)
    y = random.randint(1, 9)
    bu = ring(radius = 3, color = vec(0,1,1), pos = vec(x,y,0))
t1 = label(text = 'point: 0', pos = vec(20,20,0))
while True : 
    rate(100)
    if t % 100 == 0 :
        label(text = 'time:'+str(t//100), pos = vec(-20,20,0))
    t = t + 1
    ball.pos = ball.pos + ball.v * 0.01
    k = keysdown()
    if 'right' in k :
        ball.v.x += 0.1*c
    if 'left' in k :
        ball.v.x -= 0.1*c
    if 'up' in k :
        ball.v.y += 0.1*c
    if 'down' in k :
        ball.v.y -= 0.1*c
    if ball.pos.y <= 1.5 : 
        ball.v.y = -ball.v.y
    else :
        ball.v.y = ball.v.y + -9.8 * 0.01
    for i in range(10) :    
        if mag(ball.pos - b_list[i].pos) <= 2 :
            b_list[i].color = color.red
            ball.v.y = -ball.v.y       
    cnt = 0
    for i in range (10) :
        if b_list[i].color == color.red :
            cnt += 1
    t1.text = 'point: '+cnt+ '/10'
    if cnt == 10 :
        label(text = 'Mission Clear!!')
        break
    for i in range(5) :
        if mag(ball.pos - a_list[i].pos) <= 2 :
            o=3
    if o == 3 :
        label(text = 'Game Over!!')
        break
    if mag(ball.pos - bu.pos) <= 0.5 :
        ball.color = bu.color
        c=10
