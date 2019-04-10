import numpy as np
from imutils import face_utils
import dlib
import cv2
from scipy.misc import imresize

# p = our pre-treined model directory, on my case, it's on the same script's diretory.
p = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(p)

#filename1 = './face/Sav.jpg'
filename1 = './face/Rost.jpg'

    
    # Read images
img1 = cv2.imread(filename1)
img1 = np.asarray(img1)
img1 = imresize(img1,[600L,600L])
#img2 = cv2.imread(filename2)
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
#gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#cv2.imshow("Output", img1)
rects = detector(gray1, 1)

landFile = open('rostLandmarks.txt','w')

# For each detected face, find the landmark.
for item in rects:
    x1 = item.left()
    y1 = item.top()
    x2 = item.right()
    y2 = item.bottom()
    cv2.rectangle(img1,(x1,y1),(x2,y2),(255,0,0),3)    
    
    # Make the prediction and transfom it to numpy array
    shape = predictor(gray1, item)
    shape = face_utils.shape_to_np(shape)
    # Draw on our image, all the finded cordinate points (x,y) 
    for (x, y) in shape:
        #cv2.circle(img1, (x, y), 2, (0, 255, 0), 1)
        landFile.write('{} {}\n'.format(x,y))
        
    landFile.close()
    
    # Show the image
#cv2.imshow("Output", img1)
#if cv2.waitKey(1) & 0xFF == ord('q'):
#    cv2.destroyAllWindows()