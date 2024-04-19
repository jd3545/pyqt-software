#   CONVERT LABELED IMAGES TO YOLO
#   SAVES TO "./LABELED_IMAGES" PATH IN YOLO FORMAT

from pathlib import Path
import cv2
from ast import literal_eval

LABELED_IMG_DIR="./LABELED_IMAGES"

def SAVE_YOLO_FORMAT(IMG_NAME,LABELED_DATA):
    #   check if txt file exists for image name

    LABELED_FILE_NAME=IMG_NAME.replace(".jpg",".txt")
    LABELED_FILE_PATH=LABELED_IMG_DIR+"/"+LABELED_FILE_NAME
    if not(Path(LABELED_FILE_PATH).is_file()):
        #   create the text file for client
        open(LABELED_FILE_PATH,"x")
    #   YOLO CONFIGURATION FORMULA
    IMG=cv2.imread(f"./IMAGES/{IMG_NAME}")

    IMG_W,IMG_H=IMG.shape[1],IMG.shape[0] #for yolo org img w,h

    #   GO THROUGH EACH LABELED DATA AND CHECK IF ITS LABELED
    FILE_DATA=[]
    for x in range(len(list(LABELED_DATA))):
        LABEL_NUMBER=list(LABELED_DATA)[x]

        if LABELED_DATA[LABEL_NUMBER][0]: #IN # LABEL DATA
            CLASS_NUMBER=LABELED_DATA[LABEL_NUMBER][1]
            BOX_COORDINATE = literal_eval(LABELED_DATA[LABEL_NUMBER][2])
            BOX_DIMENSIONS = literal_eval(LABELED_DATA[LABEL_NUMBER][3])
            UPPER_LEFT_X, UPPER_LEFT_Y = BOX_COORDINATE[0], BOX_COORDINATE[1]
            BOX_DIMENSIONS_W, BOX_DIMENSIONS_H = BOX_DIMENSIONS[0], BOX_DIMENSIONS[1]
            CALCULATED_YOLO = f"{CLASS_NUMBER} {float('%.6f' % ((2 * UPPER_LEFT_X + BOX_DIMENSIONS_W) / (2 * IMG_W)))} {float('%.6f' % ((2 * UPPER_LEFT_Y + BOX_DIMENSIONS_H) / (2 * IMG_H)))} {float('%.6f' % (BOX_DIMENSIONS_W / IMG_W))} {float('%.6f' % (BOX_DIMENSIONS_H / IMG_H))}"
            FILE_DATA.append(CALCULATED_YOLO)

    #NOW APPEND TO FILE
    with open(LABELED_FILE_PATH,"w") as f:
        for x in range(len(FILE_DATA)):
            f.write(f"{FILE_DATA[x]}\n") #OVERWRITE FILE WITH NEW DATA
    f.close()