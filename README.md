This program was run and tested only on an Ubuntu system

Instructions to run the program:

1. Install darknet by following the instructions from here: (https://pjreddie.com/darknet/install/). You don't need to install with CUDA, but it can increase your inference time. Installing with OpenCV is required. And LIBSO must be enabled. 
Or you can also simply replace with this in your makefile to make sure opencv and libso are enabled: 
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
2. Clone this repository into your system.
3. After installing darknet, copy all the files in 'cfg', and 'data' folders in this repository into your darknet installated 'cfg', and 'data' folders. 
4. Then copy the foler 'test_images' into your darknet foler. 
5. Next copy all the remaining '.txt', '.py', and '.weights' files as it is into your darknet installation folder.  
6. If it asks you want replace a file while copying, click yes.
7. Now run in your terminal 'python3 signalswitchalgo.py' 
