import cv2
import darknet as dn
from ctypes import c_float

config_file = "cfg/yolov4-tiny-custom.cfg"
data_file = "data/obj.data"
weights = "yolov4-tiny-custom_best.weights"
v4_config_file = "cfg/yolov4-tiny.cfg"
v4_data_file = "data/v4.data"
v4_weights = "yolov4-tiny.weights"

def array_to_image(arr):
    arr = arr.transpose(2,0,1)
    c = arr.shape[0]
    h = arr.shape[1]
    w = arr.shape[2]
    arr = (arr/255.0).flatten()
    data = dn.c_array(c_float, arr)
    im = dn.IMAGE(w,h,c,data)
    return im

def start_yolo():
    network, class_names, class_colors = dn.load_network(config_file, data_file, weights)
    v4_network, v4_class_names, v4_class_colors = dn.load_network(v4_config_file, v4_data_file, v4_weights)
    return network, class_names, class_colors, v4_network, v4_class_names, v4_class_colors

def detect(arr1, arr2, arr3, arr4, network, class_names, class_colors, v4_network, v4_class_names, v4_class_colors):
    Roads = {
    "Road1" : {"car":0, "motorbike":0, "bus":0, "truck":0, "Emergency_vehicle":0},
    "Road2" : {"car":0, "motorbike":0, "bus":0, "truck":0, "Emergency_vehicle":0},
    "Road3" : {"car":0, "motorbike":0, "bus":0, "truck":0, "Emergency_vehicle":0},
    "Road4" : {"car":0, "motorbike":0, "bus":0, "truck":0, "Emergency_vehicle":0}
    }
    # arr = cv2.imread("test_images/amb4.jpeg")
    img1 = array_to_image(arr1)
    img2 = array_to_image(arr2)
    img3 = array_to_image(arr3)
    img4 = array_to_image(arr4)
    dn.rgbgr_image(img1)
    dn.rgbgr_image(img2)
    dn.rgbgr_image(img3)
    dn.rgbgr_image(img4)
    images = [img1, img2, img3, img4]
    arr = [arr1, arr2, arr3, arr4]
    R = ["Road1", "Road2", "Road3", "Road4"]

    for i in range(4):
        prediction = dn.detect_image(network, class_names, images[i], thresh=.3)
        v4_prediction = dn.detect_image(v4_network, v4_class_names, images[i], thresh=.3)
        for j in range(len(prediction)):
            if prediction[j][0] == "Emergency_vehicle":
                    # print(prediction[j][0])
                    Roads[R[i]]["Emergency_vehicle"]+=1
                    # print(Roads[R[i]]["Emergency_vehicle"])

        for k in range(len(v4_prediction)):
            if v4_prediction[k][0] == "car" or v4_prediction[k][0] == "motorbike" or v4_prediction[k][0] == "bus" or v4_prediction[k][0] == "truck":
                # print(v4_prediction[k][0])
                Roads[R[i]][v4_prediction[k][0]]+=1
                # print(Roads[R[i]][v4_prediction[k][0]])
    # print(Roads)
    img_bbox = []
    v4_img_bbox = []
    for l in range(4):
        img_bbox.append(dn.draw_boxes(prediction, arr[l], class_colors))
        v4_img_bbox.append(dn.draw_boxes(v4_prediction, arr[l], v4_class_colors))

    return Roads, img_bbox, v4_img_bbox
#
# cv2.imshow("emergency vehicle", img_bbox)
# cv2.waitKey()
# cv2.destroyAllWindows()
#
# print(dn.network_width(network))
# print(dn.network_height(network))
