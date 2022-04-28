import cv2
from utils import get_files_list,check_folder_exist,write_data_json
import os

json_file = {}
video_folder = "D:\\Projects\\Hand Gesture\\Training\\Data Creation\\video_folder"
data_folder = "D:\\Projects\\Hand Gesture\\Training\\Data Creation\\data"
file_type = ".mp4"
video_files = get_files_list(file_type,video_folder)
print(video_files)
for single_video in video_files:
    file_name = single_video.split(".")[0]
    class_name = file_name.split("_")[0]
    video_file = os.path.join(video_folder,single_video)
    class_folder = os.path.join(data_folder,class_name)
    is_exist = check_folder_exist(class_folder)
    print("Folder Exist === >",is_exist)
    if not is_exist:
        os.mkdir(class_folder)
    cap = cv2.VideoCapture(video_file)
    index = 0
    trigger_frame = 20
    json_file[class_name] = []
    while True:
        ret,frame = cap.read()
        if not ret:
            break
        if index >= trigger_frame:
            image_name = os.path.join(class_folder,class_name+"_"+str(index)+".jpg")
            cv2.imwrite(image_name, frame)
            json_file[class_name].append(image_name)
            trigger_frame += 20
        index += 1
        print("Index ==== >",index)
        cv2.imshow("Output",frame)
        cv2.waitKey(1)
    
    write_data_json(json_file)