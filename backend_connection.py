#   connect front end to backend(pyside2_objects)
import ast

import ast
import os
import json
from functools import partial
from os.path import dirname, join

import cv2
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from detect_cue_ball import DETECT_CUE_BALL, UPDATE_LABELED_IMG
from YOLO_CONVERT import SAVE_YOLO_FORMAT


#import custom made methods
from detect_cue_ball import DETECT_CUE_BALL,UPDATE_LABELED_IMG
from YOLO_CONVERT import SAVE_YOLO_FORMAT
current_dir = dirname(__file__)

#   GRAB EACH CUE BALL DEFUALT IMAGE FROM CLASSES
CUE_BALL_IMG={}
CUE_BALL_IMGS=[]
CUE_BALL_IMGS_PATH="./CUE_BALL_IMAGES"
for path in os.listdir(CUE_BALL_IMGS_PATH):
    #CUE_BALL_IMGS.append(str(path).strip(".jpg"))
    CUE_BALL_IMG[str(path).strip(".jpg")]=path

#   create frame details for each class
class CREATE_CLASS_FRAME:
    def __init__(self, UI, DATA):
        self.UI = UI
        self.DATA=DATA #TO SET
        self.LABEL_DATA=UI.label_3 #SET LABELING DATA TEXT

        self.sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)

        self.frame_12 = QFrame(self.UI.scrollAreaWidgetContents)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 45))
        self.frame_12.setMaximumSize(QSize(16777215, 0))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_12)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(100, 100))

        self.horizontalLayout_2.addWidget(self.label_4)

        self.UI.verticalLayout_7.addWidget(self.frame_12, 0, Qt.AlignTop)

        self.CLASS_LABEL=self.label_4

        #update data from client
        self.LABEL_NUMBER=self.DATA[1]
        self.CLASSES=self.DATA[2]
        self.CHECKPOINTS=self.DATA[0] #client checkpoints we need to update
        self.IMG_NAME=self.DATA[3]
        #QIMAGE
        self.QIMAGE = QImage()
        self.UPDATE_DATA() #Update



    def UPDATE_LABEL(self,LABEL_NAME,REFERENCE,LABEL_NUMBER):
        #self.CHECKPOINTS = json.loads(open(join(current_dir, "./checkpoint.json"), mode='r').read())
        #REFERENCE=THE CLASS INDEX FROM classes.txt
        CLASS_NAME = self.CLASSES[REFERENCE]
        LABEL_NAME.setStyleSheet("color: Green")
        LABEL_NAME.setText(f"[{LABEL_NUMBER}]-[{REFERENCE}]")


        #update the checkpoints data for each label on file as well, for each labeling
        #[CLASS_REFERENCE_NAME,CLASS_REFERENCE_NUMBER,(x,y),(w,h)]

        LABEL_DATA=self.CHECKPOINTS[self.IMG_NAME][LABEL_NUMBER]
        LABEL_DATA[0]=CLASS_NAME
        LABEL_DATA[1]=REFERENCE
        self.CHECKPOINTS[self.IMG_NAME][LABEL_NUMBER]=LABEL_DATA #rewrite label data foreach

        #print("SAVED TO CHECKPOINTS",self.CHECKPOINTS)
        #UPDATE TEXT ON SOFTWARE
        self.LABEL_DATA.setText(f"LABELED | CLASS_LABEL_NUMBER [{LABEL_NUMBER}] : CLASS_NAME [{CLASS_NAME}] | REFERENCE_NUMBER [{REFERENCE}]")
        print(f"LABELED DATA SAVED! | IMAGE | {self.IMG_NAME} | LABEL NUMBER [{LABEL_NUMBER}] REFERENCE NUMBER [{REFERENCE}] CLASS NAME [{CLASS_NAME}]")

        #SAVE TO CLIENT DIRECTORY!
        #print(self.IMG_NAME)
        with open("./checkpoint.json", "w") as file:
            json.dump(self.CHECKPOINTS,file)
        SAVE_YOLO_FORMAT(self.IMG_NAME,self.CHECKPOINTS[self.IMG_NAME])
        #print(f"LABELED | CLASS_LABEL_NUMBER [{LABEL_NUMBER}] : CLASS_NAME [{CLASS_NAME}] | REFERENCE_NUMBER [{REFERENCE}]")

        #UPDATE THE ORIGINAL POOL TABLE IMAGE WITH A NEW LABELED ONE FROM CLIENT
        self.QIMAGE.loadFromData(UPDATE_LABELED_IMG(self.IMG_NAME,self.CHECKPOINTS[self.IMG_NAME],True))
        self.UI.label_6.setPixmap(QPixmap(self.QIMAGE))
        self.UI.label_6.setScaledContents(True)
        self.UI.label_6.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

    def UPDATE_DATA(self):
        #[self.CHECKPOINTS,label_number,self.LOADED_CLASSES]

        #print(self.CLASSES)
        LABEL_DATA=self.CHECKPOINTS[self.IMG_NAME][self.LABEL_NUMBER]
        LABELED_CLASS_REFERENCE=LABEL_DATA[1] #WHAT THE CLIENT LABELED IT AS CLASS NUMBER
        #GRAB PICTURE

        #make green when client labeled from save file
        #   ok client has already labeled
        if LABELED_CLASS_REFERENCE:

            self.CLASS_LABEL.setStyleSheet("color: Green")



        self.CLASS_LABEL.setText(f"[{self.LABEL_NUMBER}]-[{LABELED_CLASS_REFERENCE}]") #TO_BE_LABELED_NAME,CLASS_NAME[IF CLIENT LABELED]

        BUTTONS_DATA={} #add to partial

        #create the push buttons
        for x in range(len(self.CLASSES)):
            self.pushButton = QPushButton(self.frame_12)
            self.pushButton.setObjectName(u"pushButton")
            self.sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
            self.pushButton.setSizePolicy(self.sizePolicy)
            self.horizontalLayout_2.addWidget(self.pushButton)

            #SET ICON FOR EACH
            self.pushButton.setIcon(QIcon(CUE_BALL_IMGS_PATH+"/"+CUE_BALL_IMG[self.CLASSES[x]]))
            self.pushButton.setIconSize(QSize(40,40))
            #self.pushButton.setText(f"[{x}]")
            BUTTONS_DATA[x]=[self.pushButton,x] #BUTTONS_DATA[x][1] == CLASSES[x]=>self.LOADED_CLASSES[x]





            # UPDATE REFERENCE LABELING FOR EACH INDEX
        for x in range(len(list(BUTTONS_DATA))):
            BUTTON,CLASS_NUMBER=BUTTONS_DATA[x][0],BUTTONS_DATA[x][1]
            BUTTON.clicked.connect(partial(self.UPDATE_LABEL,self.CLASS_LABEL,CLASS_NUMBER,self.LABEL_NUMBER))



