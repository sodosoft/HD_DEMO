import pyautogui as pg
import cv2
import numpy as np
import pytesseract
from PIL import ImageGrab

button5location = pg.locateOnScreen('D:/green.png')# 이미지가 있는 위치를 가져옵니다. 
print(button5location)  

if(button5location != None):
    startX =  button5location.left + 132   
    startY =  button5location.top

    # 캡쳐 구간
    img = ImageGrab.grab((button5location.left + 132, startY, startX + 35 ,startY + 18))   
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(img)

    print(text) 
# img = cv2.imread('D:/colorTest.png')
# hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# bound_lower = np.array([25, 20, 20])
# bound_upper = np.array([100, 255, 255])

# mask_green = cv2.inRange(hsv_img, bound_lower, bound_upper)
# kernel = np.ones((7,7),np.uint8)

# mask_green = cv2.morphologyEx(mask_green, cv2.MORPH_CLOSE, kernel)
# mask_green = cv2.morphologyEx(mask_green, cv2.MORPH_OPEN, kernel)

# seg_img = cv2.bitwise_and(img, img, mask=mask_green)
# contours, hier = cv2.findContours(mask_green.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# output = cv2.drawContours(seg_img, contours, -1, (0, 0, 255), 3)

# cv2.imshow("Result", output)
# cv2.waitKey(0)
# cv2.destroyAllWindows()