import cv2
import numpy as np
from PIL import Image

class CocoDataset:

    def detection(self, img):

        net = cv2.dnn.readNetFromDarknet('files//yolov3-spp.cfg', 'files//yolov3-spp.weights')


        with open('files//coco.names', 'r') as f:
            self.classes = [line.strip() for line in f.readlines()]

        #print(type(self.img))
        my_img = cv2.imread(img)
        my_img = cv2.resize(my_img, (800, 800))

        # my_img.shape
        wt, ht, _ = my_img.shape  # width, height, channel

        blob = cv2.dnn.blobFromImage(my_img, 1 / 255, (416, 416), (0, 0, 0), swapRB=True, crop=False)
        net.setInput(blob)
        last_layer = net.getUnconnectedOutLayersNames()
        layer_out = net.forward(last_layer)

        boxes = []
        confidences = []
        class_ids = []

        # we will use the for loop to figure out the bounding boxes, confidence and class ids
        for output in layer_out:
            for detection in output:
                score = detection[5:]  # class probabilities are after the 5th element
                class_id = np.argmax(score)  # maximum probability of which class by using argmax function
                confidence = score[class_id]

                if confidence > 0.6:  # we don't need low confidence values
                    center_x = int(detection[0] * wt)  # we are doing this because detection would be in the range 0 to 1 and we want to
                    center_y = int(detection[1] * ht)  # convert it back to normal image size
                    w = int(detection[2] * wt)
                    h = int(detection[3] * ht)

                    x = int(center_x - (w / 2))
                    y = int(center_y - (h / 2))

                    # we got all the values required so lets append our boxes, our confidences and class_ids by .append method
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        # to figure out the bounding boxes out of these values we can utiize following command
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

        # once we have defined the indexes we need to give the font
        font = cv2.FONT_HERSHEY_PLAIN
        colors = np.random.uniform(0, 255, size=(len(boxes), 3))

        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            label = str(self.classes[class_ids[i]])  # to get the label. class_ids only gives class id not the class name
            confidence = str(round(confidences[i], 2))
            color = colors[i]
            cv2.rectangle(my_img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(my_img, label + " " + confidence, (x, y), font, 2, (0, 0, 0), 2)

        im = cv2.cvtColor(my_img, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(im)
        return im

#coco = CocoDataset('3.jpg')
#image=coco.detection()
#image.save('testimages/myfile.jpg')