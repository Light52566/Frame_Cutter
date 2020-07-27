# Frame_Cutter
A simple python script for extracting substantially different frames from a video. It's ideal for easy data preparation from a video for a CNN machine learning algorithm.

Just change directory to where you downloaded/cloned the project to in the comand prompt.
Run the script by specifying the file path of the video to be extracted from, and the path for the directory/folder for the extracted frames to be saved in.
Syntax:  ".\frame_cutter.py -f path\video.mp4 -s path\frame_folder"
Sample syntax: .\frame_cutter.py -f C:\Users\User\Desktop\data_prep\desk.mp4 -s C:\Users\User\Desktop\data_prep\frames

# Cropper
There is also a simple cropping script to crop all images in a directory/folder to a designated identical size centered at the middle of the frames.
Syntax: .\cropper.py -f path\frame_folder
