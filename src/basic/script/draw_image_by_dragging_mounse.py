import numpy as np
import cv2

## Initialize some global variable 
drawing = False
ix , iy = -1, -1


## call back function
def draw_rectange(event, x, y,flags, params):
	global ix, iy, drawing
	
	if event == cv2.EVENT_LBUTTONDOWN:
		ix = x
		iy = y 
		drawing = True
	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing:
			cv2.rectangle(blank_image, pt1=(ix, iy), pt2=(x,y), color=(250, 0, 0), thickness=-1)
	elif event == cv2.EVENT_LBUTTONUP:
		cv2.rectangle(blank_image, pt1=(ix, iy), pt2=(x,y), color=(250, 0, 0), thickness=-1)
		drawing = False


## main function
def main(blank_image):
	cv2.namedWindow("draw_image")
	cv2.setMouseCallback("draw_image", draw_rectange)
	# cv2.imshow("draw_image", blank_image)
	# cv2.waitKey(-1)
	while True:
		cv2.imshow("draw_image", blank_image)
		if cv2.waitKey(4) & 0xFF == 27:
			break
	cv2.destroyAllWindows()


if __name__ == "__main__":
	blank_image = np.zeros(shape=(512, 512, 3))
	main(blank_image)

