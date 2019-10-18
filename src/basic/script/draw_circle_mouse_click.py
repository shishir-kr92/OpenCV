import cv2
import numpy as np
import time
import random

blank_img = np.zeros((512, 512, 3))



def draw_circle(event, x_coordinate, y_coordinate, flags, param):
	if event == cv2.EVENT_LBUTTONDOWN:
		cv2.circle(blank_img, 
				center = (x_coordinate, y_coordinate), 
				radius=100,
				color=(250,250,0),
				thickness=-1)
	if event == cv2.EVENT_RBUTTONDOWN:
		cv2.circle(blank_img, 
				center = (x_coordinate, y_coordinate), 
				radius=100,
				color=(0,0,250),
				thickness=-1)

def main():
	cv2.namedWindow("image1")
	cv2.setMouseCallback("image1", draw_circle)
	
	while True:
		cv2.imshow("image1",blank_img)

		if cv2.waitKey(20) & 0xFF == 27:
			break

if __name__ == "__main__":
	main()


