import cv2
import numpy as np
import os
import time
import shutil

car_cascade = cv2.CascadeClassifier(r'/home/melon/Desktop/project_dinu/cars.xml')


def Launch(video):
    start = time.time()
    cap = cv2.VideoCapture(video)

    fps = cap.get(cv2.CAP_PROP_FPS)
    totalFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    #print( "total frames = : ",totalFrames )
    videolength = totalFrames/fps
    os.chdir(r'/home/melon/Desktop/project_dinu')
    try:
        if os.path.exists('data'):
            shutil.rmtree('data', ignore_errors=True)
        os.makedirs('data')

    except OSError:
        print('Error: Creating data')

    count = 0
    success = True
    framesWeNeed = 7
    interval = round(totalFrames/framesWeNeed)
    while (success):
        
        #uncomment this to bottleneck number of frames to 30.
        i = 0
        while(i<interval-1):
            a,b = cap.read()
            i += 1
		 
        success, frame = cap.read()
	#comment two lines below to remove rotation clockwise.
        #frame=cv2.transpose(frame)
        #frame=cv2.flip(frame,flipCode=1)
        #cv2.imshow('frame',frame)
        #cv2.waitKey(0)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)
	
        for (x,y,w,h) in cars:
            if(w>300 and h>300):
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)    
                img1=frame[y:y+h,x:x+w]
        #cv2.imshow('video',img1)
        #cv2.waitKey(0)
	
        name = r'/home/melon/Desktop/project_dinu/data/frame' + str(count) + '.jpg'
        print('Creating'+name)
	#print('Saving Frames')
        cv2.imwrite(name,img1)
        count += 1
    	
    print( "total frames = : ",count )   
    name = './data/frame' + str(count - 1) + '.jpg'
    os.remove(name)

    print('\ntime taken = ' + str(time.time() - start))

    cap.release()
    
    return ("{0:.2f}".format(videolength),str(totalFrames))
    
Launch(r'/home/melon/Desktop/project_dinu/a-car3.mp4')
