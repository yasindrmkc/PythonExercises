import cv2


img = cv2.imread("kaplan.jpg") #resim okuma
img=cv2.resize(img,(640,480))  #resim boyutunu ayarlama
cv2.namedWindow("Image",cv2.WINDOW_NORMAL) #size büyütüp küçültmeye göre değişiyor
cv2.imshow("Image",img) #resimi gösterme
cv2.waitKey(0) #resim tuşa basana kadar durucak
cv2.destroyAllWindows()
#cv2.imwrite("klon1.jpg",img)   resimi kopyalama 
