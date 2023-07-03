import cv2
import numpy as np
import imageio

noise_tv = []

img = cv2.imread('tv.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

for i in range(20):
    noise_img = np.random.random((473,640)) * 255
    img_gray[27:500, 100:740] = noise_img
    img_uint8 = img_gray.astype(np.uint8)
    noise_tv.append(img_uint8)
    
noise_tv.append(img_gray)
output_filename = "noisy_television.gif"
imageio.mimsave(output_filename, noise_tv, duration=0.2)