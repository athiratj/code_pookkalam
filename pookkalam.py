import cv2
import numpy as np
import math

size = 800
center = size//2
radius = 3*size//8

dark_red = (0,0,170)
red = (0,0,240)
dark_orange = (0,80,255)
orange = (0,120,255)
yellow = (0,200,255)
light_yellow = (150,240,255)
light_yellow2 = (200,240,255)
white = (255,255,255)
violet = (100,20,140)
dark_violet = (80,0,100)
dark_green = (0,120,0)
green = (65,175,0)
black = (0,0,0)
black2 = (2,2,2)


def rotate(x,y,xo,yo,theta): 
    xr=math.cos(theta)*(x-xo)-math.sin(theta)*(y-yo)   + xo
    yr=math.sin(theta)*(x-xo)+math.cos(theta)*(y-yo)  + yo
    return (int(xr), int(yr))

def gen_points(r, n, xo = center, yo = center, omega = 0):
    result = []
    theta = math.radians(360/n)
    omega = math.radians(omega)
    for i in range(n):
        result.append( rotate(xo+r, yo, xo, yo, i*theta + omega) )
    return result

im = 255 * np.ones(shape=[900, 800, 3], dtype=np.uint8)
im2 = 255 * np.ones(shape=[900, 800, 3], dtype=np.uint8)
mask = np.zeros(shape=[900, 800, 3], dtype=np.uint8)
mask2 = np.zeros(shape=[900, 800, 3], dtype=np.uint8)
cv2.circle(im, (size//2, size//2) , radius +24, red, 1, 0)

cv2.circle(mask, (size//2, size//2) , radius +24, white, 1, 0)
cv2.floodFill(mask,None, (0,0), white)

cv2.circle(mask2, (size//2-1, size//2) , 195, white, 1, 0)
cv2.floodFill(mask2,None, (0,0), white)

for point in gen_points(radius//2, 24):
    cv2.circle(im, (point[0], point[1]) , radius, (0,0,0), 1, 0)

# Adding Colors
for point in gen_points(radius - 2, 24, omega=2):
    cv2.floodFill(im,None, (point[0], point[1]), dark_green)

for point in gen_points(radius - 16, 24, omega=5):
    cv2.floodFill(im,None, (point[0], point[1]), green)

for point in gen_points(radius - 2, 6, omega=5):
    cv2.floodFill(im,None, (point[0], point[1]), light_yellow)

for point in gen_points(radius - 16, 6, omega=5):
    cv2.floodFill(im,None, (point[0], point[1]), yellow)

for point in gen_points(radius - 16, 6, omega=10):
    cv2.floodFill(im,None, (point[0], point[1]), yellow)

for point in gen_points(radius -30, 24, omega=5):
    cv2.floodFill(im,None, (point[0], point[1]), orange)

for point in gen_points(radius -30, 6, omega=35):
    cv2.floodFill(im,None, (point[0], point[1]), light_yellow)

for point in gen_points(radius -60, 24, omega=0 ):
    cv2.floodFill(im,None, (point[0], point[1]), red)

for point in gen_points(radius -70, 24, omega=35 ):
    cv2.floodFill(im,None, (point[0], point[1]), dark_red)

for point in gen_points(radius -90, 24, omega=35 ):
    cv2.floodFill(im,None, (point[0], point[1]), violet)

for point in gen_points(radius -100, 24, omega=35 ):
    cv2.floodFill(im,None, (point[0], point[1]), dark_violet)

# Erase construction lines of layer 1
im = cv2.bitwise_or(im,mask)
cv2.circle(im, (size//2-1,size//2), 196,black,-1,8,0)
cv2.circle(im, (size//2-1,size//2), 194,white,-1,8,0)

#second layer
cv2.circle(im2, (size//2-1,size//2), 196,black,-1,8,0)
circ_points = gen_points(175, 24, omega=0, xo = center-1 )
for i in range(12):
    cv2.line(im2, circ_points[i], circ_points[i+12], black2, 1)

for i in range(4):
    cv2.circle(im2, (size//2-1,size//2), 175-30*i,black2,1,0)
print("made by Vaishnav A V")
colors = [dark_violet,red,yellow,light_yellow2]

for i in range(1,5):
    for j in range(4):
        for points in gen_points(178-30*i, 6, omega=10+ 15*j + 15*i, xo = center-1 ):
            cv2.floodFill(im2, None, points, colors[j])

cv2.circle(im2, (size//2-1,size//2), 90,black2,-1,8,0)
cv2.circle(im2, (size//2-1,size//2), 65,dark_green,-1,8,0)
cv2.circle(im2, (size//2-1,size//2), 90,black,1,8,0)



cv2.circle(im2, (size//2-1,size//2), 75,dark_green,-1,8,0)
cv2.circle(im2, (size//2-1,size//2), 60,green,-1,8,0)
cv2.circle(im2, (size//2-1,size//2), 75,black,1,8,0)
cv2.circle(im2, (size//2-1,size//2), 5,(0,220,255),-1,8,0)
cv2.circle(im2, (size//2-1,size//2), 22,black,1,8,0)
for point in gen_points(30, 6, omega=5, xo = center-1 ):
    cv2.circle(im2, point, 20,black,1,8,0)

for point in gen_points(32, 6, omega=5, xo = center-1 ):
    cv2.floodFill(im2,None, point, light_yellow2)
    cv2.circle(im2, point, 5,violet,-1,8,0)
for point in gen_points(32, 6, omega=35, xo = center-1 ):
    cv2.floodFill(im2,None, point, yellow)

for point in gen_points(16, 6, omega=35, xo = center-1 ):
    cv2.floodFill(im2,None, point, orange)

for point in gen_points(16, 6, omega=5, xo = center-1 ):
    cv2.floodFill(im2,None, point, red)

# Erase construction lines of layer 2
im2 = cv2.bitwise_or(im2,mask2)

#Joining layer 1 & 2
im = cv2.bitwise_and(im,im2)
text='HAPPY ONAM'
col = [yellow,dark_green,dark_violet,red,dark_orange]
for i in range (10):
    cv2.putText(im,text[i],(80+(i*65),850), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 3,col[i%5],8)

cv2.imwrite("pookalam.png",im)
