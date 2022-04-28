
"""
IMPORTS
"""

import cv2
import numpy as np



class HandEncodings:

    """
    CLass Parameters
    user_frame: A frame of a video is passed
    handsclass: Model parameter object
    mp_hands: Media Pipe hand class import

    """

    def __init__(self,user_frame,handsclass,mp_hands):
        self.process_frame = user_frame
        self.handsclassobj = handsclass
        self.mp_hands = mp_hands

    """
    Get required hand landmarks as an output
    """

    def frame_to_encodings(self):

        frame_height, frame_width = self.process_frame.shape[:2]
        results = self.handsclassobj.process(cv2.cvtColor(self.process_frame, cv2.COLOR_BGR2RGB))
        hands_encode = results.multi_hand_landmarks
        thumb_finger_coords = None
        index_finger_coords = None
        middle_finger_coords = None
        ring_finger_coords = None
        pinky_finger_coords = None


        if hands_encode is not None:
            """
            Returns Thumb,index,middle,ring,pinky finger tip co-ordinates
            """
            single_hand_encode = hands_encode[0]

            thumb_tip_x_coords = int(
                single_hand_encode.landmark[self.mp_hands.HandLandmark.THUMB_TIP].x * frame_width)
            thumb_tip_y_coords = int(
                single_hand_encode.landmark[self.mp_hands.HandLandmark.THUMB_TIP].y * frame_height)

            index_finger_tip_x_coords = int(
                single_hand_encode.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].x * frame_width)
            index_finger_tip_y_coords = int(
                single_hand_encode.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].y * frame_height)
            
            middle_finger_tip_x_coords = int(
                single_hand_encode.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x * frame_width)
            middle_finger_tip_y_coords = int(
                single_hand_encode.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * frame_height)
            
            ring_finger_tip_x_coords = int(
                single_hand_encode.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].x * frame_width)
            ring_finger_tip_y_coords = int(
                single_hand_encode.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].y * frame_height)
            
            pinky_tip_x_coords = int(
                single_hand_encode.landmark[self.mp_hands.HandLandmark.PINKY_TIP].x * frame_width)
            pinky_tip_y_coords = int(
                single_hand_encode.landmark[self.mp_hands.HandLandmark.PINKY_TIP].y * frame_height)

            # print("Finger Coords",(index_finger_x_coords,index_finger_y_coords))

            thumb_finger_coords = (thumb_tip_x_coords,thumb_tip_y_coords)
            index_finger_coords = (index_finger_tip_x_coords,index_finger_tip_y_coords)
            middle_finger_coords = (middle_finger_tip_x_coords,middle_finger_tip_y_coords)
            ring_finger_coords = (ring_finger_tip_x_coords,ring_finger_tip_y_coords)
            pinky_finger_coords = (pinky_tip_x_coords,pinky_tip_y_coords)

        return thumb_finger_coords,index_finger_coords,middle_finger_coords,ring_finger_coords,pinky_finger_coords

    """
    Function is used to calculate euclidean distance between any two points
    Parameters:
    p1: contain x,y co-ordinates of the first point type:tuple
    p2: contain x,y co-ordinates of the second point type:tuple
    """

    def CalculateDistace(self,p1,p2):

        import math
        eu_dist = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
        return eu_dist









