import cv2
import numpy as np
import matplotlib.pyplot as plt
import pyautogui
from time import sleep
from tkinter import *


def button_click():
    im3 = pyautogui.screenshot('img\\screenshot1.png', region=(10, 120, 500, 500))
    sleep(0.1)

    img = cv2.imread('img\\screenshot1.png')
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    blue1 = np.array([90, 50, 50])
    blue2 = np.array([120, 255,255])
    green1 = np.array([45, 50,50])
    green2 = np.array([75, 255,255])
    red1 = np.array([0, 50,50])
    red2 = np.array([15, 255,255])
    red3 = np.array([165, 50,50])
    red4 = np.array([180, 255,255])
    yellow1 = np.array([20, 50,50])
    yellow2 = np.array([35, 255,255])

    mask_blue = cv2.inRange(hsv, blue1, blue2)
    mask_green = cv2.inRange(hsv, green1, green2)
    mask_red = cv2.inRange(hsv, red1, red2)
    mask_red2 = cv2.inRange(hsv, red3, red4)
    mask_yellow = cv2.inRange(hsv, yellow1, yellow2)

    res_blue = cv2.bitwise_and(img, img, mask=mask_blue)
    res_green = cv2.bitwise_and(img, img, mask=mask_green)
    res_red1 = cv2.bitwise_and(img, img, mask=mask_red)
    res_red2 = cv2.bitwise_and(img, img, mask=mask_red2)
    res_red = cv2.bitwise_or(res_red1, res_red2)
    res_yellow = cv2.bitwise_and(img, img, mask=mask_yellow)




    # res_red에서 빨간색 물체 개수 세기
    img_gray = cv2.cvtColor(res_red, cv2.COLOR_BGR2GRAY)
    ret, img_binary = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnt = 0
    for i in range(len(contours)):
        area = cv2.contourArea(contours[i])
        if area > 100:
            cnt += 1

    cnt = cnt-1
    print(cnt)
    label.config(text=cnt)

    if chkVal1.get():
        # img show
        plt.imshow(cv2.cvtColor(res_red, cv2.COLOR_BGR2RGB))
        plt.show()


root = Tk()
root.title("GUI")
root.geometry("300x100")
root.resizable(False, False)
button = Button(root, text="Click", command=button_click)
button.pack()
label = Label(root, text="Click the button")
label.pack()
checkbutton = Checkbutton(root, text="Check")
checkbutton.pack()
chkVal1 = BooleanVar()
checkbutton.config(variable=chkVal1)
root.mainloop()