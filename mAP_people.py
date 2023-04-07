import cv2
import numpy as np
import sys
import PhotoConverter
import Classify, Detect
import ClassConverter
import matplotlib.pyplot as plt

imgList = []
#사진 파일 읽기
for i in range(50):
    if i < 10 :
        filename = f"0{i}.png"
    else :
        filename = f"{i}.png"
    img = cv2.imread("./YoloTest/people/" + filename)
    imgList.append(img)

for i in range(50):
    if i < 10 :
        filename = f"0{i}.png"
    else :
        filename = f"{i}.png"
    img = cv2.imread("./YoloTest/gym/" + filename)
    imgList.append(img)

# 객체 검출 함수
ap_raw = []
pr = []
rc = []
for k in range(9):
    threshold = 0.1 * k + 0.1
    detectedInfos, _ = Detect.detect(imgList, threshold)
    classes = detectedInfos[0][4]
    tp = 0
    fn = 0
    fp = 0
    for i in range(len(detectedInfos)) :

        check_class = []
        class_ids, confidence, boxes, indexes, _ = detectedInfos[i]
        font = cv2.FONT_HERSHEY_PLAIN
        for j in range(len(boxes)):
            if j in indexes:
                check_class.append(ClassConverter.Label2Class(classes[class_ids[j]]))
        if 'people' in check_class and i < 50 :
            tp = tp + 1
        elif i < 50 :
            fn = fn + 1
        elif 'people' in check_class and i >= 50 :
            fp = fp + 1
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    print("----------confidence threshold : "+str(round(threshold,2))+"----------")
    print("precision : "+str(round(precision,2)))
    print("recall : "+str(round(recall,2)))
    pr.append(round(precision,2))
    rc.append(round(recall,2))
plt.plot(rc,pr)
plt.savefig('people_PR.png')