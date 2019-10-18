import cv2
import numpy as np


def draw_shape(blank_img):
	cv2.namedWindow("image_one")
	cv2.rectangle(blank_img, pt1=(100, 100), pt2=(300, 300), color=(250,0,0), thickness=-1)
	cv2.circle(blank_img, center = (200, 200), radius = 90, color = (0,250,0), thickness=-1)
	cv2.line(blank_img, pt1=(100,100), pt2=(300,300), color=(0,0,250), thickness=10)

	cv2.imshow("image_one", blank_img)
	cv2.waitKey(-1)
	cv2.destroyAllWindows()




if __name__ == "__main__":
	blank_img = np.zeros((512,512,3), dtype=np.uint8)

	draw_shape(blank_img)