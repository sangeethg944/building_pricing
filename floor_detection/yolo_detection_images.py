import numpy as np
import cv2
# import streamlit as st
# from PIL import Image


def detectObjects(img_name, confidence_thresh):
    img_path = r"C:/Users/91974/PycharmProjects/Building Pricing Model/floor_detection/temp_img_dir/" + img_name

    result_img_path = r"C:/Users/91974/PycharmProjects/Building Pricing Model/floor_detection/temp_result_img_dir/" + img_name
    confidenceThreshold = confidence_thresh/100
    NMSThreshold = 0.3

    modelConfiguration = r'C:\Users\91974\PycharmProjects\Building Pricing Model\floor_detection\yolov4_custom.cfg'
    modelWeights = r'C:\Users\91974\PycharmProjects\Building Pricing Model\floor_detection\yolov4_custom_best.weights'

    labelsPath = r'C:/Users/91974/PycharmProjects/Building Pricing Model/floor_detection/classes.names'
    labels = open(labelsPath).read().strip().split('\n')

    np.random.seed(10)
    COLORS = np.random.randint(0, 255, size=(len(labels), 3), dtype="uint8")

    net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)

    # print(img_path)
    # image = cv2.imread(str(img_path))
    image = cv2.imread(img_path)
    # st.image(image, width=512)
    # (H, W) = np.shape(img_path)[:2]
    H, W = image.shape[0], image.shape[1]
    # st.write(H,W)
    # Determine output layer names
    layerName = net.getLayerNames()
    layerName = [layerName[i - 1] for i in net.getUnconnectedOutLayers()]

    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    layersOutputs = net.forward(layerName)

    boxes = []
    confidences = []
    classIDs = []

    for output in layersOutputs:
        for detection in output:
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]
            if confidence > confidenceThreshold:
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY, width, height) = box.astype('int')
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))

                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                classIDs.append(classID)

    # Apply Non Maxima Suppression
    detectionNMS = cv2.dnn.NMSBoxes(boxes, confidences, confidenceThreshold, NMSThreshold)
    floors = []
    if len(detectionNMS) > 0:
        for i in detectionNMS.flatten():
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])

            floors.append((x, y, w, h))
            color = [int(c) for c in COLORS[classIDs[i]]]
            cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
            text = '{}: {:.4f}'.format(labels[classIDs[i]], confidences[i])
            cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    cv2.imwrite(result_img_path, image)
    return result_img_path, len(floors)


