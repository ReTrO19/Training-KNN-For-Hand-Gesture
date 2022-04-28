import cv2
from os.path import exists
import os

videos_path = "D:\\Projects\\Hand Gesture\\Training\\Data Creation\\video_folder"
class_name = input("Enter Class Name:")
name_index = 0
file_name = os.path.join(videos_path,class_name +"_"+ str(name_index))

while True:
    if exists(file_name + ".mp4"):
        file_name = file_name + "_" + str(name_index)
        name_index = 0
    else:
        break

cap = cv2.VideoCapture("http://192.168.0.103:4747/video")

result = cv2.VideoWriter(file_name + ".mp4", 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, (640,480))
while True:
    ret,frame = cap.read()
    if not ret:
        break
    frame = cv2.resize(frame,(640,480))
    result.write(frame)
    cv2.imshow('Frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
            break

cap.release()
result.release()
    
# Closes all the frames
cv2.destroyAllWindows()