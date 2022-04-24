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
2. After installing darknet, copy all the files in 'cfg', and 'data' folders in this repository into your darknet installated 'cfg', and 'data' folders. 
3. Then copy the foler 'test_images' into your darknet foler. 
4. Next copy all the remaining '.txt', '.py', and '.weights' files as it is into your darknet installation folder.  
5. If it asks you want replace a file while copying, click yes.
6. Now run in your terminal 'python3 signalswitchalgo.py' 
