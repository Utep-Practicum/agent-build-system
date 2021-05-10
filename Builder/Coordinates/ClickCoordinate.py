import os
import sys
import pyautogui
import numpy as np
import cv2

class ClickCoordinate:
    def __init__(self):
        self.mask = None

    def analyze_file(self,image_name):
        try:
            self.img = cv2.imread(image_name)
          
            self.hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
            
        except Exception as e:
            #print(e)
            print("Cannot detect coordinates " + image_name, sys.exc_info()[0])
            print("Please introduce coordinates manually")
            return

        self.lower_range = np.array([0, 100, 100])
        self.up_range = np.array([0, 255, 255])
        self.create_mask()

    def create_mask(self):
        self.mask = cv2.inRange(self.hsv,self.lower_range,self.up_range)
        #cv2.imwrite('mask.png',self.mask)
        #cv2.imshow("Image",self.img)
        #cv2.imshow("Mask",self.mask)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

    def click_coord(self):
        ##To find images in the middle
        click_square = (r'Builder/Coordinates/mask_find.png')
        mask_image = self.mask
        self.pos = pyautogui.locate(click_square,mask_image,grayscale=True,confidence=0.9)
        if not self.pos:
            #For images in top left
            click_square = (r'Builder/Coordinates/mask_find1.PNG')
            self.pos = pyautogui.locate(click_square, mask_image, grayscale=True, confidence=0.9)
            if not self.pos:
                #For images bottom left
                click_square = (r'Builder/Coordinates/mask_find3.PNG')
                self.pos = pyautogui.locate(click_square, mask_image, grayscale=True, confidence=0.9)

                if not self.pos:
                    #For images middle right
                    click_square = (r'Builder/Coordinates/mask_find4.PNG')
                    self.pos = pyautogui.locate(click_square, mask_image, grayscale=True, confidence=0.9)
                    if not self.pos:
                        # For images bottom center
                        click_square = (r'Builder/Coordinates/mask_find5.PNG')
                        self.pos = pyautogui.locate(click_square, mask_image, grayscale=True, confidence=0.9)
                        if not self.pos:
                            # For images bottom center
                            click_square = (r'Builder/Coordinates/mask_find5.PNG')
                            self.pos = pyautogui.locate(click_square, mask_image, grayscale=True, confidence=0.7)
                            if not self.pos:
                                click_square = (r'Builder/Coordinates/mask_find1.PNG')
                                self.pos = pyautogui.locate(click_square, mask_image, grayscale=True, confidence=0.7)
                                if not self.pos:
                                    #For images top center
                                    click_square = (r'Builder/Coordinates/mask_find2.png')
                                    self.pos = pyautogui.locate(click_square, mask_image, grayscale=True, confidence=0.9)
                                    if not self.pos:
                                        return (0,0)
        #print(self.pos)
        #print(pyautogui.center(self.pos))
        return pyautogui.center(self.pos)
