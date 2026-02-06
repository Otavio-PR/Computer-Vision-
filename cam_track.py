import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import time

class ViewCamera: 
    
    def __init__(self):
        self.capture = cv.VideoCapture(0)
    
    def take_photo(self):
        
        ret, frame = self.capture.read()
        
        plt.imshow(cv.cvtColor(frame, cv.COLOR_BGR2RGB))
        print("Click!")
        cv.imwrite("Mycamera.jpg", frame)
        plt.show()
       
        self.capture.release()
        cv.destroyAllWindows()
        

    def rec_video(self):
        while self.capture.isOpened():
            ret,frame = self.capture.read()
            cv.imshow('WebCam', frame)

            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        
        self.capture.release()
        cv.destroyAllWindows()
    
    def main(self):
        self.take_photo()
        #time.sleep(3)
        #self.rec_video()
       
if __name__ == "__main__":
       
    view = ViewCamera()
    view.main()

    
