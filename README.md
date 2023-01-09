# Intelligent Traffic Flow using Machine Learning

### About:

Traffic congestion is a serious problem of rising concern especially in India where the population is already over a billion and the common choices of transport for commuting being a four wheeler and a two wheeler. India is urbanizing at a great pace and it is competing with the fastest growing countries in the world which also resulted in high vehicular growth. In order to tackle this some research has been conducted on the existing methods and technologies for relieving traffic congestion and was identified with a lot of improvement to make. Hence the main aim  of this project is to make it now intelligent enough to take into consideration accidents/breakdowns, clearing way for ambulances and firetrucks and better reliability of the existing system in detecting vehicles. Using the live feed from cameras with image processing, deep learning and an algorithm with a timer logic for the signals, this project tackles the issue.

### System Architecture:

The system has been split into four categories: 1. Incoming camera feed 2. AI model for object detection 3. Signal switching algorithm 4. Signal timer logic update.

![Architecture Diagram (1)](https://user-images.githubusercontent.com/53865153/211255215-9d0ad70b-9d21-4a9e-936f-8d003c584eaf.png)

** 1. Incoming Camera Feed **

It is assumed that there is a CCTV camera at the junction with good picture quality, and the feed is being provided to the station continuously. With this incoming feed theimages are pre-processed and resized to fit the network.

** 2. AI Model for Object Detection **

The incoming feed once fits the network, the darknet library runs a feed forward propagation through the network to obtain inference for the feed. There are two models, one is the custom trained model and the other is a pre-trained model. The custom trained model is used for recognising ambulances and fire trucks. And the pre-trained model is used for recognising cars, motorbikes, trucks, and buses. This data is then sent to the next module for processing the data for calculating the total number of vehicle classes and calculating the green signal time.

** 3. Signal Switching Algorithm **

From the AI model for object detection the data that is received, gets taken and processed.Once processed if there is an emergency vehicle in a road then that road is given highest priority. Then the signal is changed to green for that respective road immediately. During this time another thread is started to simultaneously process the green signal time for the remaining roads. And according to the traffic density that road is given higher priority than others. Once the emergency vehicle passes the remaining the green signal times are assigned based on the order from before. This cycle then keeps repeating until the system is halted. Every time a road is assigned a green signal a system called the starvation tracker is initiated.This starvation keeps a track for how long a road is under green signal. And every time each road turns green it checks the status of the road the last time it turned green to see if the traffic is moving or stagnant. If it is found that the traffic is static and not moving much then an alert is issued for manual inspection to see if there is a possible accident or breakdown.

** 4. Signal Timer Logic Update **

Once the priority for each signal is assigned and green signal time is also calculated then the information is then sent to the traffic signal junction and updated accordingly in a loop as long as the system is running and incoming feed is not stopped.


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
