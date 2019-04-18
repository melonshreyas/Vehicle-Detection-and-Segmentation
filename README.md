# Vehicle-Detection-and-Segmentation from Video
The ﬁrst stage of processing in a license plate recognition system is the video frame selection followed by detection and extraction of the license plate area from a larger scene image to minimize subsequent computations and complexity of the algorithm. A moving object can be detected and tracked from a continuous video sequence based on the two primary information such as visual characteristics such as color, texture, shape, and motion characteristics. In video, as object moves from one frame to another, the object to be tracked changes its position. The variability in visual features is quite evident due to this movement. The various challenges a moving object detection and segmentation technique faces are illumination involving changes in brightness, dynamic background, presence of background clutters, presence of shadows, camera motion, presence of noise, etc. The car in the video is considered as positive images and all the background in the video is considered as negative images are classiﬁed using haar cascade classiﬁer.  Hencein the complete video only the positive part is extracted as shown in the Fgure 1 and 2.
![](c1.jpg)
![](c2.jpg)
![](c3.jpg)
![](c4.jpg)


# Extracting the Frames from the video
The car video is divided into multiple frames based on the length of the video, which ispassed onto further process of license plate extraction to extract and recognise the licensenplate characters. The extraction of frames from the sample video is as shown in the Figure3
![](c5.jpg)

# Python-OpenCV code
1.Create a folder named project_dinu.<br/>
2.Create a folder data in the project_dinu folder.<br/>
3.Paste the python code in the project_dinu.<br/>
4.Change the path in the python code and then run the command in terminal "python3 vehicle_detect_extract.py".<br/>
5.The extracted images are stored in the folder named data.<br/>
