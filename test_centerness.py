import cv2
import numpy as np
import sys
import PhotoConverter
import Classify, Detect
import ClassConverter
import matplotlib.pyplot as plt

imgList = []
#사진 정답 읽기
with open("./CenternessTest/CenterCriteria.txt") as f:
    ans = f.read().splitlines()

#사진 파일 읽기
for i in range(10):
    if i < 10 :
        filename = f"0{i}.png"
    else :
        filename = f"{i}.png"
    img = cv2.imread("./CenternessTest/" + filename)
    imgList.append(img)


# 객체 검출 함수
detectedInfos, imgShapeList = Detect.detect(imgList,0.5)

mains = Classify.classify(imgShapeList,detectedInfos)

cnt = 0
font = cv2.FONT_HERSHEY_PLAIN
for i in range(len(imgList)) :
    main_label, main_x, main_y, main_w, main_h, color = mains[i]
    if main_label == ans[i]:
        cnt += 1
    else:
        cv2.rectangle(imgList[i], (main_x, main_y), (main_x + main_w, main_y + main_h), color, 2)
        cv2.putText(imgList[i], "Main Class : "+main_label, (10,20), font, 1, color, 1)
        cv2.imwrite(f"res/res{i}.jpg", imgList[i])
        print(str(i) + " : " + main_label + " :: " + ans[i])

print("accuracy : "+str(round(cnt/100,2)))