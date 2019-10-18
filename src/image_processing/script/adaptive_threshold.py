import cv2

path="/home/shishir/study/code/openCV/resource"
img_file_name = "crossword.jpg"

def main():
	raw_img = cv2.imread(f"{path}/{img_file_name}", 0)

	adaptive_mean_c = cv2.adaptiveThreshold(raw_img,
											 255, 
											 cv2.ADAPTIVE_THRESH_MEAN_C,
											 cv2.THRESH_BINARY,
											 11,
											 8)
	adaptive_gaussian_c = cv2.adaptiveThreshold(raw_img, 
							                    255, 
							                    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
							                    cv2.THRESH_BINARY, 
							                    11,
							                    8)
	blended_img = cv2.addWeighted(adaptive_mean_c, 
								  .5, 
								  adaptive_gaussian_c,
								  0.5, 
								  0)
	cv2.imshow("raw_img", raw_img)
	cv2.imshow("adaptive_mean_c", adaptive_mean_c)
	cv2.imshow("adaptive_gaussian_c", adaptive_gaussian_c)
	cv2.imshow("blended_img", blended_img)
	
	cv2.waitKey(-1)


if __name__ == "__main__":
	main()