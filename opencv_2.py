import cv2
import numpy as np

def show(title, im):
	cv2.imshow(title,im)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

bounds = 5

img = cv2.imread("ojas.png", cv2.IMREAD_GRAYSCALE)
ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
out = thresh.copy()
height, width = img.shape
for y in range(bounds, height-bounds):
	for x in range(bounds, width-bounds):
		if thresh[y][x]:
			for i in range(1, bounds):
				if thresh[y][x+i] == 0 and thresh[y][x-i] == 0:
					out[y][x] = 0
				if thresh[y+i][x] == 0 and thresh[y-i][x] == 0:
					out[y][x] = 0
				if thresh[y+i][x-i] == 0 and thresh[y-i][x+i] == 0:
					out[y][x] = 0
				if thresh[y+i][x+i] == 0 and thresh[y-i][x-i] == 0:
					out[y][x] = 0


show("img", out)
