import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
import cv2

img_path = "/home/shishir/study/code/openCV/resource/test.JPG"
def main():
	try:
		'''
			cv2 read image in BGR order
		'''
		pic = cv2.imread(img_path)
	except FileNotFoundError:
		pic = cv2.imread("resource/test.JPG")

	pic_array = cv2.resize(pic, (512, 512))
	fixed_image = cv2.cvtColor(pic_array, cv2.COLOR_BGR2RGB)
	print(f"shape = {pic_array.shape}")
	# print(f"shape = {fixed_image.shape}")
	
	
	b = fixed_image.copy()
	b[:,:,1] = 0
	b[:,:,2] = 0
	
	g = pic_array.copy()
	g[:,:,1] = 0
	g[:,:,2] = 0

	r = fixed_image.copy()
	r[:,:,0] = 0
	r[:,:,1] = 0

	cv2.imshow("raw", pic_array)
	cv2.imshow("fixed", fixed_image)
	'''
		From reading to displaying , for all operation color
		channel in cv2 is in BGR sequence
	'''
	cv2.imshow("blue", b)
	cv2.imshow("green", g)
	# cv2.imshow("red", r)
	plt.imshow(fixed_image)

	cv2.waitKey(0)
	cv2.destroyAllWindows()


if __name__ == "__main__":
	main()
	