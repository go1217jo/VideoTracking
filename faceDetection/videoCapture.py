
# coding: utf-8

# In[4]:


import cv2
import sys
import os
import argparse
from PIL import Image


# In[5]:


vidcap = cv2.VideoCapture("./video.mp4")

imgs = []
idx = 1

#print("진행 ", end='')
while(vidcap.isOpened()):
    # read()는 grab()와 retrieve() 두 함수를 한 함수로 불러옴
    # 두 함수를 동시에 불러오는 이유는 프레임이 존재하지 않을 때
    # grab() 함수를 이용하여 return false 혹은 NULL 값을 넘겨 주기 때문
    ret, image = vidcap.read()
    
    if not(ret):
        break
        
    if(int(vidcap.get(1)) % 50 == 1):
        cv2.imwrite("./ImageSamples\\Sample" + str(idx) + ".jpg", image)
        idx+=1

vidcap.release()

