import cv2
from find_best import find_best
import video_to_frames
import find_rectangle

video = video_to_frames.path_to_video("vid.mp4")
frames = video_to_frames.video_to_frames(video)

key_images = []
for frame in frames:
	success, key_image, _ = find_rectangle.process(frame)
	if success:
		key_images.append(key_image)
results = find_best(5, key_images)

for image in results:
	cv2.imshow("image", image)
	cv2.waitKey(0)
cv2.destroyAllWindows()
