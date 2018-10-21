import cv2
from find_best import find_best
import video_to_frames
import find_rectangle

video = video_to_frames.path_to_video("../../vid3.mp4")
frames = video_to_frames.video_to_frames(video)

key_images = []
for frame in frames:
	#cv2.waitKey(1)
	#cv2.imshow("image", frame)
	#ret, th3 = cv2.threshold(frame,90,255,cv2.THRESH_BINARY)
	#th3 = cv2.adaptiveThreshold(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY),255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
	#cv2.imshow("th3", th3)
	cv2.waitKey(1)
	success, key_image, draw = find_rectangle.process(frame)
	if success:
		key_images.append(key_image)
	cv2.imshow("draw", draw)
	cv2.waitKey(1)
results = find_best(5, key_images)

for image in results:
	cv2.imshow("image", image)
	cv2.waitKey(0)

"""
sobely = cv2.Sobel(results,cv2.CV_64F,0,1,ksize=1)
cv2.imshow("image", sobely)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
