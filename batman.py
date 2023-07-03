import cv2

img = cv2.imread('bat.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, img_gray_t = cv2.threshold(img_gray, 135, 255, cv2.THRESH_BINARY_INV)
# cv2.putText(img_gray_t, "BATMAN", (img_gray_t.shape[1]//2 - 100, 6* img_gray_t.shape[0]//7),
#             cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2, cv2.LINE_AA)

text_size, _ = cv2.getTextSize("BATMAN", cv2.FONT_HERSHEY_SIMPLEX, 1.5, 2)
text_x = int((img_gray_t.shape[1] - text_size[0]) / 2)
text_y = int(6* img_gray_t.shape[0]//7)
cv2.putText(img_gray_t, "BATMAN", (text_x, text_y),
            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2, cv2.LINE_AA)
cv2.imshow("2", img_gray_t)
cv2.waitKey()