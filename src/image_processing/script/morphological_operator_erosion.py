import cv2
import numpy as np


def load_img():
	img = np.zeros(shape=(600, 600), dtype=np.uint8)
	imgFont = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(img, 
				text='TEXT',
				org=(60, 500), 
				fontFace=imgFont,
				fontScale=5,
				color=(255,0),
				thickness=30)
	return img

def erode_img(img, kernel_shape=3):
	'''
		in order to erode the image we need to create kernel , a square metrix
		it will erode the boundries of the image 
	'''
	kernel = np.ones(shape=(kernel_shape, kernel_shape), dtype=np.uint8)
	eroded_img = cv2.erode(img, kernel, iterations=2)
	return eroded_img

def add_fore_ground_noise(img):
	white_noise = np.random.randint(low=0, high=2, size=(600, 600), dtype=np.uint8) * 255
	return img + white_noise
	

if __name__ == "__main__":
	img = load_img()
	print(img)
	# eroded_img = erode_img(img)
	noisy_img = add_fore_ground_noise(img)
	clean_img  = erode_img(noisy_img, kernel_shape=5)

	cv2.imshow("original",img)
	cv2.imshow("noisy",noisy_img)
	cv2.imshow("clean_img", clean_img)
	cv2.waitKey(-1)