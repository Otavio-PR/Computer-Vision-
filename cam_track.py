import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import time

class ViewCamera: 
    
    
    
    def __init__(self):
        self.capture = cv.VideoCapture(0)
        self.face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
        self.eye_cascade = cv.CascadeClassifier("haarcascade_eye.xml") 
        self.glasses_cascade = cv.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")

    def take_photo(self):
        
        ret, frame = self.capture.read()
        
        plt.imshow(cv.cvtColor(frame, cv.COLOR_BGR2RGB))
        print("Click!")
        cv.imwrite("Mycamera.jpg", frame)
        plt.show()
       
        self.capture.release()
        cv.destroyAllWindows()
        

    def op_video(self):
        while self.capture.isOpened():
            ret, frame = self.capture.read()   
            gray_ver = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            
            faces = self.face_cascade.detectMultiScale(gray_ver, 1.1, 5)
        
            #quadrado no rosto detectado#
            
            for (x,y,wi,he) in faces:
                
                cv.rectangle(frame, (x,y), (x+wi,y+he), (255,0,0, 4))

                eye_gray = gray_ver[y:y+he, x:x+wi]
                eye_color = frame[y:y+he, x:x+wi]
                
                glasses = self.glasses_cascade.detectMultiScale(eye_gray, 1.1, 5)
                eyes = self.eye_cascade.detectMultiScale(eye_gray, 1.1, 5)
                
                for (gx, gy, gw, gh) in glasses:
                    cv.rectangle(eye_color, (gx,gy), (gx+gw, gy+gh), (0,255,0))
                
                if len(glasses) == 0:
                    for (ex, ey, ew, eh) in eyes:
                        cv.rectangle(eye_color, (ex, ey), (ex+ew, ey+eh),(0, 255, 255))
            
            #preciso arrumar precisao
            cv.imshow('WebCam', frame)

            if cv.waitKey(1) & 0xFF == ord('q'):
                break
            
        
    
    
    def main(self):
        #self.take_photo()
        #time.sleep(3)
        self.op_video()
        self.capture.release()
        cv.destroyAllWindows()
       
if __name__ == "__main__":
       
    view = ViewCamera()
    view.main()

    
