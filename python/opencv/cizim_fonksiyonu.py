import numpy as np
import cv2

canvas=np.zeros((512,512,3),dtype=np.uint8) +190

cv2.line(canvas,(0,0),(512,512),(255,0,0),thickness=5) #düz çizgi
            #baslangic   son     renk      kalınlık
cv2.rectangle(canvas,(20,20),(50,50),(0,255,0),-1) #dikdörtgen
cv2.rectangle(canvas,(10,10),(180,180),(0,255,0),-1)

cv2.circle(canvas,(250,250),100,(255,0,0),-1)


cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()


