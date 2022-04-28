import cv2
import mediapipe as mp
import ctypes
from hand_details import HandEncodings
from utils import csv_write_data,feature_extract
import json

# Load Json with the Training Image Data
json_file = open('class_data.json',)

# Load TXT to write the classes
class_txt_file = open("classes.txt","w")

json_data = json.load(json_file)

mp_hands = mp.solutions.hands
user32 = ctypes.windll.user32

radius = 5
color = (0,255,0)
thickness = -1
main_list = []

for class_index,curr_class in enumerate(json_data):
  class_txt_file.write(str(curr_class) + " \n")
  for singlefile in json_data[curr_class]:
    print("Image Path ==== >",singlefile)
    image = cv2.flip(cv2.imread(singlefile), 1)

    with mp_hands.Hands(static_image_mode = False,max_num_hands = 1,
      min_detection_confidence = 0.5,model_complexity = 0) as hands:

      """ Created Object of class HandEncodings """
      HEclass = HandEncodings(image,hands,mp_hands)
      """
      Extracts Thumb Finger(TF),Index Finger(IF),Middle Finger(MF), Ring Finger(RF), Pinky Finger(PF) co-ordinates
      """
      TF,IF,MF,RF,PF = HEclass.frame_to_encodings()
      if TF is not None:
        TF_IF,IF_MF,MF_RF,RF_PF = feature_extract(TF,IF,MF,RF,PF)
        main_list.append([TF_IF,IF_MF,MF_RF,RF_PF,class_index])

# Writing Data in CSV
csv_write_data(main_list)
class_txt_file.close()




  


