# Intelligent Traffic Flow using Machine Learning

### About:

Traffic congestion is a serious problem of rising concern especially in India where the population is already over a billion and the common choices of transport for commuting being a four wheeler and a two wheeler. India is urbanizing at a great pace and it is competing with the fastest growing countries in the world which also resulted in high vehicular growth. In order to tackle this some research has been conducted on the existing methods and technologies for relieving traffic congestion and was identified with a lot of improvement to make. Hence the main aim  of this project is to make it now intelligent enough to take into consideration accidents/breakdowns, clearing way for ambulances and firetrucks and better reliability of the existing system in detecting vehicles. Using the live feed from cameras with image processing, deep learning and an algorithm with a timer logic for the signals, this project tackles the issue.

### System Architecture:

The system has been split into four categories: 1. Incoming camera feed 2. AI model for object detection 3. Signal switching algorithm 4. Signal timer logic update.

![Architecture Diagram (1)](https://user-images.githubusercontent.com/53865153/211255215-9d0ad70b-9d21-4a9e-936f-8d003c584eaf.png)

###### Incoming Camera Feed

### Instructions to run the program:

**_This program was run and tested only on an Ubuntu system_**

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
