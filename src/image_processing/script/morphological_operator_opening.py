import cv2
import numpy as np


def load_img():
	img = np.zeros(shape=(600, 600))
	imgFont = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(img, 
				text='ABCD',
				org=(60, 500), 
				fontFace=imgFont,
				fontScale=5,
				color=(255,0),
				thickness=30)
	return img


def add_background_noise(img):
	'''
		add noise to black background
	'''
	white_noise = np.random.randint(low=0, high=2, size=(600, 600), dtype=np.uint8) * 255
	return white_noise + img 

def add_foreground_noise(img):
	'''
		add noise to white fore ground
	'''
	black_noise = np.random.randint(low=0, high=2, size=(600, 600)) * -255
	black_noise_img = black_noise + img
	black_noise_img[black_noise_img == -255] = 0
	cv2.imshow("noise_img", black_noise_img)
	return black_noise_img


def opening(src):
	'''
		opening is an erosion followed by dilation using same structural element
	'''
	kernel = np.ones(shape=(5,5), dtype=np.uint8)
	return cv2.morphologyEx(src, cv2.MORPH_DILATE, kernel)

if __name__ == "__main__":
	img = load_img()
	noisy_img = add_foreground_noise(img)
	# dst = opening(noisy_img)
	# cv2.imshow("img", img)
	# cv2.imshow("noise_img", noisy_img)
	# cv2.imshow("dst", dst)
	cv2.waitKey(-1)
	cv2.destroyAllWindows()
