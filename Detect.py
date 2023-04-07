import cv2
import numpy as np
import sys
import PhotoConverter
import Classify

def detect(imgList, threshold):
    # 변수 선언
    classes = []
    class_ids = []
    confidences = []
    boxes = []
    imgShapeList = []
    # yolov3 reading
    net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
    with open("coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))
    detectedInfos = []
    for i in range(len(imgList)):
        img = imgList[i]
        #img info
        imgShapeList.append(img.shape)
        height, width, channels = img.shape
        
        # Detecting objects
        blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > threshold:
                    # Object detected
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    # 좌표
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        
        # 검출된 객체들 중 main class를 판별하는 코드
        detectedInfo = []
        detectedInfo.append(class_ids)
        detectedInfo.append(confidences)
        detectedInfo.append(boxes)
        detectedInfo.append(indexes)
        detectedInfo.append(classes)
        detectedInfos.append(detectedInfo)
        class_ids = []
        confidences = []
        boxes = []
        indexes = []
    return detectedInfos, imgShapeList