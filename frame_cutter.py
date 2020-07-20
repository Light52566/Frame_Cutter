

# 1. Import the necessary packages
from skimage.measure import compare_ssim
import argparse
import imutils
from cv2 import cv2
import os
import pathlib



# 2. Construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True, help="Directory of the video that will be used")
ap.add_argument("-s", "--second", required=True, help="Directory for the frames to be saved")
args = vars(ap.parse_args())

# Opens the Video file
cap= cv2.VideoCapture(args["first"])
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if (ret == False):
        break
    if (i==0):
        cv2.imwrite(os.path.join(args["second"],'frame'+str(i)+'.jpg'),frame)
    else:
        similar = False
        imageB = frame
        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
        for path in pathlib.Path(args["second"]).iterdir():
            if path.is_file():
                imageA = cv2.imread(str(path))
                grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
                score = 1
                (score, diff) = compare_ssim(grayA, grayB, full=True)
                print(str(path)+"\t"+str(score))
                if score > 0.7:
                    similar = True
        if not similar:
            cv2.imwrite(os.path.join(args["second"],'frame'+str(i)+'.jpg'),frame)
    #cv2.imwrite(os.path.join(args["second"],'frame'+str(i)+'.jpg'),frame)
    i+=1
cap.release()
cv2.destroyAllWindows()

#.\frame_cutter.py -f C:\Users\User\Desktop\data_prep\desk.mp4 -s C:\Users\User\Desktop\data_prep\frames