import cv2 as cv



camera = cv.VideoCapture(0)

fps = 30
size = (int(camera.get(cv.CAP_PROP_FRAME_HEIGHT)),int(camera.get(cv.CAP_PROP_FRAME_WIDTH)))

videoWriter = cv.VideoWriter(
    'MyOutputVid.mp4', cv.VideoWriter_fourcc('m','p','4','v'),
    fps, size)


framesRemaining = 10*fps - 1 # this is for 10 seconds


success, frame = camera.read()

while success and framesRemaining > 0:
    videoWriter.write(frame)
    framesRemaining -= 1
    success,frame = camera.read()

