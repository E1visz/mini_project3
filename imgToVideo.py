import os
import cv2


def imgToVideo(hashtag):
  path = "img/" + hashtag
  fps = 24 
  size = (1000,450) 
  VideoWriter = cv2.VideoWriter(hashtag+".avi",cv2.VideoWriter_fourcc('M','J','P','G'),fps,size)
  for i in range(11):
    img = cv2.imread(path + str(i) +".png")
    for i in range(70):
      VideoWriter.write(img)


