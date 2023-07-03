import cv2
import numpy as np

cap = cv2.VideoCapture(0)
_, frame = cap.read()
R, C = frame.shape[0], frame.shape[1]




while True:
    _, frame = cap.read()
    
    center = frame[R//2 -100: R//2 +100, C//2 -100: C//2 +100]
    center = cv2.cvtColor(center, cv2.COLOR_BGR2GRAY)
    
    blurred_image = cv2.blur(frame, (50, 50))
    
    blurred_image[R//2 -100: R//2 +100, C//2 -100: C//2 +100] = cv2.cvtColor(center,cv2.COLOR_GRAY2RGB)
    blurred_image [R//2 - 105: R//2 - 100, C//2 -105: C//2 +105] = 0
    blurred_image [R//2 + 100: R//2 + 105, C//2 -105: C//2 +105] = 0
    
    blurred_image[R//2 -100: R//2 +100, C//2 - 105: C//2 - 100] = 0
    blurred_image[R//2 -100: R//2 +100, C//2 + 100: C//2 + 105] = 0
    
    m = int(np.mean(center))
    text = ""
    if (m < 64):
        text = "black"
    elif m < 128:
        text = "dark gray"
    elif m < 192:
        text = "light gray"
    else:
        text = "white"
    
    text_size, _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1.5, 2)
    text_x = int((blurred_image.shape[1] - text_size[0]) / 2)
    text_y = int(6* blurred_image.shape[0]//7)
    cv2.putText(blurred_image,text , (text_x, text_y),
            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2, cv2.LINE_AA)
    
    cv2.imshow("1", blurred_image)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
