import cv2
import skimage.io
import darknet as dn
from PIL import Image
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


network, class_names, class_colors = dn.load_network(config_file, data_file, weights)
v4_network, v4_class_names, v4_class_colors = dn.load_network(v4_config_file, v4_data_file, v4_weights)



arr = cv2.imread("test_images/roads/road4.jpeg")
img = array_to_image(arr)
dn.rgbgr_image(img)


prediction = dn.detect_image(network, class_names, img, thresh=.3)
v4_prediction = dn.detect_image(v4_network, v4_class_names, img, thresh=.3)
print(prediction)
print(v4_prediction)

img_bbox = dn.draw_boxes(prediction, arr, class_colors)
v4_img_bbox = dn.draw_boxes(v4_prediction, arr, v4_class_colors)

cv2.imshow("emergency vehicle", img_bbox)
cv2.waitKey()
cv2.destroyAllWindows()

# print(dn.network_width(network))
# print(dn.network_height(network))
