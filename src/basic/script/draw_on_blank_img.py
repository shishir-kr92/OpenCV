import cv2
import numpy as np

def show_img(blank_img):
	cv2.imshow("img", blank_img)
	new_img = cv2.cvtColor(blank_img, cv2.COLOR_BGR2GRAY)
	cv2.imshow("img1", new_img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == "__main__":
	blank_img = np.zeros((250, 250, 3), dtype=np.uint8)
	for i in range(100):
		blank_img[100 + i][100 + i][1] = 100

	print(f"shape = {blank_img.shape}")
	show_img(blank_img)