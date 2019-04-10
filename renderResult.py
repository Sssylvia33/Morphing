import cv2
import os
dir_path ='./result2'
images = []
for f in os.listdir(dir_path):
    if f.endswith('jpg'):
        images.append(f)



image_path = os.path.join(dir_path, images[0])
frame = cv2.imread(image_path)
height, width, channels = frame.shape

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'DIVX') # Be sure to use lower case
out = cv2.VideoWriter('output.mp4', fourcc, 10, (width, height))

for image in images:

    image_path = os.path.join(dir_path, image)
    frame = cv2.imread(image_path)

    out.write(frame) # Write out frame to video

    #cv2.imshow('video',frame)
    #if (cv2.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
     #   break

# Release everything if job is finished
out.release()
#cv2.destroyAllWindows()