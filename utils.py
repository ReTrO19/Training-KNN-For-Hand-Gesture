import os
import math
import json
import csv

def get_files_list(file_type,folder_path):
    files_list = [] 
    for file in os.listdir(folder_path):
        if file.endswith(file_type):
            files_list.append(file)
    
    return files_list

def eculidean_distance(x1,y1,x2,y2):
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return distance

def check_folder_exist(folder_path):
    return os.path.isdir(folder_path)

def write_data_json(json_data):
    json_object = json.dumps(json_data, indent = 4)
    with open("class_data.json", "w") as outfile:
        outfile.write(json_object)

def csv_write_data(file_list):
    with open('train_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["TT_IFT", "IFT_MFT", "MFT_RFT","RFT_PT","CLASS"])
        for row in file_list:
            writer.writerow(row)
        
def feature_extract(TF,IF,MF,RF,PF):
    TF_IF = eculidean_distance(TF[0],TF[1],IF[0],IF[1])
    IF_MF = eculidean_distance(IF[0],IF[1],MF[0],MF[1])
    MF_RF = eculidean_distance(MF[0],MF[1],RF[0],RF[1])
    RF_PF = eculidean_distance(RF[0],RF[1],PF[0],PF[1])

    return TF_IF,IF_MF,MF_RF,RF_PF