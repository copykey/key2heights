import cv2
import numpy as np
import sys
import os

def show(title, im):
	cv2.imshow(title,im)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def nothing(x):
	pass

cv2.namedWindow("orig")

def show_canny(im):
	cv2.namedWindow("canny")
	cv2.createTrackbar('low', 'canny', 0, 255, nothing)
	cv2.createTrackbar('high', 'canny', 0, 255, nothing)
	canny = cv2.Canny(im, 0, 255)
	cv2.imshow("orig", im)
	while(1):
		cv2.imshow('canny',canny)
		k = cv2.waitKey(1) & 0xFF
		if k == 27 or k == 115:
			break
		if k == 97:
			sys.exit()
		print(cv2.getTrackbarPos('low', 'canny'))
		canny = cv2.Canny(im, cv2.getTrackbarPos('low', 'canny'), cv2.getTrackbarPos('high', 'canny'))

def pick_best(num_desired, images, t1, t2):
	laplacian_variances = []
	for image in images:
		height, width, _ = image.shape
		#variance = cv2.Laplacian(image, cv2.CV_64F).var()
		#canny = cv2.Canny(image, t1, t2)
		#amtofcanny = np.sum(canny)/(width*height)
		#laplacian_variances.append([image, amtofcanny]) #amtofcanny * width * variance])
		#canny = cv2.Canny(image, 60, 135)
		#laplacian_variances.append([image, cv2.Laplacian(canny, cv2.CV_64F).var() * width])
		show_canny(image)
		break
	laplacian_variances.sort(key=lambda x: -x[1])
	return [i[0] for i in laplacian_variances[0:num_desired]]

images = []
for i in range(2, len(sys.argv)):
	images.append(cv2.imread(sys.argv[i], cv2.IMREAD_COLOR))


best = pick_best(int(sys.argv[1]), images, 255, 255)
for i in range(0, len(best)):
	cv2.imwrite("best/" + str(i) + ".jpg", best[i])

"""
for t1 in range(0, 255, 30):
	for t2 in range(0, 255, 30):
		foldername = "can/" + str(t1) + "_" + str(t2) + "/"
		os.system("mkdir " + foldername)
		best = pick_best(int(sys.argv[1]), images, t1, t2)
		for i in range(0, len(best)):
			cv2.imwrite(foldername + str(i) + ".jpg", best[i])
			#show("good image " + str(i+1), best[i])
"""
