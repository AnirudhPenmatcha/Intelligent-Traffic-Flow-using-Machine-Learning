This program was run and tested only on an Ubuntu system

Instructions to run the program:

1. Install git in your system. If you are using ubunutu, run 'sudo apt-get install git' in your terminal. 
2. Run in your terminal 'git clone https://github.com/AlexeyAB/darknet' 
3. You don't need to install with CUDA, but it can increase your inference time. Installing with OpenCV is required. And LIBSO must be enabled. 
Or you can also simply replace with this in your makefile to make sure opencv and libso are enabled: 
```
GPU=0
CUDNN=0
CUDNN_HALF=0
OPENCV=1
AVX=0
OPENMP=0
LIBSO=1
ZED_CAMERA=0
ZED_CAMERA_v2_8=0
```
4. Now run 'make' in your terminal. 
2. Clone this repository into your system by running this in your terminal: 'git clone https://github.com/AnirudhPenmatcha/Intelligent-Traffic-Flow-using-Machine-Learning.git'.
3. Copy all the files in 'cfg', and 'data' folders in this repository into your darknet installated 'cfg', and 'data' folders. If it asks whether you want replace a file while copying and pasting everytime, click yes always.
4. Then copy the foler 'test_images' from this repository into your darknet foler. 
5. Next copy all the remaining '.txt', '.py', and '.weights' files from this repository as it is into your darknet installation folder.  
7. Now run in your terminal 'python3 signalswitchalgo.py' 
