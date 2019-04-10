import cv2
from scipy.misc import imresize

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),13,(255,0,0),1)
        print(x,y)


img= cv2.imread('./face/Sav.jpg')
img = imresize(img,[600L,600L])
cv2.imwrite('sav.jpg',img)
'''
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
'''