#   to connect to backend
class Connect:
    def __init__(self, UI):
        self.UI = UI
        #   client labels/buttons
        self.CLIENT_BUTTONS = {
            "PREVIOUS_BUTTON": self.UI.pushButton_5,
            "NEXT_BUTTON": self.UI.pushButton_6,
            "LOAD_IMAGES_BUTTON": self.UI.pushButton_3,
        }
        self.CLIENT_LABELS = {
            "STATUS_LABEL": self.UI.label_5,
            "IMAGE_LABEL": self.UI.label,
            "IMAGE_TO_LABEL_LABEL": self.UI.label_2,
            "CLASSES_LABEL": self.UI.label_3,

            "IMAGE_SET": self.UI.label_6, #the whole image aka the pool table image
            "LABEL_SET": self.UI.label_7, #the image to label

        }
        #   client toggled data
        self.TOGGLED_DATA = {
            "LOADED_IMGS": False,
            "GO_NEXT" : False, #client is allowed to go process the next image when finished labeling

        }
        self.LOADED_IMAGES=[]
        self.LOADED_CLASSES=[]

        #GRAB THE CHECKPOINT FILE


        self.STATUS = self.CLIENT_LABELS['STATUS_LABEL']

        #   update main status to load in images/classes
        self.UPDATE_STATUS("LOAD IN IMAGES/CLASSES", "orange")
        #   set path
        self.IMAGES_DIR=join(current_dir,"./IMAGES")
        self.CLASSES_DIR=join(current_dir,"./classes.txt")
        # # GRAB CHECKPOINTS DATA IN JSON FORMAT
        # self.CHECKPOINTS=json.loads(open(join(current_dir,"./checkpoint.json"),mode='r').read())


        self.CLIENT_BUTTONS['LOAD_IMAGES_BUTTON'].clicked.connect(partial(self.LOAD_IMAGES))

        self.CLIENT_BUTTONS['NEXT_BUTTON'].clicked.connect(partial(self.UPDATE_REFERENCE,1))
        self.CLIENT_BUTTONS['PREVIOUS_BUTTON'].clicked.connect(partial(self.UPDATE_REFERENCE, -1))
        # CLIENT DATA HANDLING
        self.CURRENT_INDEX=0 #reference index to each image
        self.QIMAGE=QImage()

    # go through next/previous image
    # todo: load in checkpoints for each image if applicable

    def UPDATE_REFERENCE(self,index): #1,-1

        if self.TOGGLED_DATA['LOADED_IMGS']:

            if index > 0: #positive 1
                #make sure we dont go past the max images
                #print(self.CURRENT_INDEX,len(self.LOADED_IMAGES))
                if (self.CURRENT_INDEX != (len(self.LOADED_IMAGES)-1) ): #0,1
                    #we add to current_index value to reference image
                    self.CURRENT_INDEX=self.CURRENT_INDEX+1 #1,
                    self.SET_IMAGE(self.CURRENT_INDEX)
                else:
                    self.UPDATE_STATUS("LAST IMAGE!","orange")

            if index < 0:
                #make sure not to go past 0 for referencing non existent images
                if self.CURRENT_INDEX != 0: #if current_index is not 0 (or first image in list)
                    self.CURRENT_INDEX=self.CURRENT_INDEX-1
                    self.SET_IMAGE(self.CURRENT_INDEX)
                else:
                    self.UPDATE_STATUS("FIRST IMAGE!","orange") #if it is the first image in list(or 0) then we can only add (update to next reference!)


        #update the image once we have a reference update


        else:
            self.UPDATE_STATUS("PLEASE LOAD IN IMGS/CLASSES","red")

    def SET_IMAGE(self,index):
        #   first update checkpoints file
        #   GRAB CHECKPOINTS DATA IN JSON FORMAT
        IMAGE_NAME = self.LOADED_IMAGES[index]  # grab current image name OF POOL-TABLE
        #print(IMAGE_NAME)

        #   SINCE JSON FORMAT PRODUCES DOUBLE QUOTES ON EACH INDEX OF DICT WE WANT TO REVERSE THAT
        #   EX) "{"1663881461000.jpg": {"0":" <-- "0"(string)-->0(int)
        CHECKPOINT_DATA=json.load(open(join(current_dir, "checkpoint.json"), "r"))
        NEW_DATA={}
        for x in range(len(list(CHECKPOINT_DATA))):
            IMG=list(CHECKPOINT_DATA)[x]
            for y in range(len(list(CHECKPOINT_DATA[IMG]))):
                LABEL_NUMBER=list(CHECKPOINT_DATA[IMG])[y]
                FIRST_NUM=NEW_DATA.get(IMG,None)
                if FIRST_NUM is None:
                    NEW_DATA[IMG]={} #create the empty data set
                    #NEW_DATA[IMG][int(LABEL_NUMBER)]=CHECKPOINT_DATA[IMG][LABEL_NUMBER]
                NEW_DATA[IMG][int(LABEL_NUMBER)]=CHECKPOINT_DATA[IMG][LABEL_NUMBER]

        #print(NEW_DATA[IMG])
        self.CHECKPOINTS=NEW_DATA




        # remove class labels output (before updating next valid reference)
        OUTPUT_COUNT=self.UI.verticalLayout_7.count()
        for x in range(OUTPUT_COUNT):
            self.UI.verticalLayout_7.itemAt(x).widget().deleteLater()
        # grab image from index number
        TABLE_IMAGE,DETECTED_BALLS_INFO,DETECTED_BALLS_IMAGE=DETECT_CUE_BALL(self.IMAGES_DIR + "/" + self.LOADED_IMAGES[index])






        # update the current image reference index text
        # the current label / total number of labels
        self.CLIENT_LABELS['IMAGE_LABEL'].setText(f"CURRENT IMAGE [{IMAGE_NAME}] | [{self.CURRENT_INDEX+1}]/[{len(self.LOADED_IMAGES)}]")
        #self.CLIENT_LABELS['CLASSES_LABEL'].setText(f"CLASSES LOADED [{len(DETECTED_BALLS_INFO)}] |")
        # check if in checkpoints
        if not (IMAGE_NAME in self.CHECKPOINTS):
            self.CHECKPOINTS[IMAGE_NAME] = {}
            # add to checkpoint data
            for label_number in range(len(DETECTED_BALLS_INFO)):
                DETECTED_BALL_COORDINATE = str((DETECTED_BALLS_INFO[label_number][1][0], DETECTED_BALLS_INFO[label_number][1][1]))
                # print(label_number,DETECTED_BALL_COORDINATE)
                DETECTED_BALL_BOX_COORDINATE = str((DETECTED_BALLS_INFO[label_number][1][2], DETECTED_BALLS_INFO[label_number][1][3]))
                self.CHECKPOINTS[IMAGE_NAME][label_number] = [False, False, DETECTED_BALL_COORDINATE,DETECTED_BALL_BOX_COORDINATE]

        #CREATE THE LABEL FOR EACH


        #   SET LABELED POOL TABLE IMAGE

        #   UPDATE ORIGINAL POOL TABLE IMAGE IF CLIENT HAS ALREADY LABELED EACH CUE BALL ACCORDINGLY
        self.QIMAGE.loadFromData(UPDATE_LABELED_IMG(IMAGE_NAME, self.CHECKPOINTS[IMAGE_NAME], False))
        self.CLIENT_LABELS['IMAGE_SET'].setPixmap(QPixmap(self.QIMAGE))
        self.CLIENT_LABELS['IMAGE_SET'].setScaledContents(True)
        self.CLIENT_LABELS['IMAGE_SET'].setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

        for label_number in range(len(DETECTED_BALLS_INFO)):

                #   CREATE EACH FRAME FROM LOADED DATA FROM CLIENT DIRECTORY
                CREATE_CLASS_FRAME(self.UI,[self.CHECKPOINTS,label_number,self.LOADED_CLASSES,IMAGE_NAME]) #TODO: SENDING DATA TO CREATE CLASS FRAME

        #   LOAD DETECTED BALLS IMAGE SO CLIENT CAN SEE WHAT TO LABEL
        self.QIMAGE.loadFromData(DETECTED_BALLS_IMAGE)
        self.CLIENT_LABELS['LABEL_SET'].setPixmap(QPixmap(self.QIMAGE))
        self.CLIENT_LABELS['LABEL_SET'].setScaledContents(True)
        self.CLIENT_LABELS['LABEL_SET'].setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

        # UPDATE TEXT
        self.CLIENT_LABELS['CLASSES_LABEL'].setText(f"CLASSES LOADED [{len(self.LOADED_CLASSES)}] | TO LABEL [{len(DETECTED_BALLS_INFO)}]")



    # load in client self labeling
    def SELF_LABEL(self,index,all_labels_data):
        #   start from loaded image to next cue ball to label
        #   to label text
        self.CLIENT_LABELS['CLASSES_LABEL'].setText(f"TO-LABEL [{len(all_labels_data)}] [ITEMS] | CLASSES LOADED [{len(self.LOADED_CLASSES)}] | LABELING [{index}]/[{len(all_labels_data)}]")
        self.CLIENT_LABELS['IMAGE_TO_LABEL_LABEL'].setText(f"CURRENT LABELING [{index}]")

    # load in images and classes
    def LOAD_IMAGES(self):
        #   check if client has already loaded in data
        if not(self.TOGGLED_DATA['LOADED_IMGS']):
            #   check if directory is empty
            if not(len(os.listdir(self.IMAGES_DIR)) == 0):
                #   load in images from client dir
                for path in os.listdir(self.IMAGES_DIR):
                    self.LOADED_IMAGES.append(path)
                #   load in classes from client dir
                with open(self.CLASSES_DIR) as f:
                    for line in f:
                        self.LOADED_CLASSES.append(str(line).strip())
                self.TOGGLED_DATA['LOADED_IMGS']=True
                #   load in the first image
                self.SET_IMAGE(self.CURRENT_INDEX)
                #print(self.LOADED_IMAGES,self.LOADED_CLASSES)

                self.CLIENT_BUTTONS['LOAD_IMAGES_BUTTON'].setStyleSheet("color: Green")
                self.UPDATE_STATUS("CLASSES/IMAGES LOADED!","green")
            else:
                self.UPDATE_STATUS(f"IMAGES FOLDER IN DIRECTORY IS EMPTY!","red")
        else:
            self.UPDATE_STATUS("CLASSES/IMAGES ALREADY LOADED IN!","red")

    # update status of client program backend
    def UPDATE_STATUS(self, text, color):
        self.STATUS.setText(f"<span style=\"color:{color};\" >[STATUS]: {text} </span>")
