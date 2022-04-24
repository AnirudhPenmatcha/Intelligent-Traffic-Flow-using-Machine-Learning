Instructions to run the program:
1. First install darknet by following the instructions from here: (https://pjreddie.com/darknet/install/). You don't need to install with CUDA, but it can increase your inference time. Installing with OpenCV is required. And also enable LIBSO. 
You can also replace with this in your makefile: 
```GPU=0
CUDNN=0
CUDNN_HALF=0
OPENCV=1
AVX=0
OPENMP=0
LIBSO=1
ZED_CAMERA=0
ZED_CAMERA_v2_8=0
```
