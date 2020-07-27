

# Import the necessary packages
from skimage.measure import compare_ssim
import argparse
import imutils
from cv2 import cv2
import os
import pathlib


frame_name = 'frame'    #can be edited to determine the general name for the frames that will be extracted/saved
max_similarity = 0.85   #can be edited to choose the maximum similarity for the frames to have between each other

# Construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True, help="Directory of the video that will be used")
ap.add_argument("-s", "--second", required=True, help="Directory for the frames to be saved")
args = vars(ap.parse_args())


# Open the Video file
cap= cv2.VideoCapture(args["first"])
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if (ret == False):
        break
    if (i==0):
        cv2.imwrite(os.path.join(args["second"],frame_name + str(i)+'.jpg'),frame)  #initial frame saved
    else:
        similar = False
        imageB = frame
        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
        for path in pathlib.Path(args["second"]).iterdir(): #iteration to check similarity of current frame with previously saved frames
            if path.is_file():
                imageA = cv2.imread(str(path))
                grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
                score = 1
                (score, diff) = compare_ssim(grayA, grayB, full=True)   #similarity determined with SSIM score
                print(str(path)+"\t"+str(score))
                if score > max_similarity:
                    similar = True
        if not similar:
            cv2.imwrite(os.path.join(args["second"],frame_name + str(i)+'.jpg'),frame)
    i+=1
cap.release()
cv2.destroyAllWindows()

#.\frame_cutter.py -f C:\Users\User\Desktop\data_prep\desk.mp4 -s C:\Users\User\Desktop\data_prep\frames
