import cv2
import numpy as np
import sys

def show(title, im):
	cv2.imshow(title,im)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

img = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
#ret,thresh = cv2.threshold(img,60,255,cv2.THRESH_TOZERO)
#show("img", thresh)
laplacian = cv2.Laplacian(img, cv2.CV_64F)
#show("img", laplacian)
print(laplacian.var() < 2)
