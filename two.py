import numpy as np
import cv2
img = cv2.imread(r'C:\Users\fcbba\Pictures\6J5A9866.JPG',1)
#img = np.zeros([512,512,3],np.uint8) # h,w
# line
img = cv2.line(img,( 0,0), (255,255), (255,0,0), 5) # here (b,r,g) if b=255 and r,g=0 we get blue
# arrow line
img = cv2.arrowedLine(img,( 300,99),(255,300), (0,255,0), 5)
# rectangle here two coordinates are left top and right bottom
img = cv2.rectangle(img,( 384,0),(510,128), (0,0,255), 5) # if we give -1 as thickness the rect will be filled with color
# circle with center,radius,color,thickness
img = cv2.circle(img,(440,63),63,(0,255,0),-1)
# text
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img,'OPENCV',(10,500),font,4,(255,255,0),10,cv2.LINE_AA)
cv2.imshow('frame',img)

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
    cv2.imwrite('mm.JPG',img)
