#   uses opencv2 circle detection to grab any circle or (cue ball in image)
#   function to return image with detected circles (drawn rectangles) and all extracted (cue ball)
import ast

import cv2
import numpy as np
from PIL import Image

from ast import literal_eval

#   check if client has already completed marking for image and update with text to labeled accordingly
#   return encoded image after processing

def UPDATE_LABELED_IMG(IMG_NAME,LABELED_DATA,UPDATED):
    color=(0,0,0)#black
    if UPDATED:
        color=(0, 255,0)#green if updated to new one

    POOL_TABLE_IMG=cv2.imread(f"./IMAGES/{IMG_NAME}") #start with original clean pool table image
    #print(LABELED_DATA)
    for x in range(len(list(LABELED_DATA))):
        INDEX=list(LABELED_DATA)[x]
        CLIENT_LABELED=LABELED_DATA[INDEX][0]
        #check if client has labeled it?
        if CLIENT_LABELED:
            BOX_COORDINATE=ast.literal_eval(LABELED_DATA[INDEX][2])
            BOX_COORDINATE_X,BOX_COORDINATE_Y=BOX_COORDINATE[0],BOX_COORDINATE[1]
            cv2.circle(POOL_TABLE_IMG, (BOX_COORDINATE_X,BOX_COORDINATE_Y+5), 5, (0, 255, 0), -5)
            cv2.putText(POOL_TABLE_IMG, f'[{LABELED_DATA[INDEX][0]}]', (BOX_COORDINATE_X,BOX_COORDINATE_Y+5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color,1, cv2.LINE_AA)

    return cv2.imencode('.jpg', POOL_TABLE_IMG)[1].tobytes()     #return as encoded img for qimage reading

#   put image ontop of another image with coordianates
def overlay_image(img1,img2,location,LABEL_NAME):
    h,w = img1.shape[:2]
    h1,w1=img2.shape[:2]
    x,y = location
    img1[y:y+h1,x:x+w1]=img2
    cv2.putText(img1,f'[{LABEL_NAME}]',(x,y+int(h1*1.5)),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),0,cv2.LINE_AA)
    #return img1


#   USES OPENCV HoughCircles detection to detect any circles (needed to detect cue balls)
def DETECT_CUE_BALL(img_path):
    img=cv2.imread(img_path,cv2.IMREAD_UNCHANGED)
    gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    EXTRACTED_CUEBALLS=[]

    #circle detection
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=18, minRadius=10, maxRadius=15)


    BLANK_IMG=cv2.imread("./BLANK.jpg")

    blank_width = BLANK_IMG.shape[1]  # keep original width
    blank_height = 90
    dim = (blank_width, blank_height)
    blank_img = cv2.resize(BLANK_IMG, dim, interpolation=cv2.INTER_AREA)


    COUNT=0
    LABEL_NAME=0
    if circles is not None:
        circles = np.uint16(circles)

        for pt in circles[0, :]:

            x, y, r = pt[0], pt[1], pt[2]

            #cv2.circle(img, (x, y), r, (0, 0, 255), 1)  # draw detected circles
            # bounding box around each circle
            a = 5  #width&height space of rectangle
            point_1 = (x - (r + a), y - (r + a))  # x,y
            point_2 = (x + (r + a), y + (r + a))

            #cv2.rectangle(edit_img, point_1, point_2, (0, 255, 0), 0) #draw rectangle
            #cv2.circle(img,point_1,5,(0,0,255),-5)

            corner_rect_x=point_1[0]
            corner_rect_y=point_1[1]

            length,width = point_2[1]-point_1[1],point_2[0]-point_1[0]

            #extract each detected cue ball from the rectangle
            extracted_img=img[corner_rect_y:corner_rect_y+length,corner_rect_x:corner_rect_x+width]

            #overlay each





            label_info=[corner_rect_x,corner_rect_y,width,length] #Top-left corner along with the width and height of the bounding box.

            #   COLLECT VALID DETECTED CUE BALLS
            try:

                extracted_img_data=cv2.imencode('.png',extracted_img)[1].tobytes()

                #EXTRACTED_CUEBALLS.append([extracted_img_data,label_info])
                EXTRACTED_CUEBALLS.append([extracted_img_data,label_info])
                #extracted_img_h, extracted_img_w = extracted_img.shape[0], extracted_img.shape[1]
                x,y=(0+40*COUNT,0)
                overlay_image(blank_img, extracted_img, (x,y), COUNT)
                COUNT = COUNT + 1
            except:
                pass
            LABEL_NAME = LABEL_NAME + 1 #next label


    table_img_data=cv2.imencode('.jpg', img)[1].tobytes() #send image data encoded over


    # cv2.imshow("image",blank_img)
    # cv2.waitKey(0)

    # unedited_pool_table_img,ALL_EXTRACTED_CUEBALLS_IMGS_indvidual,ALL_EXTRACTED_CUEBALLS_IMG_FULL
    return table_img_data,EXTRACTED_CUEBALLS,cv2.imencode('.jpg', blank_img)[1].tobytes()

