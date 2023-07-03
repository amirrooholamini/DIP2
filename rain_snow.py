import cv2
import numpy as np
import imageio
import random

dataset = []
snow_circles = []
rain_lines = []

winter = cv2.imread('winter.jpg')
winter = cv2.cvtColor(winter, cv2.COLOR_BGR2GRAY)

autumn = cv2.imread('autumn.jpg')
autumn = cv2.cvtColor(autumn, cv2.COLOR_BGR2GRAY)


R,C = winter.shape


winter_copy = winter.copy()

winter_percent = 1
autumn_percent = 0


while True:
    if len(snow_circles) <= 100:
        snow_circles.append((random.randint(0, C),-10))  # c and r1
        snow_circles.append((random.randint(0, C),-10))  # c and r1
    else:
        winter_copy = cv2.addWeighted(winter, winter_percent, autumn, autumn_percent, 0)
        
        winter_percent -= 0.02
        winter_percent = max(0, winter_percent)
        autumn_percent += 0.02
        autumn_percent = min(1, autumn_percent)
        
    continue_loop = False
    for j in range(len(snow_circles)):
        cv2.circle(winter_copy, snow_circles[j], 1, 255, -1)
        left_random = random.randint(-1, 1)
        snow_circles[j] = (snow_circles[j][0] + left_random, snow_circles[j][1] + 3)
        if snow_circles[j][1] < R + 30:
            continue_loop = True
    
    if not continue_loop:
        break
        
    img_uint8 = winter_copy.astype(np.uint8)
    dataset.append(img_uint8)
    winter_copy = winter.copy()
    
autumn_copy = autumn.copy()

rain_speed = 7

while True:
    if len(rain_lines) >= 1000:
        break
    for i in range(int(rain_speed)):
        rain_lines.append((random.randint(-C, C), -5))
    rain_speed += 0.2
    for i in range(len(rain_lines)):
        cv2.line(autumn_copy, (rain_lines[i][0], rain_lines[i][1]), (rain_lines[i][0] + 3, rain_lines[i][1] + 5), 200, 1)
        rain_lines[i] = (rain_lines[i][0] + 3, rain_lines[i][1] + 7)
    
    img_uint8 = autumn_copy.astype(np.uint8)
    dataset.append(img_uint8)
    autumn_copy = autumn.copy()
    
    
imageio.mimsave("rain_snow.gif", dataset, duration=0.2)