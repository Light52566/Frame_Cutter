import argparse
import imutils
from cv2 import cv2
import os
import pathlib

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True, help="Directory of the frames that will be cropped")
#ap.add_argument("-s", "--second", required=True, help="Directory for the cropped frames to be saved")
args = vars(ap.parse_args())

height = 214
width = 214

for path in pathlib.Path(args["first"]).iterdir():
        if path.is_file():
            img = cv2.imread(str(path))
            y = img.shape[0]
            x = img.shape[1]
            if x > width and y > height:
                y = y // 2
                x = x // 2
                crop_img = img[y-(height//2):y+(height//2), x-(width//2):x+(width//2)]
                cv2.imwrite(str(path),crop_img)
            else:
                print(str(path) + "\t frame too small")            
#cv2.imwrite(os.path.join(args["second"],'frame'+str(i)+'.jpg'),frame)