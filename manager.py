import cv2 as cv
import numpy as np
import time


class CaptureManager:

    def __init__(self,caputureObject,previewWindow=None,flipWindow=False):
        
        self.captureObject = caputureObject
        self.previewWindow = previewWindow
        self.flipWindow = flipWindow

        self.isFrameProcessed = False
        self.currentFrame = None
        self.outputImageFile = None
        self.outputVideoFile = None
        self.videoEncoding = None
        self.videoWriter = None


        self.startTime = None
        self.framesProcessed = 0
        self.fpsEstimate = None


    @property
    def frame(self):
        if self.isFrameProcessed and self.currentFrame is None:
            _, self.currentFrame = self.captureObject.retrieve(
                self.frame, self.channel)
        return self._frame
    
    @property
    def isWritingImage(self):
        return self._imageFilename is not None
    
    @property
    def isWritingVideo(self):
        return self._videoFilename is not None


