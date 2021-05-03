import os
import sys
import pyautogui
import numpy as np
import cv2

class ClickCoordinate:
    def __init__(self):
        #self.mask = None
        pass
        

    def analyze_file(self, image_name):
        try:
            self.img = cv2.imread(image_name)
            print("color?")
            self.hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
        except:
            print("File is broken" + image_name, sys.exc_info()[0])
            return

        self.lower_range = np.array([0, 100, 100])
        self.up_range = np.array([0, 255, 255])
        self.create_mask()

    def create_mask(self):
        print("y la mask?")
        self.mask = cv2.inRange(self.hsv,self.lower_range,self.up_range)
        #cv2.imwrite('mask.png',self.mask)
        #cv2.imshow("Image",self.img)
        #cv2.imshow("Mask",self.mask)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

    def click_coord(self):
        ##To find images in the middle
        click_square = 'mask_find.png'
        mask_image = self.mask
        self.pos = pyautogui.locate(click_square,mask_image,grayscale=True,confidence=0.9)
        if not self.pos:
            #For images in top left
            click_square = 'mask_find1.png'
            self.pos = pyautogui.locate(click_square, mask_image, grayscale=True, confidence=0.9)
            if not self.pos:
                #For images bottom left
                click_square = 'mask_find3.png'
                self.pos = pyautogui.locate(click_square, mask_image, grayscale=True, confidence=0.9)

                if not self.pos:
                    #For images middle right
                    click_square = 'mask_find4.png'
                    self.pos = pyautogui.locate(click_square, mask_image, grayscale=True, confidence=0.9)
                    if not self.pos:
                        # For images bottom center
                        click_square = 'mask_find5.png'
                        self.pos = pyautogui.locate(click_square, mask_image, grayscale=True, confidence=0.9)
                        if not self.pos:
                            # For images bottom center
                            click_square = 'mask_find5.png'
                            self.pos = pyautogui.locate(click_square, mask_image, grayscale=True, confidence=0.7)
                            if not self.pos:
                                click_square = 'mask_find1.png'
                                self.pos = pyautogui.locate(click_square, mask_image, grayscale=True, confidence=0.7)
                                if not self.pos:
                                    #For images top center
                                    click_square = 'mask_find2.png'
                                    self.pos = pyautogui.locate(click_square, mask_image, grayscale=True, confidence=0.9)
                                    if not self.pos:
                                        return (0,0)
        #print(self.pos)
        #print(pyautogui.center(self.pos))
        return pyautogui.center(self.pos)
'''
def analyze_clicksFolder(rootDir):
    thisdict = dict()
    analyzer = ClickCoordinate()

    for file in os.listdir(rootDir):
        if file.endswith('_root.png'):
            analyzer.analyze_file(rootDir + '\\' + file)
            x,y = analyzer.click_coord()
            thisdict[file] = (x,y)
    print(thisdict)

analyzer = ClickCoordinate()
analyzer.analyze_file('tempImage/1619991780.4492707_main.py_root.png')
x,y = analyzer.click_coord()
print(x,y)
'''
#rootDir = 'C:\\Users\\Diana R\\Desktop\\15_min\\15_min\\Clicks'
#rootDir = 'C:\\Users\\Diana R\\IdeaProjects\\temp\\tempImage'
#rootDir = 'C:\\Users\\Diana R\\Documents\\agent-build-system\\Causation_Extractor\\eceldData\\small_sample_project\\Clicks'
#analyze_clicksFolder(rootDir)