import cv2 as cv

class Camera:
    def __init__(self):
        self.windowName = "CameraFeed"
        self.videoObject = cv.VideoCapture(0)
        self.clicked = False
    
    def onMouse(self,event,x,y,flags,param):
        if event == cv.EVENT_LBUTTONUP:
            self.clicked=True
        
    def run(self):
        cv.namedWindow(self.windowName)
        cv.setMouseCallback(self.windowName,self.onMouse)

        try:
            success,frame = self.videoObject.read()

            while success and cv.waitKey(1)==-1 and not self.clicked:
                cv.imshow(self.windowName,frame)

                success,frame = self.videoObject.read()
        finally:
            cv.destroyWindow(self.windowName)
            self.videoObject.release()


if __name__ == "__main__":
    object = Camera()
    object.run()

