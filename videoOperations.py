import cv2 as cv

# can also specify 0 here to indicate that to use the camera of the device
videoCapture = cv.VideoCapture("someVideo.avi")

fps = videoCapture.get(cv.CAP_PROP_FPS)
size = (int(videoCapture.get(cv.CAP_PROP_FRAME_WIDTH)), int(videoCapture.get(cv.CAP_PROP_FRAME_HEIGHT)))


videoWriter  = cv.VideoWriter(
     'MyOutputVid.avi',                          # Output filename
    cv.VideoWriter_fourcc('I','4','2','0'),   # Four-character code (FourCC)
    fps,                                        # Frames per second
    size                                        # Frame size (width, height)
)


success,frame = videoCapture.read()

while success:
    videoWriter.write(frame)
    success,frame = videoCapture.read()
