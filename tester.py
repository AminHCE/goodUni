from time import sleep
from math import sin, radians

width = 64 # Related to the size of your terminal
shape = '###############'
speed = 10 # Zero means the most speed
x = 0
while True :
    if speed :
        sleep(0.1/speed)
    
    x %= 360
    space = (width+int(sin(radians(x))*width))*' '
    print(space + shape)
    x += 12 # compression